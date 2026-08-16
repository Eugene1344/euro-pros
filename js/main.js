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
