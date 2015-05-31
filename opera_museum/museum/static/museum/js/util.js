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
