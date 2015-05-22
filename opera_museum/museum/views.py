# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render, render_to_response, HttpResponse, redirect, RequestContext
from models import Entry, Tag

from django.template import loader
import json
from PIL import Image


'''
    index ---> 首页

    get_image_size( Image img) ----> 获取图片大小(x,y)

    entry_detail ----> 获得详细页面 detail.html

    entry_category ----> 获取某个目录下的词条

    get_entry_json ----> 获取词条json 信息返回

'''


def index(request):
    return render_to_response("index.html")


def get_image_size(image):
    '''
    get image size
    :return: tuple of ( height,weight)
    '''
    # get Image path
    path = image.image_url.path
    im = Image.open(path)
    return im.size


# look up detail for appointed entry
def entry_detail(request):
    if request.method == 'GET':
        query_name = request.GET['name']
        entries = Entry.objects.all().fileter(name=query_name)

        if not entries:
            return render_to_response("404.html")
        else:
            # add entry watched
            if len(entries) > 1:
                #TODO If more than 1 entries , try to redirect to another page
                return HttpResponse("")
            else:
                entry = entries.first()
                if entry.watched <= 1000:
                    entry.watched += 1
                return render_to_response("entry_detail.html")

    return render_to_response("")


# support the entry
def support_entry(request):
    if request.method == 'POST':
        entry_id = request.POST['entryId']
        entry = Entry.objects.all().filter(id=entry_id)[0]


        if entry.support<1000:
            entry.support += 1

    return HttpResponse("")


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


def get_entry_json(tag):
    '''
    get entry_json data filter by tag for waterfall
    :param tag:
    :return:
    '''

    entries = Entry.objects.all().filter(tags=tag)
    print(entries)

    # return json format data to waterfall
    total = len(entries)

    entry_list = [
        {
            # TODO dirty code here
            "image": entry.images.all().first().image_url.url,  # pay attention to last .url
            "width": get_image_size( entry.images.all().first())[0],
            "height": get_image_size( entry.images.all().first())[1],
        }

        for entry in entries if entry.images.all().first()
    ]
    json_data = json.dumps(
        {
            "total": total,
            "result": json.dumps(entry_list),
        }
    )
    return json_data


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