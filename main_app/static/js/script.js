
const dateEl = document.getElementById('id_date');

M.Datepicker.init(dateEl, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: true,
    autoClose: true
});
// document.addEventListener('DOMcontentLoaded', function() {
//     var dateEl = document.querySelectorAll('.datepicker');
//     var date = M.Datepicker.init(dateEl, {
//         format: 'yyyy-mm-dd',
//         defaultDate: new Date(),
//         setDefaultDate: true,
//         autoClose: true
//     });
// })


const checkedEl = document.getElementById('id_watered');

M.Checkbox.init(checkedEl);