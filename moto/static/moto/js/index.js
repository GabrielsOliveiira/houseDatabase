const kmsInput = document.getElementById("kmsInput")
const oldKmsInput = document.getElementById("oldKms")

const calcButton = document.getElementById("calcButton")

const oilResult = document.getElementById("oilResult")

calcButton.addEventListener("click", () => {
    const currentKms = Number(kmsInput.value)
    const oldKms = Number(oldKmsInput.dataset.kms)

    if (currentKms < oldKms) {
        oilResult.textContent = "A quilometragem atual não pode ser menor que a da última troca."
        return
    }


    if (currentKms - oldKms >= 1500){
    oilResult.textContent = "Troque o óleo"
    } else {
        oilResult.textContent = `Você ainda pode andar ${Math.abs(currentKms - oldKms - 1500)} kms`
    }
})