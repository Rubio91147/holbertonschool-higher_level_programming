
const update_header = document.body.querySelector("#update_header");
const header = document.body.querySelector("header");

update_header.addEventListener("click", () => {
    header.textContent = "New Header!!!";
});
