// show the modal for single ads
function openAdModal () {
    // show modal
    $('#add-modal').modal('show');
  }
  
  // close the modal for single ads
  function hideAdModal () {
    // hide modal
    $('#add-modal').modal('hide').on('shown.bs.modal', () => {
      $('#add-modal').modal('show');
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
      openAdModal();

        
    });
  });
  