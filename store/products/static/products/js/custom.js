// Sign up
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


// Change password
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


// Send contact form
$(document).ready(function () {

    $("#letsTalkBtn").click(function (event) {

        if (!$("#subject").val()) {
            $(".alert").remove();
            $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">Please enter subject</div>`)
        }

        if (!$("#message").val()) {
            $(".alert").remove();
            $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">Please enter message </div>`)
        }


        //Stop submit the form, we will post it manually.
        event.preventDefault();

        // Get form
        const form = $('#contactForm')[0];
        // Create an FormData object
        const data = new FormData(form);


        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/api/v1/contact/",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function () {
                console.log("SUCCESS :");
                $(".alert").remove();
                $("#error").prepend(`<div class="col-xl-12 alert alert-success d-flex justify-content-center" role="alert">Thanks for your message <p> &#128515;
 </p> </div>`)

            },
            error: function (error) {
                console.log("ERROR : ", error);

            }
        });

    });
});
