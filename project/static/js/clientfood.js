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
    const url = "http://127.0.0.1:8000/api/command"
    $('.command-btn').on('click', function () {
        const command = $(this).data('command');
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
    });
});

const url = "http://127.0.0.1:8000/api/client"
$(() => {
    // CELLPHONE2
    //setup before functions
    var typingTimer;                //timer identifier
    var doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    var $input = $('.input_cellphone2');
    
    //on keyup, start the countdown
    $input.on('keyup focusout', function () {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $input.on('keydown', function () {
        clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
        //do something
        const client = $input.data('client');
        const val = $input.val();
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
    var typingTimer;                //timer identifier
    var doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    var $input = $('.input_address_details');
    
    //on keyup, start the countdown
    $input.on('keyup focusout', function () {
      clearTimeout(typingTimer);
      typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $input.on('keydown', function () {
      clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
      //do something
    }
});

$(() => {
    // INPUT CELLPHONE
    //setup before functions
    var typingTimer;                //timer identifier
    var doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    var $input = $('.input_cellphone');
    
    //on keyup, start the countdown
    $input.on('keyup focusout', function () {
      clearTimeout(typingTimer);
      typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $input.on('keydown', function () {
      clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
        //do something
        const client = $input.data('client');
        const val = $input.val();
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
    var typingTimer;                //timer identifier
    var doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    var $input = $('.input_postcode');
    
    //on keyup, start the countdown
    $input.on('keyup focusout', function () {
      clearTimeout(typingTimer);
      typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $input.on('keydown', function () {
      clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
        //do something
        const client = $input.data('client');
        const val = $input.val();
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
    var typingTimer;                //timer identifier
    var doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    var $input = $('.input_address');
    
    //on keyup, start the countdown
    $input.on('keyup focusout', function () {
      clearTimeout(typingTimer);
      typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $input.on('keydown', function () {
      clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
        //do something
        const client = $input.data('client');
        const val = $input.val();
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
    var typingTimer;                //timer identifier
    var doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    var $input = $('.input_first_name');
    
    //on keyup, start the countdown
    $input.on('keyup focusout', function () {
      clearTimeout(typingTimer);
      typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $input.on('keydown', function () {
      clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
        //do something
        const client = $input.data('client');
        const val = $input.val();
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
    var typingTimer;                //timer identifier
    var doneTypingInterval = 2000;  //time in ms, 5 seconds for example
    var $input = $('.input_last_name');
    
    //on keyup, start the countdown
    $input.on('keyup focusout', function () {
      clearTimeout(typingTimer);
      typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    
    //on keydown, clear the countdown 
    $input.on('keydown', function () {
      clearTimeout(typingTimer);
    });
    
    //user is "finished typing," do something
    function doneTyping () {
        //do something
        const client = $input.data('client');
        const val = $input.val();
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