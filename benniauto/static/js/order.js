document.addEventListener('DOMContentLoaded', function () {

  // need recovery toggle
  const needRecoveryToggle = document.getElementById('need_recovery');
  const addressFields = document.getElementById('address');

  needRecoveryToggle.addEventListener('change', function () {
    if (this.checked) {
      addressFields.style.display = 'block';
      document.getElementById('user_postcode').setAttribute('required', true);
      document.getElementById('user_address').setAttribute('required', true);
    } else {
      addressFields.style.display = 'none';
      document.getElementById('user_postcode').removeAttribute('required');
      document.getElementById('user_address').removeAttribute('required');
    }
  });

 



});