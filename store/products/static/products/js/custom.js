// Send from data when user clicked on create button
$(document).ready(function () {

    $("#signUpBtn").click(function (event) {
        console.log('Clicked')

        //Stop submit the form, we will post it manually.
        event.preventDefault();

        // Get form
        const form = $('#signUpCustomerForm')[0];

        // Create an FormData object
        const data = new FormData(form);


        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/api/v1/sign_up/",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function () {
                console.log("SUCCESS :");
                window.location = '/customer/sign_in/';
            },
            error: function (error) {
                console.log("ERROR : ", error);
                $(".alert").remove();
                $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">${error['responseJSON'][Object.keys(error['responseJSON'])[0]]}</div>`)

            }
        });

    });

});