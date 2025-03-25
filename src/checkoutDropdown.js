function initCheckoutDropdown() {
  const checkoutDropdownEl = document.querySelector("#checkoutDropdown");

  if (!checkoutDropdownEl) {
    return;
  }

  checkoutDropdownEl.addEventListener("click", () => {
    const svgEl = checkoutDropdownEl.querySelector("svg");
    const dropdownContainer = checkoutDropdownEl.nextElementSibling;

    svgEl.classList.toggle("rotate-180");
    dropdownContainer.classList.toggle("hidden");
  });
}

export default initCheckoutDropdown;
