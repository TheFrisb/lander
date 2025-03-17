import Swiper from "swiper";
import { Navigation, Pagination, Thumbs } from "swiper/modules";

function initVideoSlider() {
  const videoSliderEl = document.querySelector(".videoSwiper");

  if (!videoSliderEl) {
    return;
  }

  // Initialize the thumbnail slider
  const thumbnailSwiper = new Swiper(".thumbnailSwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    freeMode: true,
    watchSlidesProgress: true,
    // pagination: {
    //   el: ".swiper-pagination",
    //   clickable: true,
    // },
    modules: [Pagination],
  });

  // Initialize the main video slider
  const videoSlider = new Swiper(".videoSwiper", {
    modules: [Navigation, Thumbs],
    loop: true,
    speed: 500,
    grabCursor: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: {
      swiper: thumbnailSwiper, // Link to the thumbnail slider
    },
  });

  // Handle video play/pause on initialization
  videoSlider.slides.forEach((slide) => {
    const video = slide.querySelector("video");
    if (video) {
      if (slide.classList.contains("swiper-slide-active")) {
        video.muted = false;
        video.play();
      } else {
        video.pause();
        video.muted = true;
      }
    }
  });

  // Handle video play/pause on slide change
  videoSlider.on("slideChange", function () {
    const previousSlide = videoSlider.slides[videoSlider.previousIndex];
    const activeSlide = videoSlider.slides[videoSlider.activeIndex];

    const previousVideo = previousSlide.querySelector("video");
    const activeVideo = activeSlide.querySelector("video");

    if (previousVideo) {
      previousVideo.pause();
      previousVideo.muted = true;
    }

    if (activeVideo) {
      activeVideo.play();
      activeVideo.muted = false;
    }
  });
}

export default initVideoSlider;
