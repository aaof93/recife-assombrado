import pygame
import math
import os

from config import COR_INIMIGO


class InimigoBase:
    def __init__(self, x, y, largura, altura, cor, velocidade, dano, vida, valor_xp):
        self.x = x
        self.y = y

        self.largura = largura
        self.altura = altura
        self.cor = cor

        self.velocidade = velocidade
        self.dano = dano
        self.vida = vida
        self.valor_xp = valor_xp

        self.eh_chefe = False

    def mover(self, jogador):
        diferenca_x = jogador.x - self.x
        diferenca_y = jogador.y - self.y

        distancia = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)

        if distancia != 0:
            direcao_x = diferenca_x / distancia
            direcao_y = diferenca_y / distancia

            self.x += direcao_x * self.velocidade
            self.y += direcao_y * self.velocidade

    def receber_dano(self, dano):
        self.vida -= dano

    def esta_morto(self):
        return self.vida <= 0

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

    def desenhar_barra_vida(self, tela):
        largura_barra = self.largura
        altura_barra = 5

        x_barra = self.x
        y_barra = self.y - 10

        vida_maxima_aproximada = 30

        if self.eh_chefe:
            vida_maxima_aproximada = 250
        elif isinstance(self, Emparedada):
            vida_maxima_aproximada = 45

        proporcao = self.vida / vida_maxima_aproximada

        if proporcao < 0:
            proporcao = 0

        largura_atual = largura_barra * proporcao

        pygame.draw.rect(
            tela,
            (60, 60, 60),
            (x_barra, y_barra, largura_barra, altura_barra)
        )

        pygame.draw.rect(
            tela,
            (0, 220, 0),
            (x_barra, y_barra, largura_atual, altura_barra)
        )

    def desenhar(self, tela):
        pygame.draw.rect(
            tela,
            self.cor,
            self.obter_retangulo()
        )

        self.desenhar_barra_vida(tela)


class PernaCabeluda(InimigoBase):
    imagem_direita_cache = None
    imagem_esquerda_cache = None

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            largura=75,
            altura=100,
            cor=COR_INIMIGO,
            velocidade=2.6,
            dano=10,
            vida=30,
            valor_xp=10
        )

        self.olhando_para_direita = True

        self.imagem_direita = self.carregar_imagem(
            "perna_cabeluda_direita.png",
            "direita"
        )

        self.imagem_esquerda = self.carregar_imagem(
            "perna_cabeluda_esquerda.png",
            "esquerda"
        )

    def carregar_imagem(self, nome_arquivo, lado):
        if lado == "direita" and PernaCabeluda.imagem_direita_cache is not None:
            return PernaCabeluda.imagem_direita_cache

        if lado == "esquerda" and PernaCabeluda.imagem_esquerda_cache is not None:
            return PernaCabeluda.imagem_esquerda_cache

        pasta_atual = os.path.dirname(__file__)
        caminho = os.path.join(pasta_atual, "assets", nome_arquivo)

        try:
            imagem = pygame.image.load(caminho)
            imagem = imagem.convert_alpha()
            imagem = pygame.transform.scale(
                imagem,
                (self.largura, self.altura)
            )

            if lado == "direita":
                PernaCabeluda.imagem_direita_cache = imagem
            else:
                PernaCabeluda.imagem_esquerda_cache = imagem

            return imagem

        except FileNotFoundError:
            return None

    def mover(self, jogador):
        if self.x > jogador.x:
            self.olhando_para_direita = False
        else:
            self.olhando_para_direita = True

        diferenca_x = jogador.x - self.x
        diferenca_y = jogador.y - self.y

        distancia = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)

        if distancia != 0:
            direcao_x = diferenca_x / distancia
            direcao_y = diferenca_y / distancia

            self.x += direcao_x * self.velocidade
            self.y += direcao_y * self.velocidade

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

        self.desenhar_barra_vida(tela)


