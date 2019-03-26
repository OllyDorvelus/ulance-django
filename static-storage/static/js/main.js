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

// ORDER FUNCTIONS

function addToCart(serviceId, _this) {
    let api_url = `/api/orders/entries/add/${serviceId}/`
    _this.$http.post(api_url).then(function(response){
        onAlert("Service added to cart.")
    }).catch(function(err){
      if(err.status === 401) {
          onWarning("Please login to add to cart.")
      }
      if(err.body.message) {
          onWarning(err.body.message)
      }
    })
}

// SERVICES
function getServices(_this, api_url) {
    if (api_url) {
    _this.$http.get(api_url).then(function(response){
        _this.services = response.data.results
        _this.count = response.data.count
    })
    } else {
        _this.$http.get(_this.api_url).then(function (response) {
            _this.services = response.data.results
            _this.count = response.data.count
        })
    }
}

function getService(serviceId, _this) {
    _this.loading = true
    let api_url = `/api/services/${serviceId}/`
    _this.$http.get(api_url).then(function(response){
        console.log(response.data)
      _this.currentService = response.data;
      _this.getServiceCategories()
      _this.loading = false
      $('#editServiceModal').modal('show')
    })
}



function deleteService(serviceId, _this) {
        let api_url = `/api/services/${serviceId}/`
        const self = _this
        onDeletion("Are you sure you want to delete this service?", function(value){
            if(value) {
                _this.$http.delete(api_url).then(function (response) {
                    const service = response.data
                    onAlert('The service has been deleted')
                    _this.getServices()
                })
            }
        })
}

// EDITING CATEGORIES ON SERVICE

function getParentCategories(_this) {
    let api_url = '/api/services/main-categories/'
      _this.$http.get(api_url).then(function(response){
          _this.parentCategories = response.data.results  //this.parentCategories.concat(response.data.results)//
          if(_this.parentCategories[0]) {
              _this.parentCategoryId = _this.parentCategories[0].id
              getSubCategories(_this)
          }
      })
}

function getSubCategories(_this) {
   // _this.loading = true
    let api_url = `/api/services/sub-categories/${_this.parentCategoryId}/`
    _this.$http.get(api_url).then(function(response){
        _this.subCategories = response.data.results
       // _this.loading = false
    }).catch(function(err){
        _this.loading = false
    })
}

function getServiceCategories(_this) {
    _this.loading = true
    let api_url = `/api/services/${_this.currentService.id}/categories/`
    _this.$http.get(api_url).then(function(response){
        _this.categories = response.body
        _this.loading = false
    }).catch(function(err){
        _this.loading = false
    })
}

function addCategory(categoryId, _this) {
    let api_url = `/api/services/${_this.currentService.id}/add/${categoryId}/`
    _this.$http.post(api_url).then(function(response){
      _this.currentService = _this.getService(_this.currentService.id)
      _this.getServiceCategories()

    }).catch(function(err){
          const message = err.body.message
          onWarning(message)
      })
}

function removeCategory(categoryId, _this) {
    let api_url = `/api/services/${_this.currentService.id}/remove/${categoryId}/`
    _this.$http.post(api_url).then(function(response){
    _this.currentService = _this.getService(_this.currentService.id)
    _this.getServiceCategories()
    }).catch(function(err){
          const message = err.body.message
          onWarning(message)
      })
}

function getJobCategories(_this) {
    _this.loading = true
    let api_url = `/api/services/${_this.currentService.id}/categories/`
    _this.$http.get(api_url).then(function(response){
        _this.categories = response.body
        _this.loading = false
    }).catch(function(err){
        _this.loading = false
    })
}

function getJobSkills(_this) {

}

function addJobCategory(categoryId, _this) {

}

function removeJobCategory(categoryId, _this) {

}

// function getJobCategories(_this) {
//     _this.loading = true
//     let api_url = `/api/services/jobs/${_this.currentJob.id}/categories/`
//     _this.$http.get(api_url).then(function(response){
//         _this.jobCategories = response.body
//         _this.loading = false
//     }).catch(function(err){
//         _this.loading = false
//     })
// }

// EDITING SKILLS
function getParentSkills(_this) {
    let api_url = '/api/profiles/main-skills/'
    _this.$http.get(api_url).then(function(response){
        _this.parentSkills = response.data
        if(_this.parentSkills[0]) {
            _this.parentSkillId = _this.parentSkills[0].id
            getSubSkills(_this)
        }
    })
}

function getSubSkills(_this) {
   // _this.loading = true
    let api_url = `/api/profiles/sub-skills/${_this.parentSkillId}/`
    _this.$http.get(api_url).then(function(response){
        _this.subSkills = response.data.results
        _this.loading = false
    }).catch(function(err){
        _this.loading = false
    })
}

function getUserSkills(_this, api_url) {
   // _this.loading = true
    _this.$http.get(api_url).then(function(response){
        _this.skills = response.data.results
        _this.loading = false
    }).catch(function(err){
        _this.loading = false
    })
}

function addSkill(skillId, _this) {
    let api_url = `/api/profiles/skills/${_this.profile.id}/add/${skillId}/`
    _this.$http.post(api_url).then(function(response){
      _this.getSkills()
    }).catch(function(err){
          const message = err.body.message
          onWarning(message)
      })
}

function removeSkill(skillId, _this) {
    let api_url = `/api/profiles/skills/${_this.profile.id}/remove/${skillId}/`
    _this.$http.post(api_url).then(function(response){
    _this.getSkills()
    }).catch(function(err){
          const message = err.body.message
          onWarning(message)
      })
}