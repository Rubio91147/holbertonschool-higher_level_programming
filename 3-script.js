
const setColor = document.body.querySelector("#toggle_header");
setColor.addEventListener("click", () => {
    const head = document.body.querySelector("header");
    head.className === 'red' ? head.className = 'green': head.className = 'red';
});