class Emparedada(InimigoBase):
    imagem_direita_cache = None
    imagem_esquerda_cache = None

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            largura=85,
            altura=110,
            cor=(170, 170, 255),
            velocidade=1.8,
            dano=15,
            vida=45,
            valor_xp=15
        )

        self.tempo_criacao = pygame.time.get_ticks()
        self.amplitude = 40
        self.frequencia = 0.006

        self.olhando_para_direita = True

        self.imagem_direita = self.carregar_imagem(
            "emparedada_direita.png",
            "direita"
        )

        self.imagem_esquerda = self.carregar_imagem(
            "emparedada_esquerda.png",
            "esquerda"
        )

    def carregar_imagem(self, nome_arquivo, lado):
        if lado == "direita" and Emparedada.imagem_direita_cache is not None:
            return Emparedada.imagem_direita_cache

        if lado == "esquerda" and Emparedada.imagem_esquerda_cache is not None:
            return Emparedada.imagem_esquerda_cache

        pasta_atual = os.path.dirname(__file__)
        caminho = os.path.join(pasta_atual, "assets", nome_arquivo)

        try:
            imagem = pygame.image.load(caminho)
            imagem = imagem.convert_alpha()
            imagem = pygame.transform.scale(
                imagem,
                (self.largura, self.altura)
            )

            if lado == "direita":
                Emparedada.imagem_direita_cache = imagem
            else:
                Emparedada.imagem_esquerda_cache = imagem

            return imagem

        except FileNotFoundError:
            return None

    def mover(self, jogador):
        if self.x > jogador.x:
            self.olhando_para_direita = False
        else:
            self.olhando_para_direita = True

        diferenca_x = jogador.x - self.x
        diferenca_y = jogador.y - self.y

        distancia = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)

        if distancia != 0:
            direcao_x = diferenca_x / distancia
            direcao_y = diferenca_y / distancia

            tempo_atual = pygame.time.get_ticks()
            tempo_passado = tempo_atual - self.tempo_criacao

            movimento_senoidal = math.sin(tempo_passado * self.frequencia) * 2

            self.x += direcao_x * self.velocidade
            self.y += direcao_y * self.velocidade

            self.x += -direcao_y * movimento_senoidal
            self.y += direcao_x * movimento_senoidal

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

        self.desenhar_barra_vida(tela)


class HomemDoSaco(InimigoBase):
    imagem_direita_cache = None
    imagem_esquerda_cache = None

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            largura=150,
            altura=150,
            cor=(120, 70, 35),
            velocidade=1.1,
            dano=25,
            vida=250,
            valor_xp=60
        )

        self.eh_chefe = True

        self.olhando_para_direita = True

        self.imagem_direita = self.carregar_imagem(
            "homem_saco_direita.png",
            "direita"
        )

        self.imagem_esquerda = self.carregar_imagem(
            "homem_saco_esquerda.png",
            "esquerda"
        )

    def carregar_imagem(self, nome_arquivo, lado):
        if lado == "direita" and HomemDoSaco.imagem_direita_cache is not None:
            return HomemDoSaco.imagem_direita_cache

        if lado == "esquerda" and HomemDoSaco.imagem_esquerda_cache is not None:
            return HomemDoSaco.imagem_esquerda_cache

        pasta_atual = os.path.dirname(__file__)
        caminho = os.path.join(pasta_atual, "assets", nome_arquivo)

        try:
            imagem = pygame.image.load(caminho)
            imagem = imagem.convert_alpha()
            imagem = pygame.transform.scale(
                imagem,
                (self.largura, self.altura)
            )

            if lado == "direita":
                HomemDoSaco.imagem_direita_cache = imagem
            else:
                HomemDoSaco.imagem_esquerda_cache = imagem

            return imagem

        except FileNotFoundError:
            return None

    def mover(self, jogador):
        if self.x > jogador.x:
            self.olhando_para_direita = False
        else:
            self.olhando_para_direita = True

        diferenca_x = jogador.x - self.x
        diferenca_y = jogador.y - self.y

        distancia = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)

        if distancia != 0:
            direcao_x = diferenca_x / distancia
            direcao_y = diferenca_y / distancia

            self.x += direcao_x * self.velocidade
            self.y += direcao_y * self.velocidade

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

            pygame.draw.rect(
                tela,
                (80, 40, 20),
                (self.x + 10, self.y + 10, self.largura - 20, self.altura - 20)
            )

            pygame.draw.circle(
                tela,
                (255, 255, 255),
                (int(self.x + 25), int(self.y + 25)),
                4
            )

            pygame.draw.circle(
                tela,
                (255, 255, 255),
                (int(self.x + 45), int(self.y + 25)),
                4
            )

        self.desenhar_barra_vida(tela)