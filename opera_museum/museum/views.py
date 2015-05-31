# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render, render_to_response, HttpResponse, redirect, RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from models import Entry, Tag

from museum.tasks import add
from django.template import loader
import json
import logging

'''
    index ---> 首页

    entry_detail ----> 获得详细页面 detail.html

    entry_category ----> 获取某个目录下的词条

    get_entry_json ----> 获取词条json 信息返回

'''

# set a logger
logger = logging.getLogger(__name__)


def index(request):
    return render_to_response("index.html")


def link_content(entry):
    content = entry.content

    for relate_entry in entry.relate_entry.all():
        name = relate_entry.name
        name_len = len(name)
        try:
            pos = content.find(name)
        except ValueError, e:
            logger.error(e)
            pos = -1
        while (pos != -1):
            content_list = list(content)
            insert_str = "<a href='entry_detail/?id=%s'>" % (str(relate_entry.id))
            content_list.insert(pos, insert_str)
            content_list.insert(pos + name_len + 1, "</a>")
            content = "".join(content_list)
            try:
                pos = content.find(name, pos + name_len + len(insert_str) + len("</a>"))
            except ValueError, e:
                logger.error(e)
                pos = -1
    print(content)
    return "'" + content + "'"


# look up detail for appointed entry
def entry_detail(request):
    '''
    entry detail description in detail page
    :param request:
    :return:
    '''
    if request.method == 'GET':
        query_id = request.GET['id']
        entries = Entry.objects.all().filter(id=query_id)

        if not entries:
            return render_to_response("404.html")
        else:
            # add entry watched
            if len(entries) > 1:
                # TODO If more than 1 entries , try to redirect to another page
                return HttpResponse("")
            else:
                entry = entries.first()
                if entry.watched <= 1000:
                    entry.watched += 1

                name = entry.name
                content = link_content(entry)
                carousel_images = [img.image_url.url for img in entry.image_set.all()]
                carousel_description = entry.image_set.all().first().description
                video_name = entry.video_name
                video_url = entry.video_url
                video_description = entry.video_description
                relate_entry = ['haha', 'hehe']

                return render_to_response("entry_detail.html",
                                          {'name': name
                                              , 'content': content.split('\n')
                                              , 'carousel_images': carousel_images
                                              , 'carousel_description': carousel_description
                                              , 'video_name': video_name
                                              , 'video_url': video_url
                                              , 'video_description': video_description
                                              , 'support': entry.like
                                              , 'watched': entry.watched})
    return render_to_response("")


@csrf_exempt
def get_entry_detail_json(request):
    '''
    for Entry detail page water fall
    :param request:
    :return:
    '''
    if request.method == "GET":
        id = request.GET['id']

        entry = Entry.objects.all().filter(id=id)
        entry = entry.first()

        if not entry:
            return HttpResponse("fail")
        else:
            ret_json = '''

            <div class="waterfall-item">
            <div style="width:995">
                <p>''' + link_content(entry) + '''</p>

            </div>
            <div class="waterfall-item" >
                <img src="http://wlog.cn/demo/waterfall/images/001.jpg" width="995" height="288">
            </div>
            '''
            if entry.video_url:
                ret_json = ret_json + '''
                <div class="waterfall-item" >
                    <embed src=''' + entry.video_url + '''
                     quality="high" width="995" height="400" align="middle" allowScriptAccess="always" allowFullScreen="true" mode="transparent" type="application/x-shockwave-flash"></embed>
                </div>
                '''
            return HttpResponse(content=ret_json, content_type="html")

    return HttpResponse("")


# support the entry
@csrf_exempt
def like_entry(request):
    if request.method == 'POST':
        entry_id = request.POST['entryId']
        entry = Entry.objects.all().filter(id=entry_id)[0]

        if entry.like < 1000:
            entry.like += 1
            entry.save()
    return HttpResponse("success")


# look up entries in the same category
def entry_category(request):
    if request.method == 'GET':
        tag_key = request.GET['tag_key']
        tag_value = request.GET['tag_value']

        tag = Tag.objects.all().filter(key=tag_key, value=tag_value)
        # reverse query
        entries = tag.entry_set.all()
        print(entries)
    elif request.method == "POST":
        pass


