export default {
  document.querySelector('a').addEventListener('click', function () {
    confirm(this.dataset.confirm)
  })
}
