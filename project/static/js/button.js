$('.btn-plus, .btn-minus').on('click', function(e) {
    const isNegative = $(e.target).closest('.btn-minus').is('.btn-minus');
    const input = $(e.target).closest('.btn-group').find('input');
    const label = $(e.target).closest('.btn-group').find('label');
    if (input.is('input')) {
      input[0][isNegative ? 'stepDown' : 'stepUp']();
      $(label).children(":first").text(input[0].value);
    }
  })