$(document).ready(function() {
    $('#registration-form').on('submit', function(event) {
      event.preventDefault();
  
      const userData = {
        username: $('#username').val(),
        email: $('#email').val(),
        password: $('#password').val(),
        confirm_password: $('#confirm-password').val()
      };
  
      $.ajax({
        type: 'POST',
        url: '/api/register',
        contentType: 'application/json',
        data: JSON.stringify(userData),
        success: function(response) {
          $('#message').text(response.message).removeClass('alert-danger').addClass('alert-success');
        },
        error: function(xhr) {
          $('#message').text(xhr.responseJSON.message).removeClass('alert-success').addClass('alert-danger');
        }
      });
    });
  });
  