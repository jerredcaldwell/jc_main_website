const nav = document.querySelector('nav');
const line = document.querySelector('.line');
const links = document.querySelectorAll('a');

function highlightLink() {
  const linkCoords = this.getBoundingClientRect();
  const coords = {
    width: linkCoords.width,
    height: linkCoords.height,
    left: linkCoords.left + window.scrollX,
    top: linkCoords.top + window.scrollY
  };
  line.style.width = `${coords.width}px`;
  line.style.transform = `translate(${coords.left}px)`;
}

links.forEach(link => link.addEventListener('mouseenter', highlightLink));

nav.addEventListener('mouseleave', () => {
  line.style.width = '0';
});
