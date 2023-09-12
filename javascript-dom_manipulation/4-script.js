
const add_item = document.body.querySelector("#add_item");
const my_list = document.body.querySelector(".my_list");

add_item.addEventListener("click", () => {
    const li = document.createElement("li");
    li.textContent = "Item";
    my_list.appendChild(li);
});
