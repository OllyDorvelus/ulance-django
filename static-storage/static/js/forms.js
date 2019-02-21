/**
 * Created by 13477 on 9/12/2018.
 */



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

function logout() {
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

//function cancelForm(form_id, e) {
//    $('#' + form_id).hide()
//    var section = 'no-' + form_id
//    $('#' + section).show()
//}
//
//function addEdit(section) {
//    $('#' + section).hide()
//    var form_id = section.replace('no-', '')
//    $('#' + form_id).show()
//}

//$('.add-edit-btn').click(function(e) {
//    e.preventDefault();
//    var section = $(this).attr('show')
//    $('#' + section).hide()
//    var form_id = section.replace('no-', '')
//    $('#' + form_id).show()
//})

//function deleteData(ID, url) {
//    var result = confirm("Are you sure you want to delete?")
//    console.log(ID)
//    console.log(url)
//    if(result) {
//        $.ajax({
//            url: url,
//            beforeSend: function (xhr) {
//                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
//            },
//            data: {},
//            method: "DELETE",
//            success: function () {
//                $('#' + ID).hide()
//            },
//            error: function (data) {
//                alert("This item has not been deleted")
//                console.log(data) }
//
//        })
//    }
//}

function attachFormErrors(errors, edit, model) {
    var starthtml = "<ul id='errorslist'>"
    var endhtml = "</ul>"
    var htmlString
    $('.form-group > div > span').hide()
    $.each(errors, function(key, value) {
        var ID = '#' + key
        if(edit) {
            ID = ID + '_edit'
        }
        if(model) {
            ID = ID + '_' + model
        }
       $(ID).replaceWith("<span class='text-center text-danger' style='display:block' id=" + key + ">" + value + "</span>")
       // $('.form-group > div > p').show()
    })
   htmlString = starthtml + htmlString + endhtml;
  // $('#errorslist').replaceWith(htmlString)
  // $('#errors-container').show()

}


function editLink(ID) {
    var form = $('#edit-link-form')
    var url = '/api/profiles/link/' + ID + '/'
    var linkstring = "link"
    form.attr('data-url', url)
    form.attr('data-id', ID)
    var brief_description = form.find('input[name="brief_description"]')
    var link = form.find('input[name=link]')
    $.ajax({
        url: url,
        method: "GET",
        success:function(data){
            link.val(data.linkstring)
            brief_description.val(data.brief_description)
        }
    })
}

$(document).ready(function() {
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
                attachFormErrors(jsondata)
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
                attachFormErrors(jsondata)
            }

        })
    })

    $('#add-link-form').submit(function(e) {
        e.preventDefault()
        var this_ = $(this)
        var formData = this_.serialize()
        $.ajax({
            url: "/api/profiles/link/create/",
            data: formData,
            method: "POST",
            success: function(data) {
                console.log(data)
                $('#add-link-form').hide()
                $('#no-add-link-form').show()
                var htmlString = "<div class='link-list' id='" + data.id + "' data-url='/api/profiles/link/" + data.id + "/'><p style='display:inline'>" + data.brief_description + "</p>" +
                "<i class='far fa-edit add-edit-btn edit-link-btn' show='no-edit-link-form' onclick=editLink('" + data.id + "');addEdit('no-edit-link-form')></i><i class='far fa-trash-alt' onclick=deleteData('"+ data.id + "','/api/profiles/link/"+data.id +"/')></i>" +
                "<a href='" + data.link + "' target='_blank' style='display:block'>" + data.link + "</a>" +
                "</div>"

                $('#link-section').append(htmlString)
            },
            error: function(data) {
                console.log(data)
                var jsondata = JSON.parse(data.responseText)
                //attatchFormErrors(jsondata)
            }

        })
    })


    //$('.edit-link-btn').click(function(e) {
    //    e.preventDefault()
    //    var this_ = $(this)
    //    var item_div = this_.closest('div')
    //    var url = item_div.attr('data-url')
    //    var ID = item_div.attr('id')
    //    var form = $('#edit-link-form')
    //    console.log(ID)
    //    console.log(URL)
    //    form.attr('data-url', url)
    //    form.attr('data-id', ID)
    //    var brief_description = form.find('input[name="brief_description"]')
    //    var link = form.find('input[name="link"]')
    //    $.ajax({
    //        url: url,
    //        method: "GET",
    //        success:function(data){
    //            link.val(data.link)
    //            brief_description.val(data.brief_description)
    //        }
    //    })
    //
    //})

    //$('#edit-link-form').submit(function(e){
    //    e.preventDefault()
    //    var this_ = $(this)
    //    var formData = this_.serialize()
    //    var url = this_.attr('data-url')
    //    var ID = this_.attr('data-id')
    //    console.log('url', url)
    //    console.log('id', ID)
    //    $.ajax({
    //        beforeSend: function(xhr) {
    //            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    //         },
    //        url: url,
    //        data: formData,
    //        method: "PUT",
    //        success: function(data) {
    //            $('#edit-link-form').hide()
    //            $('#no-edit-link-form').show()
    //
    //            var htmlString = "<div class='link-list' id='" + data.id + "' data-url='/api/profiles/link/" + data.id + "/'><p style='display:inline'>" + data.brief_description + "</p>" +
    //            "<i class='far fa-edit add-edit-btn edit-link-btn' show='no-edit-link-form' onclick=editLink('" + data.id + "');addEdit('no-edit-link-form')></i><i class='far fa-trash-alt' onclick=deleteData('"+ data.id + "','/api/profiles/link/"+data.id +"/')></i>" +
    //            "<a href='" + data.link + "' target='_blank' style='display:block'>" + data.link + "</a>" +
    //            "</div>"
    //
    //            $('#' + ID).replaceWith(htmlString)
    //        },
    //        error: function(data) {
    //            var jsondata = JSON.parse(data.responseText)
    //            attatchFormErrors(jsondata)
    //        }
    //
    //    })
    //})

    //$('#add-certification-form').submit(function(e){
    //    e.preventDefault()
    //    var this_ = $(this)
    //    var formData = this_.serialize()
    //    $.ajax({
    //        url: '/api/profiles/certification/create/',
    //        data: formData,
    //        success: function(data){
    //            $('#add-certification-form').hide()
    //            $('#no-add-certification-form').show()
    //
    //            var htmlString = "<p>" + data.issued_from + " - " + data.name + " | " + data.year_issued + "</p><i class='far fa-edit add-edit-btn edit-certification-btn'"
    //        },
    //        error: function(data) {
    //            var jsondata = JSON.parse(data.responseText)
    //            attatchFormErrors(jsondata)
    //        }
    //    })
    //})





