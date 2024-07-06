document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const usernameOrEmail = document.getElementById('usernameOrEmail').value;
    const password = document.getElementById('password').value;

    fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username_or_email: usernameOrEmail, password: password }),
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('message').textContent = data.message;
      document.getElementById('message').className = data.success ? 'alert alert-success' : 'alert alert-danger';
      //check cookie again to update the username
      document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
    });
  });

  document.getElementById('forgotPassword').addEventListener('click', function() {
    const email = prompt("Enter your email for password reset:");
    if (email) {
      fetch('/api/forgot_password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: email }),
      })
      .then(response => response.json())
      .then(data => {
        alert(data.message);
      });
    }
  });
