const button = document.querySelectorAll(".btn-toggle")
console.log(button)

button.forEach(button => {
    button.addEventListener("click", () => {
        const targetId = button.dataset.target
        const div = document.getElementById(targetId)

        if (div.style.display == "block"){
            div.style.display = "none"
            button.textContent = "Mostrar"
        } else {
            div.style.display = "block"
            button.textContent = "Esconder"
        }
    })
})