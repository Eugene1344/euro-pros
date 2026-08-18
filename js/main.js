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

(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  if (!toggle || !nav) return;

  var NAV_BREAKPOINT = 1125;

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

/* FAQ accordion */
(function () {
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var question = item.querySelector(".faq-item__question");
    var answer = item.querySelector(".faq-item__answer");
    if (!question || !answer) return;

    question.addEventListener("click", function () {
      var isOpen = item.classList.contains("is-open");
      document.querySelectorAll(".faq-item.is-open").forEach(function (openItem) {
        if (openItem !== item) {
          openItem.classList.remove("is-open");
          openItem.querySelector(".faq-item__answer").style.maxHeight = null;
        }
      });
      if (isOpen) {
        item.classList.remove("is-open");
        answer.style.maxHeight = null;
      } else {
        item.classList.add("is-open");
        answer.style.maxHeight = answer.scrollHeight + "px";
      }
    });
  });
})();

/* Filter tabs: client-side show/hide of cards by data-category */
(function () {
  document.querySelectorAll("[data-filter-group]").forEach(function (group) {
    var groupName = group.getAttribute("data-filter-group");
    var tabs = group.querySelectorAll("[data-filter]");
    var cards = document.querySelectorAll('[data-category][data-filter-target="' + groupName + '"]');

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function (event) {
        event.preventDefault();
        var value = tab.getAttribute("data-filter");

        tabs.forEach(function (t) {
          t.classList.remove("is-active");
        });
        tab.classList.add("is-active");

        cards.forEach(function (card) {
          var show = value === "all" || card.getAttribute("data-category") === value;
          card.style.display = show ? "" : "none";
        });
      });
    });
  });
})();

/* Team block: scroll the service tag strip with the prev/next arrows */
(function () {
  var track = document.querySelector(".team-block__tags-track");
  if (!track) return;

  document.querySelectorAll(".team-block__arrow").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var dir = Number(btn.getAttribute("data-scroll")) || 1;
      track.scrollBy({ left: dir * 220, behavior: "smooth" });
    });
  });
})();

/* Review carousel: scroll one card at a time with the prev/next arrows,
   wrapping around at either end for an infinite loop feel. */
(function () {
  var track = document.querySelector(".review-carousel__track");
  if (!track) return;

  var WRAP_TOLERANCE = 4;

  document.querySelectorAll(".review-carousel__arrow").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var dir = Number(btn.getAttribute("data-scroll")) || 1;
      var card = track.querySelector(".review-card");
      var step = card ? card.getBoundingClientRect().width + 24 : 360;
      var maxScroll = track.scrollWidth - track.clientWidth;

      if (dir > 0 && track.scrollLeft >= maxScroll - WRAP_TOLERANCE) {
        // Scroll-snap fights a smooth scrollTo back to the start, so jump.
        track.scrollTo({ left: 0, behavior: "instant" });
      } else if (dir < 0 && track.scrollLeft <= WRAP_TOLERANCE) {
        track.scrollTo({ left: maxScroll, behavior: "instant" });
      } else {
        track.scrollBy({ left: dir * step, behavior: "smooth" });
      }
    });
  });
})();

/* Team cards: fade/rise into view, staggered */
(function () {
  var cards = document.querySelectorAll(".team-card");
  if (!cards.length || !("IntersectionObserver" in window)) {
    cards.forEach(function (c) { c.classList.add("is-visible"); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var index = Array.prototype.indexOf.call(cards, entry.target);
        setTimeout(function () {
          entry.target.classList.add("is-visible");
        }, index * 120);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });

  cards.forEach(function (c) {
    observer.observe(c);
  });
})();

/* Generic scroll-reveal: fade/rise, staggered per parent, for cards and
   list items across every page. (Team cards use their own pass above.) */
(function () {
  if (!("IntersectionObserver" in window)) return;

  var SELECTORS = [
    ".service-tile",
    ".project-card",
    ".blog-card",
    ".blog-featured",
    ".icon-list__item",
    ".feature-grid__item",
    ".process-step",
    ".process-row",
    ".value-prop",
    ".pricing-card",
    ".stats-bar__item",
    ".portfolio-strip__item",
    ".review-carousel",
    ".review-widget",
    ".faq-item",
    ".step-list__item",
    ".why-list > li",
    ".checklist > li",
    ".gallery-grid > img",
    ".challenge-solution",
    ".before-after__item",
    ".team-hero",
    ".experience-full__content"
  ].join(",");

  var els = Array.prototype.filter.call(
    document.querySelectorAll(SELECTORS),
    function (el) { return !el.closest(".team-card"); }
  );
  if (!els.length) return;

  els.forEach(function (el) {
    el.classList.add("reveal");
  });

  var staggerIndex = new WeakMap();
  function nextStagger(parent) {
    var n = staggerIndex.get(parent) || 0;
    staggerIndex.set(parent, n + 1);
    return n;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var idx = nextStagger(entry.target.parentElement);
      var delay = Math.min(idx * 70, 350);
      setTimeout(function () {
        entry.target.classList.add("is-visible");
      }, delay);
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -60px 0px" });

  els.forEach(function (el) {
    observer.observe(el);
  });
})();

/* Animated count-up numbers (trust bar) */
(function () {
  var nums = document.querySelectorAll("[data-count-to]");
  if (!nums.length || !("IntersectionObserver" in window)) return;

  function animate(el) {
    var target = parseFloat(el.getAttribute("data-count-to"));
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
    var duration = 1200;
    var start = Date.now();

    // Time-based (not requestAnimationFrame-based) so it still completes
    // correctly even if the tab is backgrounded/throttled mid-animation.
    var timer = setInterval(function () {
      var progress = Math.min((Date.now() - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      var val = target * eased;
      el.textContent = decimals ? val.toFixed(decimals) : Math.round(val);
      if (progress >= 1) {
        clearInterval(timer);
        el.textContent = decimals ? target.toFixed(decimals) : target;
      }
    }, 30);
  }

  var seen = new WeakSet();
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting && !seen.has(entry.target)) {
        seen.add(entry.target);
        animate(entry.target);
      }
    });
  }, { threshold: 0.4 });

  nums.forEach(function (n) {
    observer.observe(n);
  });
})();

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

  function show() {
    if (shown || Date.now() - loadedAt < minTimeMs) return;
    shown = true;
    try { sessionStorage.setItem(STORAGE_KEY, "1"); } catch (e) {}
    overlay.classList.add("is-open");
    document.body.style.overflow = "hidden";
  }

  function hide() {
    overlay.classList.remove("is-open");
    document.body.style.overflow = "";
  }

  overlay.querySelector(".exit-popup__close").addEventListener("click", hide);
  overlay.addEventListener("click", function (e) {
    if (e.target === overlay) hide();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") hide();
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

/* Contact form: static demo submit (no backend) */
(function () {
  var form = document.querySelector(".project-form");
  if (!form) return;

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var success = document.querySelector(".form-success");
    form.style.display = "none";
    if (success) success.classList.add("is-visible");
    success && success.scrollIntoView({ behavior: "smooth", block: "start" });
  });
})();
