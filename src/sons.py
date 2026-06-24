from pathlib import Path

import pygame


class GerenciadorDeSons:
    def __init__(self):
        self.efeitos_cache = {}

        pygame.mixer.init()

        self.pasta_assets = (
            Path(__file__).resolve().parent
            / "assets"
        )

    def carregar_musica(self, nome_arquivo):
        caminho = self.pasta_assets / nome_arquivo

        if not caminho.exists():
            raise FileNotFoundError(
                f"Música não encontrada em: {caminho}"
            )

        pygame.mixer.music.load(str(caminho))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def carregar_musica_menu(self):
        self.carregar_musica("a_praieira.mp3")

    def carregar_musica_gameplay(self):
        self.carregar_musica("da_lama_ao_caos_estilo.mp3")

    def carregar_musica_rua_bom_jesus(self):
        self.carregar_musica("intro_sob_pe.mp3")

    def gameover(self):
        pygame.mixer.music.stop()