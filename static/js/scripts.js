// console.log('inside scripts.js')
// document.addEventListener("DOMContentLoaded", function () {
//   const container = document.getElementById("carousel-container");
//   const prevBtn1 = document.getElementById("prevBtn");
//   const Btn = document.getElementById("nextBtn");

//   let index = 0;
//   const item = container.querySelector(".flex-shrink-0");
//   if (item != null) {
//     let itemWidth = item.offsetWidth;
//     const totalItems = container.children.length;

//     function updateCarousel() {
//       container.style.transform = `translateX(-${index * itemWidth}px)`;
//     }

//     prevBtn1.addEventListener("click", () => {
//       index = index > 0 ? index - 1 : totalItems - 1;
//       updateCarousel();
//     });

//     Btn.addEventListener("click", () => {
//       index = index < totalItems - 1 ? index + 1 : 0;
//       updateCarousel();
//     });
//   }
// });

// const container = document.getElementById("carousel-container");
// const prevBtn = document.getElementById('prevBtn');
// const nextBtn = document.getElementById('nextBtn');
// const items = container.children.length;
// let currentIndex = 0;

// function updateCarousel() {
//   const itemWidth = container.children[0].offsetWidth;
//   const offset = -currentIndex * itemWidth;
//   container.style.transform = `translateX(${offset}px)`;
// }

// nextBtn.addEventListener("click", () => {
//   if (currentIndex < items - 1) {
//     currentIndex++;
//     updateCarousel();
//   }
// });

// prevBtn.addEventListener("click", () => {
//   if (currentIndex > 0) {
//     currentIndex--;
//     updateCarousel();
//   }
// });

window.addEventListener("resize", updateCarousel);

document
  .getElementById("toggle-departments")
  .addEventListener("click", function () {
    console.log("clicked");
    var departmentList = document.getElementById("departments-list");
    var chevronIcon = document.getElementById("chevron-icon");

    departmentList.classList.toggle("hidden");

    if (chevronIcon.classList.contains("fa-chevron-down")) {
      chevronIcon.classList.remove("fa-chevron-down");
      chevronIcon.classList.add("fa-chevron-up");
    } else {
      chevronIcon.classList.remove("fa-chevron-up");
      chevronIcon.classList.add("fa-chevron-down");
    }
  });

const carouselContainer = document.getElementById("carousel-container");
const prevBtn2 = document.getElementById("prevBtn");
const nextBtn1 = document.getElementById("nextBtn");

let scrollAmount = 0;
const itemWidth = carouselContainer.querySelector("div").offsetWidth + 16;

// Next Button Click
nextBtn1.addEventListener("click", () => {
  scrollAmount += itemWidth;
  carouselContainer.style.transform = `translateX(-${scrollAmount}px)`;

  // Prevent over-scrolling
  if (
    scrollAmount >=
    carouselContainer.scrollWidth - carouselContainer.clientWidth
  ) {
    scrollAmount =
      carouselContainer.scrollWidth - carouselContainer.clientWidth;
  }
});

// Prev Button Click
prevBtn2.addEventListener("click", () => {
  scrollAmount -= itemWidth;
  if (scrollAmount < 0) scrollAmount = 0;
  carouselContainer.style.transform = `translateX(-${scrollAmount}px)`;
});


// Search functionality
document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.getElementById("search-form");
  const searchInput = document.getElementById("search-input");
  const searchButton = document.getElementById("search-button");

  searchForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const query = searchInput.value.trim();
    if (query) {
      // Redirect to search page with query parameter
      window.location.href = `/search?query=${encodeURIComponent(query)}`;
    } else {
      alert("Please enter a search term");
    }
  });

  searchButton.addEventListener("click", function () {
    searchForm.submit();
  });
});



