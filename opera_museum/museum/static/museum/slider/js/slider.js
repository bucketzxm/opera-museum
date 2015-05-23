var Slider = (function($) {
    'use strict';
    // statics
    var defaults = {
        $container: $('#slider'),
        items: [
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
            '<div><img src="/static/museum/img/test.png"/></div>',
        ],
        winHeight: 368,
        winWidth: 643,
        picPadding: 35
    };
    
    function slideLeft() {
        this.$slider.animate({"margin-left": "-=" + this.paddedWidth + "px" }, "slow");
    };
    
    // constructor
    function Slider(options) {
        // get the options
        this.options = $.extend(true, {}, defaults, options);
        
        // calculate padded width and heigth
        this.paddedWidth = this.options.winWidth + 2 * this.options.picPadding;
        this.paddedHeight= this.options.winHeight + 2 * this.options.picPadding;
        
        // slider background (real container)
        this.$container = $('<div class="sliderBackground"></div>')
        this.options.$container.append(this.$container);
        
        // construct navigators
        var $navDiv = $('<div></div>');
        this.$navPrev = this._constructNavigatorPrev();
        this.$navPrev.click({slider: this}, function(event) {
            event.data.slider.slideLeft();
        });
        this.$navNext = this._constructNavigatorNext();
        this.$navNext.click({slider: this}, function(event) {
            event.data.slider.slideRight();
        });
        $navDiv.append(this.$navPrev);
        $navDiv.append(this.$navNext);
        this.$container.append($navDiv);
        
        // construct slider
        this.$slider = this._constructSlider();
        this.$slider.css("width", this.paddedWidth * this.options.items.length);
        this.$slider.appendTo(this.$container);
        
        // add items
        for (var i = 0; i < this.options.items.length; ++i) {
            var item = this.options.items[i];
            this.append(item);
        }
    };
    
    Slider.prototype._constructSlider = function() {
        var $slider = $('<div class="slider"></div>');
        $slider.css("height", this.paddedHeight);
        return $slider;
    };
    
    Slider.prototype._constructNavigatorPrev = function() {
        var $nav = $('<span></span>');
        $nav.css("left", "30px");
        $nav.css("float", "left");
        $nav.css("background", "url(/static/museum/slider/img/nav_previous.png)");
        $nav.css("width", 64);
        $nav.css("height", 64);
        $nav.css("position", "absolute");
        $nav.css("top", "50%");
        return $nav;
    };
    
    Slider.prototype._constructNavigatorNext = function() {
        var $nav = $('<span></span>');
        $nav.css("right", "30px");
        $nav.css("float", "right");
        $nav.css("background", "url(/static/museum/slider/img/nav_next.png)");
        $nav.css("width", 64);
        $nav.css("height", 64);
        $nav.css("position", "absolute");
        $nav.css("top", "50%");
        return $nav;
    };
    
    Slider.prototype.append = function(item) {
        var $item = $(item);
        var $holder = $('<div class="sliderHolder"></div>');
        $holder.css("padding", this.options.picPadding);
        $holder.css("width", this.paddedWidth);
        $holder.css("height", this.paddedHeight);
        $holder.appendTo(this.$slider);
        $item.appendTo($holder);
    };
    
    Slider.prototype.slideLeft = function() {
        this.$slider.animate({"margin-left": "-=" + this.paddedWidth + "px" }, "slow");
    };
    
    Slider.prototype.slideRight = function() {
        this.$slider.animate({"margin-left": "+=" + this.paddedWidth + "px" }, "slow");
    };
    
    return Slider;
})(jQuery);
