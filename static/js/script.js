

const images = [
    "/static/images/hero-bg-1.jpg",
    "/static/images/hero-bg-2.jpg",
    "/static/images/hero-bg-3.jpg"
];

let index = 0;
function changeBackground() {
    document.getElementById("bg-slider").style.backgroundImage = `url(${images[index]})`;
    index = (index + 1) % images.length;
}

setInterval(changeBackground, 3000);
changeBackground();

