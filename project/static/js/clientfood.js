$(() => {
    const url = "http://127.0.0.1:8000/api/clientfood"
    $('.checkbox-default-food').on('click', function () {
        const client = $(this).data('client');
        const food = $(this).data('food');
        const checked = this.checked ? 1 : 0;
        urlFood = `${url}/${client}/${food}/${checked}/`;
        $.ajax({
            url: urlFood,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {
              console.log(data)
              $(`#price_unit__${client}`).html(data.price);
            },
            error: (e) => {
              console.log(e)
            },
        });
    });
});

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
        const client = $(this).data('client');
        const command = $(this).data('command');
        urlFood = `${url}/?id=${client}`;
        $.ajax({
            url: urlFood,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {
              $(`#food-client-${command}`).html(data.results[0].html)
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
                console.log(data);
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

const url = "http://127.0.0.1:8000/api/client"
$(() => {
  // INPUT CELLPHONE2
  //setup before functions
  let typingTimer;                //timer identifier
  const doneTypingInterval = 2000;  //time in ms, 5 seconds for example
  let input;
  
  //on keyup, start the countdown
  $('.input_cellphone2').on('keyup focusout', function () {
    clearTimeout(typingTimer);
    input = $(this);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });
  
  //on keydown, clear the countdown 
  $('.input_cellphone2').on('keydown', function () {
    clearTimeout(typingTimer);
  });
  
  //user is "finished typing," do something
  function doneTyping () {
      //do something
      const client = input.data('client');
      const val = input.val();
      urlClient = `${url}/${client}/cellphone2/${val}/`;
      $.ajax({
          url: urlClient,
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
  }
});

$(() => {
  // INPUT ADDRESS DETAILS
  //setup before functions
  let typingTimer;                //timer identifier
  const doneTypingInterval = 2000;  //time in ms, 5 seconds for example
  let input;
  
  //on keyup, start the countdown
  $('.input_address_details').on('keyup focusout', function () {
    clearTimeout(typingTimer);
    input = $(this);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });
  
  //on keydown, clear the countdown 
  $('.input_address_details').on('keydown', function () {
    clearTimeout(typingTimer);
  });
  
  //user is "finished typing," do something
  function doneTyping () {
      //do something
      const client = input.data('client');
      const val = input.val();
      urlClient = `${url}/${client}/address_details/${val}/`;
      $.ajax({
          url: urlClient,
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
  }
});

$(() => {
  // INPUT CELLPHONE
  //setup before functions
  let typingTimer;                //timer identifier
  const doneTypingInterval = 2000;  //time in ms, 5 seconds for example
  let input;
  
  //on keyup, start the countdown
  $('.input_cellphone').on('keyup focusout', function () {
    clearTimeout(typingTimer);
    input = $(this);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });
  
  //on keydown, clear the countdown 
  $('.input_cellphone').on('keydown', function () {
    clearTimeout(typingTimer);
  });
  
  //user is "finished typing," do something
  function doneTyping () {
      //do something
      const client = input.data('client');
      const val = input.val();
      urlClient = `${url}/${client}/cellphone/${val}/`;
      $.ajax({
          url: urlClient,
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
  }
});

$(() => {
  // INPUT POSTCODE
  //setup before functions
  let typingTimer;                //timer identifier
  const doneTypingInterval = 2000;  //time in ms, 5 seconds for example
  let input;
  
  //on keyup, start the countdown
  $('.input_postcode').on('keyup focusout', function () {
    clearTimeout(typingTimer);
    input = $(this);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });
  
  //on keydown, clear the countdown 
  $('.input_postcode').on('keydown', function () {
    clearTimeout(typingTimer);
  });
  
  //user is "finished typing," do something
  function doneTyping () {
      //do something
      const client = input.data('client');
      const val = input.val();
      urlClient = `${url}/${client}/postcode/${val}/`;
      $.ajax({
          url: urlClient,
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
  }
});

$(() => {
  // INPUT ADDRESS
  //setup before functions
  let typingTimer;                //timer identifier
  const doneTypingInterval = 2000;  //time in ms, 5 seconds for example
  let input;
  
  //on keyup, start the countdown
  $('.input_address').on('keyup focusout', function () {
    clearTimeout(typingTimer);
    input = $(this);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });
  
  //on keydown, clear the countdown 
  $('.input_address').on('keydown', function () {
    clearTimeout(typingTimer);
  });
  
  //user is "finished typing," do something
  function doneTyping () {
      //do something
      const client = input.data('client');
      const val = input.val();
      urlClient = `${url}/${client}/address/${val}/`;
      $.ajax({
          url: urlClient,
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
  }
});

$(() => {
  // INPUT FIRST NAME
  //setup before functions
  let typingTimer;                //timer identifier
  const doneTypingInterval = 2000;  //time in ms, 5 seconds for example
  let input;
  
  //on keyup, start the countdown
  $('.input_first_name').on('keyup focusout', function () {
    clearTimeout(typingTimer);
    input = $(this);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });
  
  //on keydown, clear the countdown 
  $('.input_first_name').on('keydown', function () {
    clearTimeout(typingTimer);
  });
  
  //user is "finished typing," do something
  function doneTyping () {
      //do something
      const client = input.data('client');
      const val = input.val();
      urlClient = `${url}/${client}/first_name/${val}/`;
      $.ajax({
          url: urlClient,
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
  }
});

$(() => {
    // INPUT LAST NAME
    //setup before functions
    let typingTimer;                //timer identifier
    const doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    let input;
    
    //on keyup, start the countdown
    $('.input_last_name').on('keyup focusout', function () {
      clearTimeout(typingTimer);
      input = $(this);
      typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $('.input_last_name').on('keydown', function () {
      clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
        //do something
        const client = input.data('client');
        const val = input.val();
        urlClient = `${url}/${client}/last_name/${val}/`;
        $.ajax({
            url: urlClient,
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
    }
});