//$('.logout-btn').click(function(e) {
//        e.preventDefault();
//
//
//    }
//)




//$('.cancel-btn').click(function(e) {
//    e.preventDefault();
//    var form_id = $(this).attr('cancel')
//  //  var form_id = $(this).closest('form').attr('id')
//    $('#' + form_id).hide()
//    var section = 'no-' + form_id
//    $('#' + section).show()
//})

//$('.add-edit-btn').click(function(e) {
//    e.preventDefault();
//    var section = $(this).attr('show')
//    $('#' + section).hide()
//    var form_id = section.replace('no-', '')
//    $('#' + form_id).show()
//})




})







    //function hideAndAttach(ID, data, htmlString, appendSection) {
    //    $('#' + ID).hide()
    //    var form_id = $(ID).attr('id')
    //    var section = "no-" + form_id
    //    $('#' + section).show()
    //    $('#' + appendSection).append(htmlString)
    //}

    //function getHtmlString(htmlString, data) {
    //    return htmlString
    //}
    //
    //function submitForm(ID, url, htmlString, appendSection) {
    //        e.preventDefault()
    //        var this_ = $(this)
    //        var formData = this_.serialize()
    //
    //        $.ajax({
    //            url: url,
    //            data: formData,
    //            method: "POST",
    //            success: function(data) {
    //                console.log(data)
    //                $('#' + ID).hide()
    //                $('#' + ID).attr('htmlString')
    //                var form_id = $(ID).attr('id')
    //                var section = "no-" + form_id
    //                $('#' + section).show()
    //
    //                $('#' + appendSection).append(htmlString)
    //            },
    //            error: function(data) {
    //                console.log(data)
    //                var jsondata = JSON.parse(data.responseText)
    //                attatchFormErrors(jsondata)
    //            }
    //        })
    //}