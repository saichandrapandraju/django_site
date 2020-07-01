new fullpage("#fullpage", {
  autoScrolling: true,
  navigation: true,
  onLeave: (origin, destination, direction) => {
    const section = destination.item;
    const title = section.querySelector("h1");
    const tl = new TimelineMax({ delay: 0.5 });
    tl.fromTo(title, 0.5, { y: "50", opacity: 0 }, { y: 0, opacity: 1 });
    if (destination.index === 1) {
      const face = document.querySelectorAll(".face");
      const description = document.querySelector(".description");

      tl.fromTo(face, 0.7, { x: "150%" }, { x: "-35%" }).fromTo(
        description,
        0.5,
        { y: "50", opacity: 0 },
        { y: 0, opacity: 1 }
      );
    }
  },
});
