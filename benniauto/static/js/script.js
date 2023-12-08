document.addEventListener('DOMContentLoaded', function () {
    // sidenav
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    let modal_del = document.querySelectorAll('.modal');
    M.Modal.init(modal_del);
});