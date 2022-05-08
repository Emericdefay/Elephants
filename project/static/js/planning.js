
$(() => {
    const url = "http://127.0.0.1:8000/api/commandfood"
    $('.checkbox-food').on('click', function () {
        const command = $(this).data('command');
        $(`input[data-command="${command}"][type="checkbox"]`).each( function () {
            const food = $(this).data('food');
            const checked = this.checked ? '1' : '0';
            urlFood = `${url}/${command}/${food}/${checked}/`;
            $.ajax({
                url: urlFood,
                type: 'GET',
                dataType: 'json',
                beforeSend: () => {
                },
                success: data => {
    
                },
                error: (e) => {
                  console.log(e)
                },
            });
        })
    });
});

$(() => {
    const url = "http://127.0.0.1:8000/api/getclientfood"
    $('.dropdown-get-food').on('click', function () {
        // const client = $(this).data('client');
        const command = $(this).data('command');
        urlFood = `${url}/?id=${command}`;
        $.ajax({
            url: urlFood,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {
              $(`#food-client-${command}`).html(data.results[0].html)
              $(`#defaultfood-client-${command}`).html(data.results[0].html_food)
            },
            error: (e) => {
              console.log(e)
            },
        });
    });
});

$(() => {
    const url = "http://127.0.0.1:8000/api/commentupdate"
    $('.save-comment').on('click', function () {
        // const client = $(this).data('client');
        const command = $(this).data('command');
        const client = $(this).data('client');
        const value = $(`textarea[data-command="${command}"]`).val()
        urlFood = `${url}/${command}/${value}/`;
        $.ajax({
            url: urlFood,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {
              // add class comment to line
              $(`td.customer-comment-btn[data-client="${client}"]`).addClass('comment');
              $(`button[data-command="${command}"][data-bs-toggle="dropdown"]`).addClass('btn-danger');
            },
            error: (e) => {
              console.log(e)
            },
        });
    });
});

$(() => {
  $('.command-btn').on('click', function () {
        let url = "http://127.0.0.1:8000/api/command"
        const command = $(this).data('command');
        const client = $(this).data('client');
        const month = $(this).data('month');
        const year = $(this).data('year');
        const value = $(`input[data-id="command_command__${command}"]`).val();
        urlFood = `${url}/${command}/${value}/`;
        $.ajax({
            url: urlFood,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {

            },
            error: (e) => {
              console.log(e)
            },
        });
        
        url = "http://127.0.0.1:8000/api/commandfood"
        $(`input[data-client="${client}"][type="checkbox"]`).each( function () {
          const food = $(this).data('food');
          const checked = this.checked ? '1' : '0';
          urlFood = `${url}/${command}/${food}/${checked}/`;
          $.ajax({
              url: urlFood,
              type: 'GET',
              dataType: 'json',
              beforeSend: () => {
              },
              success: data => {

              },
              error: (e) => {
                console.log(e)
              },
          });
        })
        url = "http://127.0.0.1:8000/api/commandbymonth"
        urlFood = `${url}/${client}/${month}/${year}/`;
        $.ajax({
            url: urlFood,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {
              $(`#money_this_month__${client}`).text(data.money_this_month);
              $(`#meal_this_month__${client}`).text(data.meal_this_month);
            },
            error: (e) => {
              console.log(e)
            },
        });
    });
});

// Initialize
// commandFood();
// getClientFood();
// commentUpdate();
// command();