def generate_entry_html(entry):
    _max_content_len = 200  # max length of entry content

    head = '<div class="waterfall-item" entryId=' + str(entry.id) + '>'
    tail = '</div>'
    img_func = lambda entry: entry.image_set.all().first()
    img = img_func(entry)
    standard_width = 249
    height = img.getImageSize()[1] * 1.0 / img.getImageSize()[0] * standard_width

    img_html = '<img src="' + img.image_url.url + '" width="249" height="' + str(height) + '">'

    title = '<p>' + entry.name + '</p>'
    content = '<div style="width: 249px"> <p>' + entry.content[0:_max_content_len] + '</p></div>'

    like_img = '<img id="like" height="20" weight="20" src="/static/museum/img/like.png" />'
    watch_img = '<img id="watch" height="20" weight="20" src="/static/museum/img/watched.png" />'
    like_and_watch = '<div>' + like_img + '<p>' + str(entry.like) + '</p>' + watch_img + '<p>' + str(
        entry.watched) + '</p>' + '</div>'
    ret_html = head + img_html + title + content + like_and_watch + tail

    return ret_html


def get_relate_entry_json(request):
    if request.method == "GET":
        id = request.GET['id']
        entry = Entry.objects.all().filter(id=id)

        try:
            entry = entry[0]
        except IndexError as e:
            logger.error(e)
            return HttpResponse('/')

        relate_entry_html_list = [generate_entry_html(related) for related in entry.relate_entry.all()]
        ret_data = "".join(relate_entry_html_list)

        return HttpResponse(content=ret_data, content_type="html")

    try:
        raise RuntimeError("/get_slider_json does not support GET method")
    except:
        logger.error("get_slider_json does not support GET method")
    finally:
        return HttpResponse("/")


def get_entry_json(request):
    '''
    for Index entry json request
    :param request:
    :return:
    '''
    tag_key = tag_value = page = None
    if request.method == "GET":
        tag_key = request.GET['tag_key']
        tag_value = request.GET['tag_value']
        page = request.GET['page']

    tag = Tag.objects.all().filter(key=tag_key, value=tag_value)
    # Tag name is error , return failed to json
    if not tag:
        return HttpResponse("failed")

    entries = Entry.objects.all().filter(tags=tag)

    # return json format data to waterfall
    total = len(entries)

    entry_list = [
        {
            # TODO dirty code here
            "image": entry.image_set.all().first().image_url.url,  # pay attention to last .url
        }
        for entry in entries if entry.image_set.all().first()
    ]
    length = len(entry_list)
    start = (int(page)-1)*10
    end = start+10

    if start > length:
        return HttpResponse("")

    if end>length:
        end = length

    entry_list = entry_list[start: end]
    print(entry_list)
    json_data = json.dumps({
        "total": total,
        # "result": json.dumps(entry_list),
        "result": entry_list,
    })
    return HttpResponse(content=json_data, content_type='application/json')


def get_slider_json(request):
    entry_list = Entry.objects.all().filter(slider_show=True)

    items = [

        '<div><img src="' + entry.image_set.all()[0].image_url.url + '" height = "293" width="513" /></div>'

        for entry in entry_list
    ]

    res_data = json.dumps(
        {
            "items": items,
            "winHeight": 293,
            "winWidth": 513,
            "picPadding": 21,
        }
    )

    if request.method == "POST":
        return HttpResponse(res_data)
    raise RuntimeError("/get_slider_json does not support GET method")


def indexData(request, page):
    jsondata = """
{
    "total": 20,
    "result": [
        {
            "image": "http://wlog.cn/demo/waterfall/images/001.jpg",
            "width": 192,
            "height": 288
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/002.jpg",
            "width": 192,
            "height": 257
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/003.jpg",
            "width": 192,
            "height": 288
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/004.jpg",
            "width": 192,
            "height": 288
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/005.jpg",
            "width": 192,
            "height": 248
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/006.jpg",
            "width": 192,
            "height": 288
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/007.jpg",
            "width": 192,
            "height": 288
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/008.jpg",
            "width": 192,
            "height": 290
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/009.jpg",
            "width": 192,
            "height": 240
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/010.jpg",
            "width": 192,
            "height": 228
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/011.jpg",
            "width": 192,
            "height": 128
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/012.jpg",
            "width": 192,
            "height": 128
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/013.jpg",
            "width": 192,
            "height": 128
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/014.jpg",
            "width": 192,
            "height": 128
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/015.jpg",
            "width": 192,
            "height": 256
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/016.jpg",
            "width": 192,
            "height": 256
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/017.jpg",
            "width": 192,
            "height": 287
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/018.jpg",
            "width": 192,
            "height": 288
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/019.jpg",
            "width": 192,
            "height": 192
        },
        {
            "image": "http://wlog.cn/demo/waterfall/images/020.jpg",
            "width": 192,
            "height": 288
        }
    ]
}
"""
    return HttpResponse(content=jsondata, content_type='application/json')
