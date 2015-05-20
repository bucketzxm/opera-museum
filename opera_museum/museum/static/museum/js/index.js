$('#waterfall-container').waterfall({
    itemCls: 'waterfall-item',
    colWidth: 222,  
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    path: function(page) {
        return 'rest/v1/index/indexImages/' + page;
        //return 'http://wlog.cn/demo/waterfall/data/data1.json?page=1';
    }
});