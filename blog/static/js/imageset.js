$(function() {
    var accent = '#69f';

    $('.imageset .image').css({
        'position': 'relative',
        'margin': '0 auto',
        'display': 'block',
        'min-width': '128px',
        'min-height': '128px',
        'border': '1px solid ' + accent,
    });

    function recenter($centerable) {
        console.log($centerable);
        var $container = $centerable.parent();
        $centerable.css({
            'display': 'block',
            'position': 'absolute',
            'margin': '0',
        });
        var left = ($container.width() - $centerable.width()) / 2;
        var top = ($container.height() - $centerable.height()) / 2;
        $centerable.css({
            'left': String(left) + 'px',
            'top': String(top) + 'px',
        });
    };

    $('.center').each(function() {
        recenter($(this));
        console.log($(this).parent());
        $(this).parent().resize(function() {
            console.log("RECENTER");
            recenter($(this))
        });
    });
});
