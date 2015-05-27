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
    colWidth: 200,
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    maxCol: 4,
    path: function (page) {
        return 'get_entry_json/?page='+page+"&tag_key=root&tag_value=root";
        //return 'rest/v1/index/indexImages/'+ page ;
    }
});

var slider = null;
$.ajax({
    type: 'post',
    url: 'get_slider_json',

    success: function (data) {
        console.log(data);
        var options = $.parseJSON(data);
        options["$container"] = $('#slider');
        slider = new Slider(options);
    }
});

