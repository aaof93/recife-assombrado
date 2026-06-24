from pathlib import Path

import pygame

from config import LARGURA_TELA, ALTURA_TELA


class Cenario:
    def __init__(self, nome_imagem):
        self.nome_imagem = nome_imagem
        self.imagem = self.carregar_imagem()

    def carregar_imagem(self):
        caminho_imagem = (
            Path(__file__).resolve().parent
            / "assets"
            / self.nome_imagem
        )

        if not caminho_imagem.exists():
            raise FileNotFoundError(
                f"Imagem do cenário não encontrada em: {caminho_imagem}"
            )

        imagem_original = pygame.image.load(
            str(caminho_imagem)
        ).convert()

        imagem_redimensionada = pygame.transform.scale(
            imagem_original,
            (LARGURA_TELA, ALTURA_TELA)
        )

        return imagem_redimensionada

    def trocar_imagem(self, nome_imagem):
        self.nome_imagem = nome_imagem
        self.imagem = self.carregar_imagem()

    def desenhar(self, tela):
        tela.blit(self.imagem, (0, 0))