const kmsInput = document.getElementById("kmsInput")
const oldKmsInput = document.getElementById("oldKms")

const calcButton = document.getElementById("calcButton")

const oilResult = document.getElementById("oilResult")

calcButton.addEventListener("click", async () => {
    const currentKms = Number(kmsInput.value);

    if (!kmsInput.value || !Number.isInteger(currentKms) || currentKms < 0) {
        oilResult.textContent = "Informe uma quilometragem válida.";
        return;
    }

    const url = new URL(
        calcButton.dataset.url,
        window.location.origin
    );

    url.searchParams.set("current_kms", currentKms);

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (!response.ok) {
            oilResult.textContent = data.error;
            return;
        }

        if (data.precisa_trocar) {
            oilResult.textContent = "Troque o óleo";
        } else {
            oilResult.textContent =
                `Você ainda pode andar ${data.kms_restantes} kms`;
        }
    } catch (error) {
        oilResult.textContent = "Erro ao calcular a troca de óleo.";
    }
});