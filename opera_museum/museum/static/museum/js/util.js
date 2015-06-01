function Waterfall_addSizeConstraintToImage($html, restraintWidth) {
    var retHTML = '';
    $html.each(function (i, node) {
        if (node.nodeName != 'DIV')
            return;

        var $node = $(node);
        var $img = $node.find('.museum_waterfall_entry_image');
        $node.css('width', restraintWidth);
        $img.css('max-width', restraintWidth-2);
        $img.css('height', 'auto');

        retHTML += $node.get(0).outerHTML + '\n';
    });
    return retHTML;
}
