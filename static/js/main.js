

const openModalBtn = document.getElementById('openModal');
const modal = document.getElementById('modal');
const closeModalBtn = document.getElementsByClassName('close')[0];

openModalBtn.addEventListener('click', function() {
  modal.style.display = 'block';
});

closeModalBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});

window.addEventListener('click', function(event) {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
});


document.querySelector('.catalog-menu__btn').addEventListener('click', function() {
  document.querySelector('.catalog-menu__submenu').classList.toggle('show');
});


document.querySelector('.filter__btn').addEventListener('click', function() {
  document.querySelector('.filter__form-menu').classList.toggle('show-filter');
});
