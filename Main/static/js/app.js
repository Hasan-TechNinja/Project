// document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById("carousel-container");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");

  let index = 0;
  const item = container.querySelector(".flex-shrink-0");
  if (item != null) {
    let itemWidth = item.offsetWidth;
    const totalItems = container.children.length;

    function updateCarousel() {
      container.style.transform = `translateX(-${index * itemWidth}px)`;
    }

    prevBtn.addEventListener("click", () => {
      index = index > 0 ? index - 1 : totalItems - 1;
      updateCarousel();
    });

    nextBtn.addEventListener("click", () => {
      index = index < totalItems - 1 ? index + 1 : 0;
      updateCarousel();
    });
  }
// });
