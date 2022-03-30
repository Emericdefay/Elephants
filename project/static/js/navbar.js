$(function () {
  // debug, re-able to click on links several times
  $(".nav-item").on('click custom', function (event) {
    event.preventDefault();
    const base = $(this).children().attr('aria-controls');
    $('.nav-item').each(function () {
      if (!$(this).children().attr('type')) {
        $(this).removeClass('d-none');
      }
    });
    $('.tab-pane').each(function () {
      if ($(this).attr('id') != base) {
        $(this).addClass('d-none');
      } else {
        $(this).removeClass('d-none');
        $(".save-position").each(function () {
          this.href = `${this.href.split('?tab=#')[0]}?tab=#${base}-tab`;
          window.history.pushState('page2', 'Title', `?tab=#${base}-tab`);
        })
      }
    })
  });
})

$(window).on('load', function () {
  try {
    const link = window.location.href.split('?tab=#')[1];
    const button = document.getElementById(link);
    $(link).click();
    $(link).trigger("click");
    $(button).trigger("click");
    $(button).trigger("custom");
    const base = $(`#${button.id}`).attr('aria-controls');
    $('.nav-item').each(function () {
      if (!$(this).children().attr('type')) {
        $(this).removeClass('d-none');
        $('.tab-pane').each(function () {
          if ($(this).attr('id') != base) {
            $(this).addClass('d-none');
          } else {
            $(this).removeClass('d-none');
            $(".save-position").each(function () {
              this.href = `${this.href.split('?tab=#')[0]}?tab=#${base}-tab`;
            })
          }
        })
      }
    }) 
  } catch (error) {
    window.open("http://127.0.0.1:8000/?tab=#client-tab","_self")
  }

  
})