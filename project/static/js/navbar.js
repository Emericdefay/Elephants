$(function () {
  $("#date_link").val(window.location.href.split('?tab=#')[0].split('8000')[1]);
  // debug, re-able to click on links several times
  $(".nav-item").on('click custom', async function (event) {
    event.preventDefault();
    console.log(window.location.href.split('?tab=#')[0].split('8000')[1]);
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
        $("#calendarBtn").children().each(async function () {
          this.href = `${this.href.split('?tab=#')[0]}?tab=#${base}-tab`;
        })
        $("#save_link").val(`?tab=#${base}-tab`);
        window.history.pushState('page2', 'Title', `?tab=#${base}-tab`);
      }
    })
  });
})

$(window).on('load',async function () {
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
        $(this).children().removeClass('active');
        $(this).removeClass('d-none');
        $('.tab-pane').each(function () {
          if ($(this).attr('id') != base) {
            $(this).addClass('d-none');
          } else {
            $(this).removeClass('d-none');
            $(this).addClass('active');
            $(this).addClass('show');
            $("#calendarBtn").children().each(async function () {
              this.href = `${this.href.split('?tab=#')[0]}?tab=#${base}-tab`;
            })
            $("#save_link").val(`?tab=#${base}-tab`);
          }
        })
      }
    $(`#${base}-tab`).addClass('active');  
    }) 
  } catch (error) {
    console.log(error);
    window.open("http://127.0.0.1:8000/?tab=#client-tab","_self");
  }

  
})