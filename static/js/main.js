$(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
            data : {
                name : $('#exampleFormControlInput1').val(),
                phone : $('#exampleFormControlInput2').val(),
                text: $('#exampleFormControlTextarea3').val()
            },
            type : 'POST',
            url : '/'
        })
        .done(function(data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            }
            else {
                $('#successAlert').text(data.success).show();
                $('#errorAlert').hide();
            }
        });
        event.preventDefault();
    });
});
