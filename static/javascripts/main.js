// Components
// import './components/_links.js'

document.addEventListener("DOMContentLoaded", function(event) {
  const links = document.querySelectorAll('a')

  for (const link of links) {
    link.addEventListener('click', function () {
      confirm(this.dataset.confirm)
      console.log(this.dataset)
    })
  }
});
