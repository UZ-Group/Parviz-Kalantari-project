// Tooltip
$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
// Tooltip

// like btn 

const select_btn = document.querySelector('.like-btn');

select_btn.addEventListener('click', () => {

  const select_btn = document.querySelector('.like-btn');

  if(select_btn.classList.contains('far')) {
    select_btn.classList.remove('far');
    select_btn.classList.add('fas');
  } else {
    select_btn.classList.remove('fas');
    select_btn.classList.add('far');
  }
})