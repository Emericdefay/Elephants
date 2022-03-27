$(function () {
    // debug, re-able to click on links several times
    $(".nav-item").on('click', function (event) {
      event.preventDefault();
      const base = $(this).children().attr('aria-controls');
      $('.nav-item').each(function () {
        if (!$(this).children().attr('type')) {
          $(this).removeClass('d-none');
          $('.tab-pane').each(function () {
            if ($(this).attr('id') != base) {
              $(this).addClass('d-none');
            }else{
              $(this).removeClass('d-none');
            }
          })
        }
      });
    });
})