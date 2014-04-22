$(function() {

    $(".imageset .buffer").load(function() {
        var $buffer = $(this);
        var src = $buffer.attr('src');
        var width = $buffer.width() - 2;
        var height = $buffer.height() - 2;
        var $parent = $buffer.parent();
        var $loader = $parent.find(".load");
        var $image = $parent.find(".image");
        var $img = $image.find('img');
        var $description = $parent.find(".description");
        $loader.fadeOut(100);
        $image.addClass("enabled");
        $image.animate({
            'width': width,
            'height': height,
        }, 200, function() {
            $img.width(width);
            $img.height(height);
            $img.attr("src", src);
            $img.animate({ 'opacity': 1 }, 200, function() {
                if ($description.text()) $description.fadeIn(200);
            });
            $loader.css({ 'margin-top': (height - $loader.height()) / 2});
        });
    });

    $(".imageset .thumbs .thumb").click(function() {
        var $thumb = $(this);
        if ($thumb.hasClass("active")) return;
        var src = $thumb.attr("href");
        var description = $thumb.data("description");
        var $parent = $thumb.closest('.imageset');
        var $image = $parent.find(".image");
        var $loader = $parent.find(".load");
        var $buffer = $parent.find(".buffer");
        var $img = $parent.find(".image img");
        var $description = $parent.find(".description");
        $parent.find('.thumb').removeClass('active');
        $thumb.addClass('active');
        $loader.fadeIn(100);
        $image.removeClass("enabled");
        $description.fadeOut(200, function() {
            $description.text(description);
        });
        $img.animate({ 'opacity': 0}, 200, function() {
            $buffer.attr("src", src);
        });
    });

    $(".imageset .image").click(function() {
        if (!$(this).hasClass("enabled")) return;
        var $image = $(this);
        var $parent = $image.closest(".imageset");
        var $fullscreen = $parent.find(".fullscreen");
        var $img = $fullscreen.find("img");
        var src = $image.find("img").attr("src");
        $fullscreen.fadeIn(200);
        $img.css({ "opacity": 0 });
        $img.attr("src", src).load(function() {
            $(this).unbind("load");
            console.log($(window).height());
            console.log($img.height());
            $img.css({"margin-top": String(($(window).height() - $img.height()) / 2) + "px"});
            $img.animate({ "opacity": 1 }, 200);
        });
    });

    $(".imageset .fullscreen").click(function() {
        var $fullscreen = $(this);
        $fullscreen.fadeOut(100, function() {
            $fullscreen.find("img").attr("src", "");
        });
    });

    $(".imageset").resize(function() {
        console.log("RESIZE");
    });

    $(".imageset").each(function(i) {
        var $thumb = $(this).find(".thumb").last();
        $thumb.click();
    });
});
