import initTestimonialSliders from "./testimonialSliders";
import initVideoSlider from "./videoSlider";
import initTimer from "./timer";
import initCelebrationTypes from "./celebrationTypes";
import initTriggerDropdownButton from "./triggerDropdownButton";
import initCheckoutOptions, { initCheckoutButton } from "./checkout";
import { initLanguagePicker } from "./languagePicker";
import initCheckoutDropdown from "./checkoutDropdown";

document.addEventListener("DOMContentLoaded", () => {
  initVideoSlider();
  initTestimonialSliders();
  initTimer();
  initCelebrationTypes();
  initTriggerDropdownButton();
  initCheckoutOptions();
  initCheckoutButton();
  initLanguagePicker();
  initCheckoutDropdown();

  const mainBodyContainerEl = document.querySelector("#mainBody");
  const telegramIconEl = document.querySelector("#telegramIcon");
  const languagePickerEl = document.querySelector("#languagePicker");

  if (mainBodyContainerEl && telegramIconEl) {
    function updatePosition() {
      const rect = mainBodyContainerEl.getBoundingClientRect();
      document.body.style.setProperty(
        "--container-left",
        `${rect.left + 16}px`,
      );
    }

    window.addEventListener("resize", updatePosition);
    updatePosition();
    telegramIconEl.classList.remove("invisible");
  }
});
