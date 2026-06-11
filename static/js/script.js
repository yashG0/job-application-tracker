const root = document.documentElement;
const themeToggle = document.querySelector("[data-theme-toggle]");
const themeIcon = document.querySelector("[data-theme-icon]");
const storedTheme = localStorage.getItem("theme");
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

function applyTheme(theme) {
  root.dataset.theme = theme;

  if (!themeToggle || !themeIcon) {
    return;
  }

  const isDark = theme === "dark";
  themeToggle.setAttribute("aria-pressed", String(isDark));
  themeToggle.setAttribute(
    "aria-label",
    isDark ? "Switch to light mode" : "Switch to dark mode",
  );
  themeIcon.textContent = isDark ? "Light" : "Dark";
}

applyTheme(storedTheme || (prefersDark ? "dark" : "light"));

themeToggle?.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
  localStorage.setItem("theme", nextTheme);
  applyTheme(nextTheme);
});

function setActiveNavigation() {
  const path = window.location.pathname;

  document.querySelectorAll("[data-nav-link]").forEach((link) => {
    const section = link.dataset.navLink;
    const isActive =
      (section === "dashboard" && path.includes("/dashboard")) ||
      (section === "applications" && path.includes("/application"));

    link.classList.toggle("active", isActive);
    if (isActive) {
      link.setAttribute("aria-current", "page");
    } else {
      link.removeAttribute("aria-current");
    }
  });
}

function showNotification(message, type = "success") {
  const region = document.getElementById("notification-region");

  if (!region) {
    return;
  }

  region.innerHTML = `
    <div class="alert alert-${type}" role="alert">
      <span>${type === "success" ? "Success:" : "Error:"}</span>
      <span>${message}</span>
    </div>
  `;

  window.setTimeout(() => {
    region.innerHTML = "";
  }, 3500);
}

document.addEventListener("click", (event) => {
  const filterButton = event.target.closest(".filter-bar button");

  if (!filterButton) {
    return;
  }

  document.querySelectorAll(".filter-bar button").forEach((button) => {
    const isActive = button === filterButton;
    button.classList.toggle("active", isActive);
    button.setAttribute("aria-pressed", String(isActive));
  });
});

document.body.addEventListener("htmx:afterRequest", (event) => {
  const source = event.detail.elt;

  if (source?.id !== "application-create-form") {
    return;
  }

  if (event.detail.successful) {
    source.reset();
    showNotification("Application created successfully.", "success");
    return;
  }

  showNotification("Something went wrong. Please check the form and try again.", "error");
});

setActiveNavigation();
