// Imagenes hostel

const myCarousel = new bootstrap.Carousel(document.getElementById('carouselActividades'), {
    interval: 2000, // Cambiar la imagen cada 2 segundos
    wrap: true // Repetir el carrusel cuando llega al final
  });



  // Video en Hostel
const videoCarrusel = document.getElementById('videoCarrusel');

function playVideo() {
  videoCarrusel.play();
}

const carrusel = new bootstrap.Carousel(document.querySelector('.calidad-ambiente'), {
  interval: 2000,
  wrap: true
});

carrusel.addEventListener('slide.bs.carousel', function () {
  playVideo();
});