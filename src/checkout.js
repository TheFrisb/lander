import { Notyf } from "notyf";

function initCheckoutOptions() {
  const checkoutOptionsEls = document.querySelectorAll(".checkoutOption");

  if (!checkoutOptionsEls.length) {
    return;
  }

  checkoutOptionsEls.forEach((checkoutOptionEl) => {
    const checkbox = checkoutOptionEl.querySelector(
      ".checkoutOption__checkbox",
    );

    checkbox.addEventListener("change", () => {
      const optionInput = checkoutOptionEl.querySelector(
        ".checkoutOption__input",
      );

      if (optionInput) {
        toggleInputSection(optionInput);
      }

      updateCheckoutSummary();
    });
  });

  function toggleInputSection(optionInput) {
    const parentEl = optionInput.parentElement;
    parentEl.classList.toggle("hidden");
  }
}

function initCheckoutButton() {
  const button = document.querySelector("#checkoutButton");
  const notyf = new Notyf({
    duration: 3000,
    position: {
      x: "right",
      y: "top",
    },
  });

  if (!button) {
    return;
  }

  button.addEventListener("click", async () => {
    const emailInput = document.querySelector("#checkoutEmailInput");
    const checkoutOptionInput = document.querySelectorAll(
      ".checkoutOption__input",
    );

    let hasError = false;

    if (!emailInput.value) {
      notyf.error("Please enter your email address.");
      emailInput.classList.add("!border-red-500");
      return;
    }

    checkoutOptionInput.forEach((input) => {
      input.classList.remove("!border-red-500");
      const parent = input.parentElement.parentElement.parentElement;
      console.log(parent);
      const checkbox = parent.querySelector(".checkoutOption__checkbox");

      if (checkbox.checked && !input.value) {
        input.classList.add("!border-red-500");
        notyf.error(`Please fill in the details for ${parent.dataset.title}.`);
        hasError = true;
      }
    });

    if (hasError) {
      return;
    }

    const response = await fetch("/payments/api/v1/checkout/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector(
          'input[name="csrfmiddlewaretoken"]',
        ).value,
      },
      body: JSON.stringify({
        email: emailInput.value,
        total_price: document
          .querySelector("#checkoutTotalPrice")
          .textContent.slice(1),
      }),
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data);
      window.location.href = data.redirect_url;
    } else {
      notyf.error("Something went wrong. Please try again.");
    }
  });
}

function updateCheckoutSummary() {
  const checkoutSummaryEl = document.querySelector(
    "#checkoutSummaryOptionsContainer",
  );
  const checkoutTotalPriceEl = document.querySelector("#checkoutTotalPrice");
  const checkoutButtonPriceEl = document.querySelector("#checkoutButtonPrice");
  const chosenProductSalePrice = document.querySelector(
    "#checkoutChosenProductSalePrice",
  );
  const checkoutOptionsEls = document.querySelectorAll(".checkoutOption");

  let html = "";

  let optionsSum = 0;

  checkoutOptionsEls.forEach((checkoutOptionEl) => {
    const checkbox = checkoutOptionEl.querySelector(
      ".checkoutOption__checkbox",
    );

    if (checkbox.checked) {
      const price = checkoutOptionEl.dataset.price;
      const title = checkoutOptionEl.dataset.title;
      const subtitle = checkoutOptionEl.dataset.subtitle;
      html += `
      <div class="flex flex-col gap-1 border-b border-gray-50 py-2 last:border-b-0">
          <div class="flex justify-between text-sm">
            <span class="text-gray-600">${title}</span>
            <span class="font-medium">$${price}</span>
          </div>
          
        `;
      if (subtitle) {
        html += `
        <div class="text-xs text-gray-500 italic pl-2 border-l-2 border-gray-100">${subtitle}</div>
        </div>
            `;
      } else {
        html += "</div>";
      }

      optionsSum += parseFloat(price);
    }
  });

  const productPrice = parseFloat(chosenProductSalePrice.textContent.slice(1));
  const totalPrice = productPrice + optionsSum;

  checkoutTotalPriceEl.textContent = `€${totalPrice.toFixed(2)}`;
  checkoutButtonPriceEl.textContent = `€${totalPrice.toFixed(2)}`;

  checkoutSummaryEl.innerHTML = html;
}

export default initCheckoutOptions;
export { updateCheckoutSummary, initCheckoutButton };
