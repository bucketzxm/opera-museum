from django.shortcuts import render, render_to_response, HttpResponse, redirect, RequestContext
from django.template import loader

def index(request):        
    # template = loader.get_template("index.html")
    # context = {"title": "Home"}
    # return render(request, template)
    return render_to_response("index.html")

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