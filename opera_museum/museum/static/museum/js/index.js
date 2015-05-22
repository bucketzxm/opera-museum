$('#waterfall-container').waterfall({
    itemCls: 'waterfall-item',
    colWidth: 222,  
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    path: function(page) {
        return 'rest/v1/index/indexImages/' + page;
    }
});

var slider = new Slider({
    /*
    items: [
        '<div><img src="/static/museum/slider/img/data/1.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/2.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/3.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/4.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/5.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/6.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/7.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/8.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/9.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/10.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/11.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/12.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/13.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/14.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/15.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/16.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/17.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/18.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/19.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/20.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/21.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/22.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/23.jpg"/ class="sliderImage"></div>',
        '<div><img src="/static/museum/slider/img/data/24.jpg"/ class="sliderImage"></div>',
    ],
    winWidth: 645,
    winHeight: 430,
    */
});

