// const navSlide = () => {
//   const burger = document.querySelector(".burger");
//   const nav = document.querySelector(".nav-links");
//   const navLinks = document.querySelectorAll(".nav-links li");

//   burger.addEventListener("click", () => {
//     //Toggle Nav
//     nav.classList.toggle("nav-active");

//     // Animate Links
//     navLinks.forEach((link, index) => {
//       if (link.style.animation) {
//         link.style.animation = "";
//       } else {
//         link.style.animation = `navLinkFade 0.5s ease forwards ${
//           index / 7 + 0.3
//         }s`;
//       }
//     });

//     //burger animation
//     burger.classList.toggle("toggle");
//   });
// };

// navSlide();

const main = document.querySelector(".main");
const slider = document.querySelector(".slider");
const logo = document.querySelector(".logo");
const headline = document.querySelector(".headline");
const navLinks = document.querySelectorAll(".nav-links li");
const nav = document.querySelector(".nav-links");

const tl = new TimelineMax();
tl.fromTo(main, 1, { height: "0%" }, { height: "80%", ease: Power2.easeinOut })
  .fromTo(
    main,
    1.2,
    { width: "100%" },
    { width: "80%", ease: Power2.easeinOut }
  )
  .fromTo(
    slider,
    1.2,
    { x: "-100%" },
    { x: "0%", ease: Power2.easeinOut },
    "-=1.2"
  )
  .fromTo(logo, 0.5, { opacity: 0, x: 30 }, { opacity: 1, x: 0 }, "-=0.5")
  .fromTo(nav, 0.5, { opacity: 0, x: 30 }, { opacity: 1, x: 0 }, "-=0.5")
  .fromTo(navLinks, 0.5, { opacity: 0, x: 30 }, { opacity: 1, x: 0 }, "-=0.5")
  .fromTo(headline, 0.5, { opacity: 0, x: 30 }, { opacity: 1, x: 0 }, "-=0.3");
