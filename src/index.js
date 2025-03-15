import initTestimonialSliders from "./testimonialSliders";
import initVideoSlider from "./videoSlider";
import initTimer from "./timer";
import initCelebrationTypes from "./celebrationTypes";
import initTriggerDropdownButton from "./triggerDropdownButton";

document.addEventListener("DOMContentLoaded", () => {
  initVideoSlider();
  initTestimonialSliders();
  initTimer();
  initCelebrationTypes();
  initTriggerDropdownButton();

  const mainBodyContainerEl = document.querySelector("#mainBody");
  const telegramIconEl = document.querySelector("#telegramIcon");

  if (mainBodyContainerEl && telegramIconEl) {
    function updatePosition() {
      const rect = mainBodyContainerEl.getBoundingClientRect();
      document.body.style.setProperty(
        "--container-left",
        `${rect.left + 16}px`,
      );
    }

    // Update position on load and resize
    window.addEventListener("resize", updatePosition);
    updatePosition();
    telegramIconEl.classList.remove("invisible");
  }
});
