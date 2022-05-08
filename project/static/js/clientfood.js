const lastName = () => {
  const url = "http://127.0.0.1:8000/api/client"
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
};

const firstName = () => {
  // INPUT FIRST NAME
  //setup before functions
  const url = "http://127.0.0.1:8000/api/client"
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
};

const address = () => {
  // INPUT ADDRESS
  //setup before functions
  const url = "http://127.0.0.1:8000/api/client"
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
};

const postCode = () => {
  // INPUT POSTCODE
  //setup before functions
  const url = "http://127.0.0.1:8000/api/client"
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
};

const addressDetails = () => {
  // INPUT ADDRESS DETAILS
  //setup before functions
  const url = "http://127.0.0.1:8000/api/client"
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
};

const cellphone = () => {
  // INPUT CELLPHONE
  //setup before functions
  const url = "http://127.0.0.1:8000/api/client"
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
};

const cellphone2 = () => {
  // INPUT CELLPHONE2
  //setup before functions
  const url = "http://127.0.0.1:8000/api/client"
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
};

const clientFood = () => {
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
};

const clientCircuit = () => {
  const url = "http://127.0.0.1:8000/api/clientcircuit"
  $('.circuit-selected').change(function () {
    const circuit = $(this)[0].selectedOptions[0].attributes[1].nodeValue;
    const client = $(this)[0].selectedOptions[0].attributes[0].nodeValue;
    urlFood = `${url}/${client}/${circuit}/`;
    $.ajax({
      url: urlFood,
      type: 'GET',
      dataType: 'json',
      beforeSend: () => {
      },
      success: data => {
        console.log(data)
        // $(`#price_unit__${client}`).html(data.price);
        $(`#tr_client_${client}`).css('background-color', data.circuit_color);
        $(`#tr_planning_${client}`).css('background-color', data.circuit_color);
      },
      error: (e) => {
        console.log(e)
      },
    });
  });
};

const exportBill = () => {
  const url = "http://127.0.0.1:8000/unit_facture"
  $('.export-unit-btn').on('click', function () {
    const client = $(this).data('client');
    const month = $(`#month_unit__${client}`).val();
    const year = $(`#year_unit__${client}`).val();
    const data = {
      'month_unit': month,
      'year_unit': year,
      'client_unit_bill': client,
    }

    $.ajax({
      url: url,
      type: 'POST',
      data: data,
      dataType: 'json',
      beforeSend: () => {
      },
      success: data => {

      },
      error: (e) => {
        toastr.options = {
          "closeButton": false,
          "debug": false,
          "newestOnTop": false,
          "progressBar": false,
          "positionClass": "toast-bottom-right",
          "preventDuplicates": false,
          "onclick": null,
          "showDuration": "300",
          "hideDuration": "1000",
          "timeOut": "5000",
          "extendedTimeOut": "1000",
          "showEasing": "swing",
          "hideEasing": "linear",
          "showMethod": "fadeIn",
          "hideMethod": "fadeOut"
        }
        if (e.responseText == 'error') {
          toastr.warning("Il n'y a pas de commandes pour ce client à cette période. 😅 Un fichier vierge a été créé.", "Zut");
        } else {
          toastr.success("Le détail pour ce client est téléchargé! 😊", "Et voilà!");
        }
      },
    });
  });
};

// Initialize
lastName();
firstName();
address();
addressDetails();
postCode();
cellphone();
cellphone2();
clientFood();
clientCircuit();
exportBill();
