import pygame
import os

from config import COR_ALMA, COR_BOLO, COR_MASCARA, COR_BRANCA


class AlmaCapibaribe:
    imagem_cache = None

    def __init__(self, x, y, valor_xp):
        self.x = x
        self.y = y

        self.largura = 28
        self.altura = 28
        self.valor_xp = valor_xp
        self.cor = COR_ALMA

        self.imagem = self.carregar_imagem()

    def carregar_imagem(self):
        if AlmaCapibaribe.imagem_cache is not None:
            return AlmaCapibaribe.imagem_cache

        pasta_atual = os.path.dirname(__file__)
        caminho = os.path.join(pasta_atual, "assets", "alma.png")

        try:
            imagem = pygame.image.load(caminho)
            imagem = imagem.convert_alpha()
            imagem = pygame.transform.scale(imagem,(self.largura, self.altura))

            AlmaCapibaribe.imagem_cache = imagem
            return imagem

        except FileNotFoundError:
            return None

    def obter_retangulo(self):
        return pygame.Rect(
            self.x - self.largura / 2,
            self.y - self.altura / 2,
            self.largura,
            self.altura
        )

    def desenhar(self, tela):
        if self.imagem is not None:
            tela.blit(self.imagem,
                (
                    self.x - self.largura / 2,
                    self.y - self.altura / 2
                )
            )
        else:
            #pygame.draw.circle(superfície, cor, centro, raio, espessura)
            pygame.draw.circle(tela,self.cor,
                (int(self.x), int(self.y)), 8,0)


class BoloDeRolo:
    imagem_cache = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.largura = 40
        self.altura = 40
        self.cura = 25
        self.cor = COR_BOLO

        self.imagem = self.carregar_imagem()

    def carregar_imagem(self):
        if BoloDeRolo.imagem_cache is not None:
            return BoloDeRolo.imagem_cache

        pasta_atual = os.path.dirname(__file__)
        caminho = os.path.join(pasta_atual, "assets", "bolo.png")

        try:
            imagem = pygame.image.load(caminho)
            imagem = imagem.convert_alpha()
            imagem = pygame.transform.scale(
                imagem,
                (self.largura, self.altura)
            )

            BoloDeRolo.imagem_cache = imagem
            return imagem

        except FileNotFoundError:
            return None

    def obter_retangulo(self):
        return pygame.Rect(
            self.x - self.largura / 2,
            self.y - self.altura / 2,
            self.largura,
            self.altura
        )

    def desenhar(self, tela):
        if self.imagem is not None:
            tela.blit(
                self.imagem,
                (
                    self.x - self.largura / 2,
                    self.y - self.altura / 2
                )
            )
        else:
            pygame.draw.circle(
                tela,
                self.cor,
                (int(self.x), int(self.y)),
                10
            )


class MascaraPapangu:
    imagem_cache = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.largura = 55
        self.altura = 60
        self.cor = COR_MASCARA

        self.imagem = self.carregar_imagem()

    def carregar_imagem(self):
        if MascaraPapangu.imagem_cache is not None:
            return MascaraPapangu.imagem_cache

        pasta_atual = os.path.dirname(__file__)
        caminho = os.path.join(pasta_atual, "assets", "mascara.png")

        try:
            imagem = pygame.image.load(caminho)
            imagem = imagem.convert_alpha()
            imagem = pygame.transform.scale(
                imagem,
                (self.largura, self.altura)
            )

            MascaraPapangu.imagem_cache = imagem
            return imagem

        except FileNotFoundError:
            return None

    def obter_retangulo(self):
        return pygame.Rect(
            self.x - self.largura / 2,
            self.y - self.altura / 2,
            self.largura,
            self.altura
        )

    def desenhar(self, tela):
        if self.imagem is not None:
            tela.blit(
                self.imagem,
                (
                    self.x - self.largura / 2,
                    self.y - self.altura / 2
                )
            )
        else:
            pygame.draw.circle(
                tela,
                self.cor,
                (int(self.x), int(self.y)),
                12
            )

            pygame.draw.circle(
                tela,
                COR_BRANCA,
                (int(self.x - 4), int(self.y - 3)),
                2
            )

            pygame.draw.circle(
                tela,
                COR_BRANCA,
                (int(self.x + 4), int(self.y - 3)),
                2
            )