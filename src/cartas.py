from armas import SombrinhaGiratoria


class CartaAprimoramento:
    def __init__(self, titulo, descricao, tipo):
        self.titulo = titulo
        self.descricao = descricao
        self.tipo = tipo

    def aplicar(self, jogador, armas):
        if self.tipo == "velocidade":
            jogador.aumentar_velocidade()

        elif self.tipo == "vida_maxima":
            jogador.aumentar_vida_maxima()

        elif self.tipo == "cura":
            jogador.recuperar_vida()

        elif self.tipo == "dano":
            for arma in armas:
                arma.aumentar_dano()

        elif self.tipo == "cooldown":
            for arma in armas:
                arma.reduzir_cooldown()

        elif self.tipo == "alcance_sombrinha":
            for arma in armas:
                if isinstance(arma, SombrinhaGiratoria):
                    arma.aumentar_alcance()


def criar_baralho_de_aprimoramentos():
    cartas = [
        CartaAprimoramento(
            "Passos de Frevo",
            "+1 velocidade de movimento",
            "velocidade"
        ),
        CartaAprimoramento(
            "Bolo de Rolo Reforçado",
            "+20 de vida máxima",
            "vida_maxima"
        ),
        CartaAprimoramento(
            "Caldo de Cana Milagroso",
            "Recupera 30 de vida",
            "cura"
        ),
        CartaAprimoramento(
            "Força do Caboclo",
            "+5 de dano nas armas",
            "dano"
        ),
        CartaAprimoramento(
            "Ritmo do Maracatu",
            "Reduz cooldown das armas",
            "cooldown"
        ),
        CartaAprimoramento(
            "Sombrinha Aberta",
            "+ Alcance da sombrinha",
            "alcance_sombrinha"
        )
    ]

    return cartas