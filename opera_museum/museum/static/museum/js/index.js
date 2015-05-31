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

var waterfallColumnWidth = 249;
$('#waterfall-container').waterfall({
    itemCls: 'waterfall-item',
    colWidth: waterfallColumnWidth,
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    maxCol: 4,
    page: 1,
    dataType: 'json',
    path: function (page) {
        return 'get_entry_json/?page=' + page + "&tag_key=root&tag_value=root";
        //return 'rest/v1/index/indexImages/'+ page ;
    },
    callbacks: {
        renderData: function (data, dataType) {
			if (dataType === 'json' ||  dataType === 'jsonp') {
				var tpl = $('#waterfall-tpl').html();
				var template = Handlebars.compile(tpl);
                var html = template(data);
                return Waterfall_addSizeRestraintToImage($(html), waterfallColumnWidth);
			} else { // html format
				return data;
			}
		}
    }
});

var slider = null;
$.ajax({
    type: 'post',
    url: 'get_slider_json',

    success: function (data) {
        var options = $.parseJSON(data);
        options["$container"] = $('#slider');
        slider = new Slider(options);
    }
});

