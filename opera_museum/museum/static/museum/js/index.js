// using jQuery
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


$('#waterfall-container').waterfall({
    itemCls: 'waterfall-item',
    colWidth: 222,
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    path: function (page) {
        return 'rest/v1/index/indexImages/' + page;
    }
});

var slider = $(function () {
    var slider = null;
    $.ajax({
        type: 'post',
        url: 'get_slider_json',

        success: function (data) {
            slider = new Slider(data);
            console.log(data);
        }
    });
    return slider
});


