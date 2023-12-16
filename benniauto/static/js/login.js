document.addEventListener('DOMContentLoaded', function () {
  
   // passwords view toggle
   document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordInput = document.getElementById('password');
    if (passwordInput.type === 'password') {
      passwordInput.type = 'text';
      this.classList.remove('fa-eye-slash');
      this.classList.add('fa-eye');
    } else {
      passwordInput.type = 'password';
      this.classList.remove('fa-eye');
      this.classList.add('fa-eye-slash');
    }
  });

});