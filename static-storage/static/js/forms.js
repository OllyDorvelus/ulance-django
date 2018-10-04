/**
 * Created by 13477 on 9/12/2018.
 */
$(document).ready(function() {

    //Login Form
    $('#loginform').submit(function(e) {
        e.preventDefault();
        var this_ = $(this)
        var formData = this_.serialize()

        $.ajax({
            url: "/rest-auth/login/",
            data: formData,
            method: "POST",
            success: function(data) {
                window.location.replace('/')
            },
            error: function(data) {
                var jsondata = JSON.parse(data.responseText)
                attatchFormErrors(jsondata)
            }
        })

    })

    //Register Form
    $('#registerform').submit(function(e) {
        e.preventDefault();
        var this_ = $(this)
        var formData = this_.serialize()

        $.ajax({
            url: "/api/accounts/register/",
            data: formData,
            method: "POST",
            success:function(data) {
                window.location.replace('/login/')
            },
            error: function(data) {
                var jsondata = JSON.parse(data.responseText)
                attatchFormErrors(jsondata)
            }

        })
    })
  //  (".form-group > div > p").show()
$('.logout-btn').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/rest-auth/logout/",
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
             },

            data: {},
            method: "POST",
            success: function(data) {
              window.location.replace('/')
            },
            error: function(data) {

            }
        })
    }
)

$('.cancel-btn').click(function(e) {
    e.preventDefault();
    var form_id = $(this).attr('cancel')
    $('#' + form_id).hide()
    var section = 'no-' + form_id
    $('#' + section).show()
})

$('.add-btn').click(function(e) {
    e.preventDefault();
    var section = $(this).attr('show')
    $('#' + section).hide()
    var form_id = section.replace('no-', '')
    $('#' + form_id).show()
})


})





function attatchErrors(errors) {
    var starthtml = "<ul id='errorslist'>"
    var endhtml = "</ul>"
    var htmlString
    $.each(errors, function(key, value) {
        console.log(key, value)
        htmlString += "<li>" + value + "</li>"
    })
   htmlString = starthtml + htmlString + endhtml;
   $('#errorslist').replaceWith(htmlString)
   $('#errors-container').show()

}

function attatchFormErrors(errors) {
    var starthtml = "<ul id='errorslist'>"
    var endhtml = "</ul>"
    var htmlString
    $('.form-group > div > span').hide()
    $.each(errors, function(key, value) {
        var ID = '#' + key
       $(ID).replaceWith("<span class='text-center text-danger' style='display:block' id=" + key + ">" + value + "</span>")
       // $('.form-group > div > p').show()
    })
   htmlString = starthtml + htmlString + endhtml;
  // $('#errorslist').replaceWith(htmlString)
  // $('#errors-container').show()

}

function login(username, password) {
    $.ajax({
        url: "/rest-auth/login/",
        data: {username: username, password: password},
        type:"POST",

        success: function(data) {
            console.log("logging in user")
            console.log(data)
        },
        error: function(data) {
            console.log(data)
            console.log("error")
        }
    })
}