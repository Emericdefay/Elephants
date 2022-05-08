function reloadJs(src) {

    $('<script/>').attr('src', src).appendTo('head');
}

$(() => {
    const url = "http://127.0.0.1:8000/api/getallclients/"
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        beforeSend: () => {
        },
        success: data => {
            // add class comment to line
            data.results.forEach(function (row) {
                $('#tbody-planning').append(row.html);
            })
            setTimeout(() => {reloadJs('http://127.0.0.1:8000/static/js/planning.js');}, 500);
        },
        error: (e) => {
          console.log(e)
        },
    });
});