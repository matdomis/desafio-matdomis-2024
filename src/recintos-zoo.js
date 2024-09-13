import { animaisCarnivoros, animaisPermitidos } from "./animais-permitidos";
import { recintosIniciais } from "./recintos-iniciais";
import { mapaDeErros } from "./erros";
import { formataMensagemRecinto } from './formata-mensagem-recinto';

class RecintosZoo {
	constructor() {
		this.recintos = recintosIniciais;
		this.animais = animaisPermitidos;
	}

	analisaRecintos(animal, quantidade) {
		if (!this.animais[animal]) return mapaDeErros.animalInvalido;

		if (quantidade <= 0) return mapaDeErros.quantidadeInvalida;

		const especieInfo = this.animais[animal];
		const recintosViaveis = [];

		this.recintos.forEach((recinto) => {
			const oBiomaEhCompativel = recinto.bioma.some((bioma) =>
				especieInfo.biomas.includes(bioma),
			);

			if (!oBiomaEhCompativel) return;

			const animaisNoRecinto = recinto.animais;

			let totalEspacoOcupado = 0;
			let carnivorosNoRecinto = false;
			let existeOutraEspecie = false;

			animaisNoRecinto.forEach((animalRecinto) => {
				const infoAnimalRecinto = this.animais[animalRecinto.especie];

				totalEspacoOcupado += infoAnimalRecinto.tamanho * animalRecinto.quantidade;

				if (infoAnimalRecinto.carnivoro) carnivorosNoRecinto = true;

				if (animalRecinto.especie !== animal) existeOutraEspecie = true;
			});

			const especieJuntoComCarnivoro = especieInfo.carnivoro &&
				(carnivorosNoRecinto || existeOutraEspecie)

			if (especieJuntoComCarnivoro) return

			let espacoNecessario = especieInfo.tamanho * quantidade;

			if (animaisNoRecinto.length > 0) {
				espacoNecessario += 1;

				if (recinto.animais.some((animal) => animal.especie === "MACACO")) {
					espacoNecessario -= 1;
				}

				const temCarnivoroComMacaco = recinto.animais.some((animal) => animaisCarnivoros.includes(animal.especie))

				if (temCarnivoroComMacaco) return;
			}

			const ehMacaco = animal === "MACACO"
			const ehHipopotamo = animal === "HIPOPOTAMO"

			if (
				ehHipopotamo &&
				(!recinto.bioma.includes("savana") || !recinto.bioma.includes("rio"))
			) {
				return;
			}

			if (
				ehMacaco &&
				quantidade === 1 &&
				animaisNoRecinto.length === 0
			) {
				return;
			}

			const espacoLivre = recinto.tamanho - totalEspacoOcupado;

			if (espacoLivre >= espacoNecessario) {
				recintosViaveis.push({
					numero: recinto.numero,
					espacoLivre: espacoLivre - espacoNecessario,
					espacoTotal: recinto.tamanho,
				});
			}
		});

		recintosViaveis.sort((a, b) => a.numero - b.numero);

		if (recintosViaveis.length === 0) {
			return mapaDeErros.semRecinto;
		}

		return {
			recintosViaveis: recintosViaveis.map(
				(recinto) => formataMensagemRecinto(recinto.numero, recinto.espacoLivre, recinto.espacoTotal)
			),
		};
	}
}

export { RecintosZoo as RecintosZoo };
