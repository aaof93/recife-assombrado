import pygame
import math

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
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            largura=35,
            altura=35,
            cor=COR_INIMIGO,
            velocidade=2.6,
            dano=10,
            vida=30,
            valor_xp=10
        )


class Emparedada(InimigoBase):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            largura=32,
            altura=45,
            cor=(170, 170, 255),
            velocidade=1.8,
            dano=15,
            vida=45,
            valor_xp=15
        )

        self.tempo_criacao = pygame.time.get_ticks()
        self.amplitude = 40
        self.frequencia = 0.006

    def mover(self, jogador):
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


class HomemDoSaco(InimigoBase):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            largura=70,
            altura=70,
            cor=(120, 70, 35),
            velocidade=1.1,
            dano=25,
            vida=250,
            valor_xp=60
        )

        self.eh_chefe = True

    def mover(self, jogador):
        diferenca_x = jogador.x - self.x
        diferenca_y = jogador.y - self.y

        distancia = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)

        if distancia != 0:
            direcao_x = diferenca_x / distancia
            direcao_y = diferenca_y / distancia

            self.x += direcao_x * self.velocidade
            self.y += direcao_y * self.velocidade

    def desenhar(self, tela):
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