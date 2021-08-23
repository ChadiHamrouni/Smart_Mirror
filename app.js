function openNav() {
  document.getElementById("myNav").style.height = "100%";
}
function closeNav() {
  document.getElementById("myNav").style.height = "0%";
}
let btnOpen = document.querySelector('submit');
let input = document.querySelector('input');
 
btnOpen.addEventListener('click', () => {
    window.open(input.value, '_top');
});