const updateButons = document.querySelectorAll(".update")
const divUpdate = document.getElementById("divUpdate")

updateButons.forEach(button => {
    button.addEventListener("click", () => {
        if (divUpdate.style.display == "none"){
            divUpdate.style.display = "block"
        } else {
            divUpdate.style.display = "none"
        }
    })
});
