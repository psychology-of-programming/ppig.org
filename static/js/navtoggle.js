
// Grab any element that has the js-toggle class and add an event listener for the toggle function
var toggleButtons = document.getElementsByClassName('js-toggle');
for (var i = 0; i < toggleButtons.length; i++) {
  toggleButtons[i].addEventListener('click', toggle, false);
}

function toggle(e) {
  var toggleButton = e.target;
  var listElement = toggleButton.parentElement;
  var elementToToggle = listElement.nextElementSibling;
  elementToToggle.classList.toggle('visible');

  // Hide the other submenus
  var menuContainer = listElement.parentElement;
  for (var i = 0; i < menuContainer.children.length; i++) {
    const listElement = menuContainer.children[i];
    if (listElement != elementToToggle) {
      listElement.classList.remove('visible');
    }
  }
}
