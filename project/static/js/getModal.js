// show the modal for single ads
function openClientModal () {
    // show modal
    $('#add-modal').modal('show');
  }
  
  // close the modal for single ads
  function hideClientModal () {
    // hide modal
    $('#add-modal').modal('hide').on('shown.bs.modal', () => {
      $('#add-modal').modal('show');
    });
  }

// show the modal for single ads
function openAdModal () {
    // show modal
    $('#feedme').empty();
    $('#feedmeTotal').empty();
    $('#unique-modal').modal('show');
  }
  
  // close the modal for single ads
  function hideAdModal () {
    // hide modal
    $('#unique-modal').modal('hide').on('shown.bs.modal', () => {
      $('#unique-modal').modal('show');
      $('#feedme').empty();
      $('#feedmeTotal').empty();
    });
  }

// show the modal for single ads
function openAdTotalModal () {
    // show modal
    $('#feedme').empty();
    $('#feedmeTotal').empty();
    $('#unique-modal-total').modal('show');
  }
  
  // close the modal for single ads
  function hideAdTotalModal () {
    // hide modal
    $('#unique-modal-total').modal('hide').on('shown.bs.modal', () => {
      $('#unique-modal-total').modal('show');
      $('#feedme').empty();
      $('#feedmeTotal').empty();
    });
  }

// show the modal for comments
function openCommentModal () {
    // show modal
    $('#feedmecomment').empty();
    $('#unique-modal-customer').modal('show');
  }
  
  // close the modal for comments
  function hideCommentModal () {
    // hide modal
    $('#unique-modal-total').modal('hide').on('shown.bs.modal', () => {
      $('#unique-modal-customer').modal('show');
      $('#feedmecomment').empty();
    });
  }

function openFoodModal () {
    // show modal
    $('#food-modal').modal('show');
  }
  
  // close the modal for single ads
  function hideFoodModal () {
    // hide modal
    $('#food-modal').modal('hide').on('shown.bs.modal', () => {
      $('#food-modal').modal('show');
    });
  }
  
  // get variables from the data collected with ajax
  function getHtml (data) {
    // If you want to add more variables, exploit this block
    // const vars = {
    //   html: data.html,
    // };
    return data;
  }
  
  
  function openCircuitModal () {
    // show modal
    $('#circuit-modal').modal('show');
  }

  // close the modal for single ads
  function hideCircuitModal () {
    // hide modal
    $('#circuit-modal').modal('hide').on('shown.bs.modal', () => {
      $('#circuit-modal').modal('show');
    });
  }


  
  // get the id of the ad clicked
  // getting data from api
  // prepare the modal for it
  $(() => {
    $('.unique-add-btn').on('click', function () {
      openClientModal();
    });
    $('.circuit-add-btn').on('click', function () {
      openCircuitModal();
    });
    $('.food-add-btn').on('click', function () {
      openFoodModal();
    });
    $('.unique-circuit-btn').on('click', function () {
      const circuit = $(this).data('circuit');
      const day = $(this).data('day');
      const month = $(this).data('month');
      const year = $(this).data('year');
      const url = 'http://127.0.0.1:8000/api';
      let urlAd = `${url}/?day_date_command=${day}&month_date_command=${month}&year_date_command=${year}&circuit=${circuit}`;
      openAdModal();
      $.ajax({
        url: urlAd,
        type: 'GET',
        dataType: 'json',
        beforeSend: () => {
        },
        success: data => {
          $('#titleCircuit').text(data.results[0].title);
          data.results.forEach(function (row) {
            $('#feedme').append(row.html);
          })      
          urlAd = `${url}/total/?day_date_command=${day}&month_date_command=${month}&year_date_command=${year}&circuit=${circuit}`;
          $.ajax({
            url: urlAd,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {
                $('#feedme').append(data.results[0].html);
              
            },
            error: (e) => {
              const html = getHtml(e.responseText);
              console.log(e)
            },
          });
        },
        error: (e) => {
          const html = getHtml(e.responseText);
          console.log(e)
        },
  
    });
    

  });

    $('.total-circuit-btn').on('click', function () {
      const circuit = $(this).data('circuit');
      const day = $(this).data('day');
      const month = $(this).data('month');
      const year = $(this).data('year');
      const url = 'http://127.0.0.1:8000/api';
      let urlAd = `${url}/circuit-total/?day_date_command=${day}&month_date_command=${month}&year_date_command=${year}&circuit=${circuit}`;
      openAdTotalModal();
      let arrayIds = new Set();
      $.ajax({
        url: urlAd,
        type: 'GET',
        dataType: 'json',
        beforeSend: () => {
        },
        success: data => {
          $('#titleCircuitTotal').text(data.results[0].title);
          data.results.forEach(function (row) {
            $('#feedmeTotal').append(row.html);
            arrayIds.add(row.id);
          })

          $('[id]').each(function () {
            $('[id="' + this.id + '"]:gt(0)').remove();
          })
        },
        error: (e) => {
          const html = getHtml(e.responseText);
          console.log(e)
        },
    });
  });

    $('.customer-comment-btn').on('click', function () {
      const client = $(this).data('client');
      const url = 'http://127.0.0.1:8000/api';
      let urlAd = `${url}/comments/?client_id=${client}`;
      openCommentModal();
      $.ajax({
        url: urlAd,
        type: 'GET',
        dataType: 'json',
        beforeSend: () => {
        },
        success: data => {
          $('#titleCustomerCommentName').text(data.results[0].client_name);
          data.results.forEach(function (row) {
            $('#feedmecomment').append(row.html);
          })
          $('.delete-comment').on('click', function () {
            command = $(this).data('command');
            const url = 'http://127.0.0.1:8000/api';
            let urlAd = `${url}/comment-delete/${command}/`;
            $.ajax({
              url: urlAd,
              type: 'PUT',
              dataType: 'json',
              beforeSend: () => {
              },
              success: data => {
                $(`.row-${command}`).css( "background-color", "darkgray" );
              },
              error: (e) => {
                $(`.row-${command}`).css( "background-color", "darkgray" );
              },
            });
          });
        },
        error: (e) => {
          console.log(e)
        },
    });
  });
});