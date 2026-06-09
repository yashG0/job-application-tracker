document.addEventListener("click", (event) => {
  if (!event.target.closest(".filter-bar button")) {
    return;
  }

  document
    .querySelectorAll(".filter-bar button")
    .forEach((btn) => btn.classList.remove("active"));

  event.target.classList.add("active");
});
