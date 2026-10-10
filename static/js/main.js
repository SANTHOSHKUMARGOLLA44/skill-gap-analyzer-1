document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("menuToggle");
  const sidebar = document.getElementById("sidebar");
  if (toggle && sidebar) {
    toggle.addEventListener("click", () => sidebar.classList.toggle("open"));
    document.addEventListener("click", (event) => {
      if (window.innerWidth <= 850 && sidebar.classList.contains("open") &&
          !sidebar.contains(event.target) && !toggle.contains(event.target)) sidebar.classList.remove("open");
    });
  }
  document.querySelectorAll("[data-range-sync]").forEach((range) => {
    const row = range.closest(".skill-input-row");
    const number = row ? row.querySelector("[data-score-input]") : null;
    if (!number) return;
    range.addEventListener("input", () => { number.value = range.value; });
    number.addEventListener("input", () => {
      const n = Number(number.value);
      if (number.value !== "" && Number.isFinite(n)) range.value = Math.max(0, Math.min(100, n));
    });
  });
  document.querySelectorAll(".flash").forEach((flash) => {
    window.setTimeout(() => { if (flash.isConnected) flash.style.opacity = "0.98"; }, 4500);
  });
});
