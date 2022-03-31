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
    $('#unique-modal').modal('show');
  }
  
  // close the modal for single ads
  function hideAdModal () {
    // hide modal
    $('#unique-modal').modal('hide').on('shown.bs.modal', () => {
      $('#unique-modal').modal('show');
    });
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
    return data.html;
  }
  
  function displayDjangoMsg () {
    hideAdModal();
    return `
    <script>
      $(document).ready(function() {
        toastr["error"]("ACTIF", "${gettext('Error. The ad is unavailable.')}");
      });
    </script>
    `;
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
      openAdModal();
    });
  });
  