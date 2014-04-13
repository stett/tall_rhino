$(function() {
    //$(".load img").attr("src", "/static/img/load.png");

    $(".imageset .buffer").load(function() {
        var $buffer = $(this);
        var src = $buffer.attr('src');
        var width = $buffer.width() - 2;
        var height = $buffer.height() - 2;
        var $parent = $buffer.parent();
        var $loader = $parent.find(".load");
        var $image = $parent.find(".image");
        var $img = $image.find('img');
        $loader.fadeOut(200);
        $image.animate({
            'width': width,
            'height': height,
        }, 300, function() {
            $img.width(width);
            $img.height(height);
            $img.attr("src", src);
            $img.animate({ 'opacity': 1 }, 200);
        });
    });

    $(".imageset .thumbs .thumb").click(function() {
        var $thumb = $(this);
        if ($thumb.hasClass("active")) return;
        var src = $thumb.attr("href");
        var $parent = $thumb.closest('.imageset');
        var $loader = $parent.find(".load");
        var $buffer = $parent.find(".buffer");
        var $img = $parent.find(".image img");
        $parent.find('.thumb').removeClass('active');
        $thumb.addClass('active');
        $loader.fadeIn(200);
        $img.animate({ 'opacity': 0}, 200, function() {
            $buffer.attr("src", src);
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
