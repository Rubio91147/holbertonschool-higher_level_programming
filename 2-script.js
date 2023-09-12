const setColor = document.body.querySelector("#red_header");
setColor.addEventListener("click", () => {
    const head = document.body.querySelector("header");
    head.className = "red";
});
