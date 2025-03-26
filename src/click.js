function makeClickRequest(clickType) {
  const crsftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const url = "/api/v1/click/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": crsftoken,
    },
    body: JSON.stringify({
      click_type: clickType,
    }),
  });
}

export default makeClickRequest;
