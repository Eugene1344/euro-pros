/* Mobile nav toggle */
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  if (!toggle || !nav) return;

  var NAV_BREAKPOINT = 1280;

  function closeNav() {
    nav.classList.remove("is-open");
    toggle.classList.remove("is-active");
    toggle.setAttribute("aria-expanded", "false");
  }

  function openNav() {
    nav.classList.add("is-open");
    toggle.classList.add("is-active");
    toggle.setAttribute("aria-expanded", "true");
  }

  toggle.addEventListener("click", function () {
    if (nav.classList.contains("is-open")) {
      closeNav();
    } else {
      openNav();
    }
  });

  nav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", closeNav);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeNav();
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > NAV_BREAKPOINT) closeNav();
  });
})();

/* Dark/light theme toggle */
(function () {
  var btn = document.querySelector(".theme-toggle");
  if (!btn) return;

  var STORAGE_KEY = "epTheme";
  var root = document.documentElement;

  function apply(theme) {
    root.setAttribute("data-theme", theme);
    btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    btn.setAttribute("aria-label", theme === "dark" ? "Switch to light theme" : "Switch to dark theme");
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (e) {}
  }

  // Sync the button's a11y state with whatever the inline head script
  // already applied (it runs before paint to avoid a flash of the
  // wrong theme); default to light if nothing was set.
  apply(root.getAttribute("data-theme") === "dark" ? "dark" : "light");

  btn.addEventListener("click", function () {
    apply(root.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });
})();
