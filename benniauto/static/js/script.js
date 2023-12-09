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
      i18n: {done: "Select"}
  });

    // select
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

});


