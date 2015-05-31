function like_entry(id) {
    $.ajax({
        type: "post",
        url: "/like_entry",
        dataType: "text",
        data: "entryId=" + id,
        success: function (result) {
            var $like = $('#museum_waterfall_entry_like_' + id);
            $like.html(parseInt(result).toString());
            console.log('id: ' + id + ' like: ' + result);
        }
    });
}
