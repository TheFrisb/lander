function initTimer() {
  // Select the timer container
  const timerCountdownEl = document.querySelector("#timerCountdown");

  // If the element doesn't exist, exit the function
  if (!timerCountdownEl) {
    return;
  }

  // Get the three time parts (hours, minutes, seconds)
  const timeParts = timerCountdownEl.querySelectorAll(".font-bold");

  // Ensure there are exactly three time parts
  if (timeParts.length !== 3) {
    console.error("Expected three time parts");
    return;
  }

  // Parse initial time from the HTML (e.g., "06", "56", "21")
  let hours = parseInt(timeParts[0].textContent, 10);
  let minutes = parseInt(timeParts[1].textContent, 10);
  let seconds = parseInt(timeParts[2].textContent, 10);

  // Calculate total seconds
  let totalSeconds = hours * 3600 + minutes * 60 + seconds;

  // Set up the interval to update every 1000ms (1 second)
  const intervalId = setInterval(() => {
    // If time is up, stop the countdown
    if (totalSeconds <= 0) {
      clearInterval(intervalId);
      return;
    }

    // Decrease the total seconds by 1
    totalSeconds--;

    // Calculate new hours, minutes, and seconds
    const h = Math.floor(totalSeconds / 3600);
    const m = Math.floor((totalSeconds % 3600) / 60);
    const s = totalSeconds % 60;

    // Update the display with leading zeros
    timeParts[0].textContent = String(h).padStart(2, "0");
    timeParts[1].textContent = String(m).padStart(2, "0");
    timeParts[2].textContent = String(s).padStart(2, "0");
  }, 1000);
}

export default initTimer;
