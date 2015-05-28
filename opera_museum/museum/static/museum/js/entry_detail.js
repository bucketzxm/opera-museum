/**
 *
 * Created by simon on 5/27/15.
 */


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

function getUrlParams(TheName) {
    var url = window.location.href.split("?");
    var gets = url[1].split("&");
    for (var i = 0; i < gets.length; i++) {
        var get = gets[i].split("=");
        if (get[0] == TheName) {
            var TheValue = get[1];
            break;
        }
    }
    return TheValue;
}


$('#waterfall-container').waterfall({
    itemCls: 'waterfall-item',
    colWidth: 995,
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    maxCol: 1,
    maxPage:1,
    dataType: "html",
    params: {
        "id": getUrlParams("id"),
        "page": 1
    },
    path: function () {
        return "/get_entry_detail_json/"
    },
    callbacks: {
        renderData: function (data, dataType) {
            var tpl,
                template;
            if (dataType === 'json' || dataType === 'jsonp') { // json或jsonp格式
                tpl = $('#waterfall-tpl').html();
                template = Handlebars.compile(tpl);

                return template(data);
            } else { // html格式
                return data;
            }
        }
    }
});



$('#waterfall-container_two').waterfall({
    itemCls: 'waterfall-item',
    colWidth: 250,
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    maxCol: 4,
    maxPage:undefined,
    dataType: "json",
    params: {
        "id": getUrlParams("id"),
        "page": 1
    },
    path: function (page) {
        return 'get_entry_json/?page='+page+"&tag_key=root&tag_value=root";
    },
    callbacks: {
        renderData: function (data, dataType) {
            var tpl,
                template;
            if (dataType === 'json' || dataType === 'jsonp') { // json或jsonp格式
                tpl = $('#waterfall-tpl').html();
                template = Handlebars.compile(tpl);

                return template(data);
            } else { // html格式
                return data;
            }
        }
    }
});


// magnifier
var evt = new Event(),
    m = new Magnifier(evt);

m.attach({
    thumb: '#thumb',
    large: 'http://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Starry_Night_Over_the_Rhone.jpg/400px-Starry_Night_Over_the_Rhone.jpg',
    largeWrapper: 'preview',
    mode: "inside",
    zoom: 1
});