const updateButons = document.querySelectorAll(".update")
const divUpdate = document.getElementById("divUpdate")
let ultimoId = null;

updateButons.forEach(button => {
    button.addEventListener("click", () => {

        let newId = button.getAttribute("data-id");

        if (divUpdate.style.display == "none"){
            divUpdate.style.display = "block"
            ultimoId = newId
        } else {
            console.log(ultimoId)
            if (ultimoId != newId){
                ultimoId = newId
                return
            }
            divUpdate.style.display = "none"
        }
    })
});

const update = document.getElementById("btnSave")

update.addEventListener("click", () => {
    let form = document.getElementById("formUpdate")
    form.action = `/moto/update/${form.getAttribute("data-type")}/${ultimoId}/`
    form.submit()
})
