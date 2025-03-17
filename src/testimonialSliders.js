import Swiper from "swiper";
import { Navigation, Pagination } from "swiper/modules";

function initTestimonialSliders() {
  const testimonialSliderEl = document.querySelector(".testimonialSwiper");

  if (!testimonialSliderEl) {
    return;
  }

  const testimonialSlider = new Swiper(".testimonialSwiper", {
    modules: [Navigation, Pagination],
    loop: true,
    speed: 500,
    grabCursor: true,

    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 24,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 32,
      },
    },
  });
}

export default initTestimonialSliders;
