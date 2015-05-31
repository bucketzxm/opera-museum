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
                    entry.save()

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
                                              , 'like': entry.like
                                              , 'watched': entry.watched})
    return render_to_response("")

# support the entry
@csrf_exempt
def like_entry(request):
    if request.method == 'POST':
        entry_id = request.POST['entryId']
        entry = Entry.objects.all().filter(id=entry_id)[0]

        if entry.like < 1000:
            entry.like += 1
            entry.save()
    return HttpResponse(str(entry.like))

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
    entry_list = [
        {
            "entry_id": entry.id,
            "image": entry.image_set.all().first().image_url.url,  # pay attention to last .url
            "like": entry.like,
            "watched": entry.watched
        }
        for entry in entries if entry.image_set.all().first()
    ]
    length = len(entry_list)
    start = (int(page)-1)*10
    end = (start + 10) if (start + 10) <= length else length

    entry_list = entry_list[start:end]
    
    json_data = json.dumps({
        "result_length": end - start,
        "result": entry_list,
    })
    return HttpResponse(content=json_data, content_type='application/json')


def get_slider_json(request):
    entry_list = Entry.objects.all().filter(slider_show=True)

    def generate_div_img(image):
        imageSize = image.getImageSize()
        if imageSize[0] > imageSize[1]:
            ret = '<div style="text-align: center;"><img src="' + image.image_url.url + '" style="max-width: 513px; height: auto;"/></div>'
        else:
            ret = '<div style="text-align: center;"><img src="' + image.image_url.url + '" style="max-height: 293px; width: auto"/></div>'
        return ret

    items = [ generate_div_img(entry.image_set.all()[0]) for entry in entry_list ]

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
