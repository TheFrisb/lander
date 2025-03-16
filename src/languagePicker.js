function initLanguagePicker() {
  const languagePicker = document.querySelector("#languagePicker");

  if (!languagePicker) {
    return;
  }

  languagePicker.addEventListener("click", function () {
    const arrowIcon = languagePicker.querySelector(".arrowIcon");
    const dropdown = languagePicker.nextElementSibling;
    dropdown.classList.toggle("hidden");
    arrowIcon.classList.toggle("rotate-180");
  });
}

export { initLanguagePicker };
