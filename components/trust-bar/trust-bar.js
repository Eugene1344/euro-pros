/* Animated count-up numbers (trust bar) */
(function () {
  var nums = document.querySelectorAll("[data-count-to]");
  if (!nums.length) return;

  function setFinal(el) {
    var target = parseFloat(el.getAttribute("data-count-to"));
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
    el.textContent = decimals ? target.toFixed(decimals) : target;
  }

  if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    nums.forEach(setFinal);
    return;
  }

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
        setFinal(el);
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
