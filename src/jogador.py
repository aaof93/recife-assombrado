from pathlib import Path

import pygame

from config import COR_JOGADOR


class Jogador:
    imagens_cache = {}

    def __init__(self, x, y, personagem):
        self.x = x
        self.y = y

        self.personagem = personagem

        self.largura = 100
        self.altura = 115
        self.cor = COR_JOGADOR

        self.velocidade = 5

        if self.personagem == "frevo":
            self.velocidade = 6
            self.vida_maxima = 90

        elif self.personagem == "caboclo":
            self.velocidade = 4
            self.vida_maxima = 130

        else:
            self.velocidade = 5
            self.vida_maxima = 100

        self.vida_atual = self.vida_maxima

        self.nivel = 1
        self.xp_atual = 0
        self.xp_para_proximo_nivel = 50

        self.tempo_ultimo_dano = 0
        self.intervalo_dano = 1000

        self.olhando_para_direita = True

        self.imagem_direita = self.carregar_imagem("direita")
        self.imagem_esquerda = self.carregar_imagem("esquerda")

    def carregar_imagem(self, lado):
        chave_cache = f"{self.personagem}_{lado}"

        if chave_cache in Jogador.imagens_cache:
            return Jogador.imagens_cache[chave_cache]

        nome_arquivo = f"{self.personagem}_{lado}.png"

        caminho_imagem = (
            Path(__file__).resolve().parent
            / "assets"
            / nome_arquivo
        )

        if not caminho_imagem.exists():
            return None

        imagem = pygame.image.load(
            str(caminho_imagem)
        ).convert_alpha()

        imagem = pygame.transform.scale(
            imagem,
            (self.largura, self.altura)
        )

        Jogador.imagens_cache[chave_cache] = imagem

        return imagem

    def atualizar_direcao_pelo_mouse(self):
        centro_x, centro_y = self.obter_centro()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_x >= centro_x:
            self.olhando_para_direita = True
        else:
            self.olhando_para_direita = False

    def mover(self, largura_tela, altura_tela):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w]:
            self.y -= self.velocidade

        if teclas[pygame.K_s]:
            self.y += self.velocidade

        if teclas[pygame.K_a]:
            self.x -= self.velocidade

        if teclas[pygame.K_d]:
            self.x += self.velocidade

        if self.x < 0:
            self.x = 0

        if self.x + self.largura > largura_tela:
            self.x = largura_tela - self.largura

        if self.y < 0:
            self.y = 0

        if self.y + self.altura > altura_tela:
            self.y = altura_tela - self.altura

        self.atualizar_direcao_pelo_mouse()

    def receber_dano(self, dano):
        tempo_atual = pygame.time.get_ticks()

        if tempo_atual - self.tempo_ultimo_dano >= self.intervalo_dano:
            self.vida_atual -= dano
            self.tempo_ultimo_dano = tempo_atual

            if self.vida_atual < 0:
                self.vida_atual = 0

    def ganhar_xp(self, quantidade):
        self.xp_atual += quantidade

        if self.xp_atual >= self.xp_para_proximo_nivel:
            self.subir_nivel()
            return True

        return False

    def subir_nivel(self):
        self.nivel += 1
        self.xp_atual = self.xp_atual - self.xp_para_proximo_nivel
        self.xp_para_proximo_nivel += 30

    def curar(self, quantidade):
        self.vida_atual += quantidade

        if self.vida_atual > self.vida_maxima:
            self.vida_atual = self.vida_maxima

    def aumentar_velocidade(self):
        self.velocidade += 1

    def aumentar_vida_maxima(self):
        self.vida_maxima += 20
        self.vida_atual += 20

        if self.vida_atual > self.vida_maxima:
            self.vida_atual = self.vida_maxima

    def recuperar_vida(self):
        self.curar(30)

    def obter_centro(self):
        centro_x = self.x + self.largura / 2
        centro_y = self.y + self.altura / 2

        return centro_x, centro_y

    def obter_retangulo(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )

    def desenhar(self, tela):
        imagem_atual = None

        if self.olhando_para_direita:
            imagem_atual = self.imagem_direita
        else:
            imagem_atual = self.imagem_esquerda

        if imagem_atual is not None:
            tela.blit(
                imagem_atual,
                (self.x, self.y)
            )

        else:
            pygame.draw.rect(
                tela,
                self.cor,
                self.obter_retangulo()
            )