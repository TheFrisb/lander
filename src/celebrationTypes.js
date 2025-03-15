function initCelebrationTypes() {
  const button = document.querySelector("#showCelebrationTypesButton");
  const celebrationModalWithOverlay = document.querySelector(
    "#celebrationModalWithOverlay",
  );
  const celebrationModal = document.querySelector("#celebrationModal");
  const celebrationModalCloseButton = document.querySelector(
    "#celebrationModalCloseButton",
  );

  if (
    !button ||
    !celebrationModalWithOverlay ||
    !celebrationModal ||
    !celebrationModalCloseButton
  ) {
    console.error(
      "Some of the elements are missing. Please check if you have all the elements in the DOM.",
    );
    return;
  }

  button.addEventListener("click", () => {
    celebrationModalWithOverlay.classList.remove("hidden");
  });

  celebrationModalCloseButton.addEventListener("click", () => {
    celebrationModalWithOverlay.classList.add("hidden");
  });

  celebrationModalWithOverlay.addEventListener("click", (event) => {
    if (event.target === celebrationModalWithOverlay) {
      celebrationModalWithOverlay.classList.add("hidden");
    }
  });
}

export default initCelebrationTypes;
