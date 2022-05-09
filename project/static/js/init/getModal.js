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
      const day2 = $(this).data('daytwo') ?? day;
      const month = $(this).data('month');
      const month2 = $(this).data('monthtwo') ?? month;
      const year = $(this).data('year');
      const year2 = $(this).data('yeartwo') ?? year;
      const url = 'http://127.0.0.1:8000/api';
      let urlAd = `${url}/?search=${day}-${month}-${year}%2C${day2}-${month2}-${year2}&circuit=${circuit}`;
      openAdModal();
      $.ajax({
        url: urlAd,
        type: 'GET',
        dataType: 'json',
        beforeSend: () => {
        },
        success: data => {
          $('#titleCircuit').text(data.results[0].title);
          let arrayClients = new Set();
          data.results.forEach(function (row) {
            if (!arrayClients.has(row.id)) {
              $('#feedme').append(row.html);
              arrayClients.add(row.id);
            } else {
              row.food.forEach(function (food_id) {
                let value = Number($(`#food_${food_id[0]}_${row.id}`).text());
                value += food_id[1];
                $(`#food_${food_id[0]}_${row.id}`).text(value);
              })
            }
          });
          urlAd = `${url}/total/?search=${day}-${month}-${year}%2C${day2}-${month2}-${year2}&circuit=${circuit}`;
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
      const day2 = $(this).data('daytwo') ?? day;
      const month = $(this).data('month');
      const month2 = $(this).data('monthtwo') ?? month;
      const year = $(this).data('year');
      const year2 = $(this).data('yeartwo') ?? year;
      const url = 'http://127.0.0.1:8000/api';
      let urlAd = `${url}/circuit-total/?search=${day}-${month}-${year}%2C${day2}-${month2}-${year2}`;
      openAdTotalModal();
      let arrayIds = new Set();
      $.ajax({
        url: urlAd,
        type: 'GET',
        dataType: 'json',
        beforeSend: () => {
        },
        success: data => {
          //$('#titleCircuitTotal').text(data.results[0].title);
          let arrayTotal = new Set();
          let arrayCheck = new Set();
          data.results.forEach(function (row) {
            arrayIds.add(row.circuit);
            if (!arrayTotal.has(row.circuit)) {
              $('#feedmeTotal').append(row.html);
              arrayTotal.add(row.circuit);
              arrayCheck.add(row.id);
            } else {
              if (!arrayCheck.has(row.id)){
                row.food.forEach(function (food_id) {
                  let value = Number($(`#total-food-${food_id[0]}-${row.circuit}`).text());
                  value += food_id[1];
                  $(`#total-food-${food_id[0]}-${row.circuit}`).text(value);
                })
              }
            }
          })

          $('[id]').each(function () {
            $('[id="' + this.id + '"]:gt(0)').remove();
          })

          urlAd = `${url}/circuit-total-total/?search=${day}-${month}-${year}%2C${day2}-${month2}-${year2}`;
          $.ajax({
            url: urlAd,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
            },
            success: data => {
                $('#feedmeTotal').append(data.results[0].html);
            },
            error: (e) => {
              const html = getHtml(e.responseText);
            },
          });
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
              type: 'GET',
              dataType: 'json',
              beforeSend: () => {
              },
              success: data => {
                $(`#comment__${('0' + data.day).slice(-2)}-${('0' + data.month).slice(-2)}-${data.year}__${data.command_id}__${data.client_id}`).val("");
                $(`button[data-command="${command}"][data-bs-toggle="dropdown"]`).removeClass('btn-danger');
                $(`button[data-command="${command}"][data-bs-toggle="dropdown"]`).removeClass('btn-outline-light');
                if ($(`button[data-command="${command}"][data-bs-toggle="dropdown"]`).text().replace(/ /g,"").replace(/\n/g,"") == "0") {
                  $(`button[data-command="${command}"][data-bs-toggle="dropdown"]`).addClass('btn-outline-light');
                } else {
                  $(`button[data-command="${command}"][data-bs-toggle="dropdown"]`).addClass('btn-warning');
                }
                $(`.row-${command}`).css( "background-color", "darkgray" );
                if (data.has_comments.length == 0) {
                  $(`td.customer-comment-btn[data-client="${client}"]`).removeClass('comment');
                }
              },
              error: (e) => {
                console.log(e)
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