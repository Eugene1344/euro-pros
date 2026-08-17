/* Reviews carousel, powered by Swiper (see vendor/swiper) */
(function () {
  var el = document.querySelector(".reviews-swiper");
  if (!el || typeof Swiper === "undefined") return;

  new Swiper(el, {
    slidesPerView: "auto",
    spaceBetween: 24,
    a11y: {
      enabled: true,
      prevSlideMessage: "Previous review",
      nextSlideMessage: "Next review",
      slideLabelMessage: "Review {{index}} of {{slidesLength}}",
    },
    keyboard: { enabled: true },
    navigation: {
      prevEl: ".reviews-carousel__arrow--prev",
      nextEl: ".reviews-carousel__arrow--next",
    },
    pagination: {
      el: ".reviews-swiper-pagination",
      clickable: true,
    },
  });
})();
