import { updateCheckoutSummary } from "./checkout";

function initTriggerDropdownButton() {
  const button = document.querySelector(".triggerDropdownButton");
  const chosenProductSalePrice = document.querySelector(
    "#chosenProductSalePrice",
  );
  const goToCheckoutButton = document.querySelector("#goToCheckoutButton");

  if (!button) {
    return;
  }

  const dropdown = button.nextElementSibling;

  let isCheckoutPage = false;
  let activeProductId = dropdown.dataset.activeProductId;

  if (dropdown.dataset.isCheckoutPage == "true") {
    isCheckoutPage = true;
  }

  const dropdownOptions = dropdown.querySelectorAll(".productDropdownOption");

  button.addEventListener("click", () => {
    dropdown.classList.toggle("hidden");
  });

  dropdownOptions.forEach((option) => {
    option.addEventListener("click", () => {
      resetAllDropdownOptions(dropdownOptions);

      activeProductId = option.dataset.productId;
      option.classList.add("bg-blue-500/5", "text-blue-500");
      const checkIcon = option.querySelector(".checkIcon");
      checkIcon.classList.remove("hidden");

      const productName = option.dataset.productName;
      const productDescription = option.dataset.productDescription;
      const productRegularPrice = option.dataset.productRegularPrice;
      const productSalePrice = option.dataset.productSalePrice;

      updateChosenProduct(
        activeProductId,
        productName,
        productDescription,
        productRegularPrice,
        productSalePrice,
      );

      if (!isCheckoutPage) {
        updateProductPageMetadata(activeProductId, productSalePrice);
      } else {
        updateCheckoutPageMetadata(
          activeProductId,
          productName,
          productSalePrice,
        );
      }

      dropdown.classList.add("hidden");
    });
  });

  function updateCheckoutPageMetadata(
    activeProductId,
    productName,
    productSalePrice,
  ) {
    const checkoutOrderSummaryEl = document.querySelector(
      "#checkoutOrderSummary",
    );
    const checkoutChosenProductName = document.querySelector(
      "#checkoutChosenProductName",
    );
    const checkoutChosenProductSalePrice = document.querySelector(
      "#checkoutChosenProductSalePrice",
    );

    const checkoutBuyButtonPriceEl = document.querySelector(
      "#checkoutButtonPrice",
    );

    checkoutChosenProductName.textContent = productName;
    checkoutChosenProductSalePrice.textContent = `€${productSalePrice}`;
    checkoutBuyButtonPriceEl.textContent = `€${productSalePrice}`;

    updateCheckoutSummary();
  }

  function updateProductPageMetadata(activeProductId, productSalePrice) {
    if (isCheckoutPage) {
      console.error("This function should only be called on the product page.");
      return;
    }

    chosenProductSalePrice.textContent = `€${productSalePrice}`;
    goToCheckoutButton.href = `/payments/checkout/${activeProductId}/`;
  }

  function updateChosenProduct(
    activeProductId,
    productName,
    productDescription,
    productRegularPrice,
    productSalePrice,
  ) {
    const productNameEl = button.querySelector(".productName");
    const productDescriptionEl = button.querySelector(".productDescription");
    const productRegularPriceEl = button.querySelector(".productRegularPrice");
    const productSalePriceEl = button.querySelector(".productSalePrice");

    productNameEl.textContent = productName;
    productDescriptionEl.textContent = productDescription;
    if (productRegularPriceEl) {
      productRegularPriceEl.textContent = `€${productRegularPrice}`;
    }
    productSalePriceEl.textContent = `€${productSalePrice}`;
  }
}

function resetAllDropdownOptions(dropdownOptions) {
  dropdownOptions.forEach((option) => {
    option.classList.remove("bg-blue-500/5", "text-blue-500");
    const checkIcon = option.querySelector(".checkIcon");
    checkIcon.classList.add("hidden");
  });
}

export default initTriggerDropdownButton;
