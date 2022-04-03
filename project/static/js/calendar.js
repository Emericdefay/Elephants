$(document).ready(function(){
    // Add smooth scrolling to all links
    $("a.save-position").on('click', function(event) {

        let anchor = $(this).data('anchor');
        console.log(anchor);
        const element = document.getElementById(`week_${anchor}`);
        event.preventDefault();
        element.scrollIntoView({
            behavior: "smooth",
            block: "start",
            inline: "center"
        });

    })
});