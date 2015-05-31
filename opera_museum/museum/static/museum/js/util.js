function Waterfall_addSizeRestraintToImage($html, restraintWidth) {
    var retHTML = '';
    $html.each(function (i, node) {
        if (node.nodeName != 'DIV')
            return;

        var $node = $(node);
        var $img = $node.find('img');
        $node.css('width', restraintWidth);
        $img.css('max-width', restraintWidth);
        $img.css('height', 'auto');

        retHTML += $node.get(0).outerHTML + '\n';
    });
    return retHTML;
}


function like_entry(id) {
    alert("okok");
    var like = document.getElementById("like");
    var obj = like.next;
    //var entryId = this.parents('div').attr("entryId");
    var myData = "entryId=" + id;

    $.ajax({
        type: "post",
        url: "/like_entry",
        dataType: "text",
        data: myData,
        success: function (result) {
            var num = parseInt(obj.text());
            obj.test(num + 1);
            console.log(num + 1);
        }

    });

    var num = parseInt(obj.text());
    obj.text(num + 1);


}