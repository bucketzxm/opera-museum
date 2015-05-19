$('#waterfall-container').waterfall({
    itemCls: 'waterfall-item',
    colWidth: 222,  
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    path: function(page) {
        return 'data/data1.json?page=' + page;
    }
});
