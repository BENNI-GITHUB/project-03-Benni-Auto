document.addEventListener('DOMContentLoaded', function () {
  // sidenav
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // Modal
  let modal_del = document.querySelectorAll('.modal');
  M.Modal.init(modal_del);

  // Datepicker
  let datepicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    disableWeekends: true,
    i18n: {
      done: "Select"
    }
  });

  // select
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // collapsible initializataion
  let collapsibles = document.querySelectorAll(".collapsible");
  M.Collapsible.init(collapsibles);


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