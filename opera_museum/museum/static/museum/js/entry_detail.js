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

$('#waterfall-container').waterfall({
    itemCls: 'waterfall-item',
    colWidth: 200,
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    maxCol: 1,
    path: function (page,id) {
        //return 'get_entry_json/?page=' + page + "&tag_key=root&tag_value=root";
        //return 'rest/v1/index/indexImages/'+ page ;
        return 'get_entry_detail_json/?id='+ id ;
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