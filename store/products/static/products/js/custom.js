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


// Get data when user click on load more
$(document).ready(function () {
    let count = 0;

    $("#loadMoreBtn").click(function (event) {
        const category = $("#categoryP").text();
        count += 1;

        //Stop submit the form, we will post it manually.
        event.preventDefault();


        $.ajax({
            type: "GET",
            url: `/api/v1/product_list/?category=${category}&page=${count}`,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function (response) {
                console.log("SUCCESS :");

                let result = response.results

                for (let each in result) {

                    $("#productRow").append(
                        ` <div class="col-md-4">
                            <div class="card mb-4 product-wap rounded-0">
                                <div class="card rounded-0">
                                    <img class="card-img rounded-0 img-fluid" src="${result[each]['image']}"
                                         alt="{{ product.name }} Image">

                                    <div class="card-img-overlay rounded-0 product-overlay d-flex align-items-center justify-content-center">
                                        <ul class="list-unstyled">
                                            <li><a class="btn btn-success text-white" href="shop-single.html"><i
                                                    class="far fa-heart"></i></a></li>
                                            <li><a class="btn btn-success text-white mt-2"
                                                   href="{% url 'products:product_detail' product.slug %}"><i
                                                    class="far fa-eye"></i></a></li>
                                            <li><a class="btn btn-success text-white mt-2" href="shop-single.html"><i
                                                    class="fas fa-cart-plus"></i></a></li>
                                        </ul>
                                    </div>
                                </div>

                                <div class="card-body">
                                    <a href="{% url 'products:product_detail' product.slug %}"
                                       class="h3 text-decoration-none">${result[each]['name']}</a>
                                    <ul class="w-100 list-unstyled d-flex justify-content-between mb-0">
                                        <li class="pt-2">
                                            <span class="product-color-dot color-dot-red float-left rounded-circle ml-1"></span>
                                            <span class="product-color-dot color-dot-blue float-left rounded-circle ml-1"></span>
                                            <span class="product-color-dot color-dot-black float-left rounded-circle ml-1"></span>
                                            <span class="product-color-dot color-dot-light float-left rounded-circle ml-1"></span>
                                            <span class="product-color-dot color-dot-green float-left rounded-circle ml-1"></span>
                                        </li>
                                    </ul>
                                    <p class="text-center mb-0">${result[each]['price']}</p>
                                </div>
                            </div>
                        </div>
`)

                    console.log(result[each])
                }

                // console.log(e['results'])
                // console.log(category)
                // console.log(count)
            },

            error: function (error) {
                console.log("ERROR : ", error);

            }
        });

    });
});

