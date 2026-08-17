/* Exit-intent popup */
(function () {
  var overlay = document.getElementById("exitPopupOverlay");
  if (!overlay) return;

  var STORAGE_KEY = "epExitPopupShown";
  if (sessionStorage.getItem(STORAGE_KEY)) return;

  var shown = false;
  var loadedAt = Date.now();
  var minTimeMs = 6000;
  var maxScroll = 0;
  var lastFocused = null;

  function show() {
    if (shown || Date.now() - loadedAt < minTimeMs) return;
    shown = true;
    try { sessionStorage.setItem(STORAGE_KEY, "1"); } catch (e) {}
    lastFocused = document.activeElement;
    overlay.classList.add("is-open");
    document.body.style.overflow = "hidden";
    var closeBtn = overlay.querySelector(".exit-popup__close");
    if (closeBtn) closeBtn.focus();
  }

  function hide() {
    overlay.classList.remove("is-open");
    document.body.style.overflow = "";
    if (lastFocused && typeof lastFocused.focus === "function") lastFocused.focus();
  }

  overlay.querySelector(".exit-popup__close").addEventListener("click", hide);
  overlay.addEventListener("click", function (e) {
    if (e.target === overlay) hide();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && overlay.classList.contains("is-open")) hide();
  });

  // Desktop: cursor exits through the top of the viewport
  document.addEventListener("mouseout", function (e) {
    if (!e.relatedTarget && e.clientY <= 0) show();
  });

  // Any device: scrolled down significantly, then jumped back near the top
  window.addEventListener("scroll", function () {
    maxScroll = Math.max(maxScroll, window.scrollY);
    if (maxScroll > 700 && window.scrollY < 100) show();
  }, { passive: true });

  // Fallback so engaged visitors still see it once
  setTimeout(show, 45000);
})();
