// Send from data when user clicked on Sign up button
$(document).ready(function () {

    $("#signUpBtn").click(function (event) {
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


// Send from data when user clicked on Change password button
$(document).ready(function () {

    $("#changePasswordBtn").click(function (event) {
        // Getting CSRFToken
        const $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

        //Stop submit the form, we will post it manually.
        event.preventDefault();

        // Get form
        const form = $('#changePasswordForm')[0];
        // Create an FormData object
        const data = new FormData(form);


        $.ajax({
            type: "PUT",
            enctype: 'multipart/form-data',
            url: "/api/v1/change_password/",
            // Adding CSRFToken to headers
            headers: {"X-CSRFToken": $crf_token},
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function () {
                console.log("SUCCESS :");
                alert('Your password was successfully changed.')
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