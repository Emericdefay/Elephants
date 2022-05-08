function reloadJs(src) {

    $('<script/>').attr('src', src).appendTo('head');
}

$(() => {
    const d = new Date()
    const date = window.location.href.split('?tab=#')[0].split('8000/')[1];

    let month;
    let year;
    if (date) {
        month = date.split('/')[1] ?? 0;
        year = date.split('/')[0] ?? 0;
    } else {
        month = 0; year = 0;
    }

    
    const url = `http://127.0.0.1:8000/api/getallclients/?month=${month}&year=${year}`;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        beforeSend: () => {
        },
        success: data => {
            // add class comment to line
            data.results.forEach(function (row) {
                $('#tbody-client').append(row.html);
            })
            setTimeout(() => {reloadJs('http://127.0.0.1:8000/static/js/clientfood.js');}, 500);
        },
        error: (e) => {
          console.log(e)
        },
    });
});