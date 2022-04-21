$(function() {
    $('#resizable').on('mouseup mouseleave mouseover', function () {
        $('.follow-resizing').each(function () {
            $(this).css("width",($('#resizable').width()));
        })
    });    
})
