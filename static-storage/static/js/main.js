/**
 * Created by 13477 on 9/1/2018.
 */
$(document).ready(function() {
    $('.subnav-item').mouseenter(function(){
    //$(this).animate({backgroundColor: 'yellow'},500)
    $(this).animate({borderWidth: '2px'},250)
  }).mouseleave(function(){
    $(this).animate({borderWidth: '0px'},250)
  })

})

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function onDeletion(message, callback) {
     vex.dialog.buttons.YES.text = 'Delete'
     vex.dialog.buttons.YES.className = 'delete-confirm-btn'
     vex.dialog.confirm({
        message: message,
        className: 'vex-theme-os',
        callback: function(value) {
            callback(value)
        }
    })
}

function onAlert(message) {
    vex.dialog.buttons.YES.text = 'Ok'
    vex.dialog.buttons.YES.className = 'alert-btn'
    vex.dialog.alert({
        message: message,
        className: 'vex-theme-os',
    })
}

function onWarning(message) {
    vex.dialog.buttons.YES.text = 'Ok'
    vex.dialog.buttons.YES.className = 'warning-btn'
    vex.dialog.alert({
        message: message,
        className: 'vex-theme-top'
    })
}