import makeClickRequest from "./click";

function initCheckoutDropdown() {
  const checkoutDropdownEl = document.querySelector("#checkoutDropdown");

  if (!checkoutDropdownEl) {
    return;
  }

  checkoutDropdownEl.addEventListener("click", () => {
    const svgEl = checkoutDropdownEl.querySelector("svg");
    const dropdownContainer = checkoutDropdownEl.nextElementSibling;

    if (!svgEl.classList.contains("rotate-180")) {
      makeClickRequest("VIEW_CHECKOUT_OPTIONS");
    }

    svgEl.classList.toggle("rotate-180");
    dropdownContainer.classList.toggle("hidden");
  });
}

export default initCheckoutDropdown;
