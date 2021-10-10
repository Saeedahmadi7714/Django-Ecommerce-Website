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

                // Username length < 3
                if ('username' in error['responseJSON'] && error['responseJSON']['username'].includes('3')) {
                    $(".alert").remove();
                    $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">${error['responseJSON']['username']}</div>`)

                    // Blank username
                } else if ('username' in error['responseJSON'] && error['responseJSON']['username'][0].includes('blank')) {
                    $(".alert").remove();
                    $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">Username must not be blank</div>`)

                    // Blank password
                } else if ('password' in error['responseJSON'] && error['responseJSON']['password'][0].includes('blank')) {
                    $(".alert").remove();
                    $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">Please enter a password</div>`)

                    // Blank password check
                } else if ('password_check' in error['responseJSON'] && error['responseJSON']['password_check'][0].includes('blank')) {
                    $(".alert").remove();
                    $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">Please enter password check</div>`)
                }

                // Duplicate username
                else if ('username' in error['responseJSON'] && error['responseJSON']['username'][0].includes('exists.')) {
                    $(".alert").remove();
                    $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">${error['responseJSON']['username'][0]}</div>`)
                }

                // Password length < 8
                else if ('password' in error['responseJSON'] && error['responseJSON']['password'].includes('8')) {
                    $(".alert").remove();
                    $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">${error['responseJSON']['password']}</div>`)
                }

                // Passwords not match
                else if ('password' in error['responseJSON'] && error['responseJSON']['password'].includes('must match')) {
                    $(".alert").remove();
                    $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">${error['responseJSON']['password']}</div>`)
                }

            }
        });

    })
    ;
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
                alert('Your password was successfully changed.')
                window.location = '/customer/sign_in/';
            },
            error: function (error) {
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
                $(".alert").remove();
                $("#error").prepend(`<div class="col-xl-12 alert alert-success d-flex justify-content-center" role="alert">Thanks for your message <p> &#128515;
 </p> </div>`)

            },
            error: function (error) {

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

                }

            },

            error: function (error) {

            }
        });

    });
});

// Set hidden input quantity value
$(document).ready(function () {
    $("#var-value").on('DOMSubtreeModified', function () {
        $('#product_quantity').val(`${$("#var-value").text()}`)

    });
});


// Delete an item from user basket
$(document).ready(function () {

    $(".deleteItemBtn").unbind().click(function () {

        const productId = $(this).attr("id")

        const $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        console.log($crf_token)
        const formData = new FormData(); // Create form data here
        formData.append('productId', productId);

        $.ajax({
            type: "POST",
            // Adding CSRFToken to headers
            headers: {"X-CSRFToken": $crf_token},
            url: "/order/basket/delete/",
            data: formData,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function () {
                $(`table tr#${productId}`).remove();

            },
            error: function (error) {

            }
        });

    });
});


// Offer code
$(document).ready(function () {

    $("#applyBtn").unbind().click(function () {

        const offerCode = $('#offerCode').val()

        const $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        console.log($crf_token)
        const formData = new FormData(); // Create form data here
        formData.append('offerCode', offerCode);

        $.ajax({
            type: "POST",
            // Adding CSRFToken to headers
            headers: {"X-CSRFToken": $crf_token},
            url: "/api/v1/offer_code/",
            data: formData,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function (response) {
                const offerCodeAmount = response['amount']
                const splicedTotalPrice = $('#totalPrice').text().split(':')[1].split('$')[1];
                const offer = splicedTotalPrice * offerCodeAmount / 100
                const totalPriceAfterOffer = (splicedTotalPrice - offer).toFixed(2)
                $('#totalPrice').text(`Total price : $${totalPriceAfterOffer}`)

                // Disable apply button if offer code successfully applied
                $("#applyBtn").attr('disabled', true);
            },
            error: function (error) {
                $(".alert").remove();
                $("#error").prepend(`<div class="col-xl-12 alert alert-danger d-flex justify-content-center" role="alert">${error['responseJSON'][Object.keys(error['responseJSON'])[0]]}</div>`)

            }
        });
    });
});
