from pathlib import Path

import pygame
import math

from config import COR_PROJETIL, COR_SOMBRINHA


class Projetil:
    imagem_cache = None

    def __init__(self, x, y, direcao_x, direcao_y, dano):
        self.x = x
        self.y = y

        self.largura = 70
        self.altura = 35
        self.raio = 6
        self.cor = COR_PROJETIL

        self.velocidade = 8
        self.dano = dano

        self.direcao_x = direcao_x
        self.direcao_y = direcao_y

        self.imagem_original = self.carregar_imagem()
        self.imagem = self.criar_imagem_rotacionada()

    def carregar_imagem(self):
        if Projetil.imagem_cache is not None:
            return Projetil.imagem_cache

        caminho_imagem = (
            Path(__file__).resolve().parent
            / "assets"
            / "lanca_final.png"
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

        Projetil.imagem_cache = imagem

        return imagem

    def criar_imagem_rotacionada(self):
        if self.imagem_original is None:
            return None

        angulo = math.degrees(
            math.atan2(self.direcao_y, self.direcao_x)
        )

        imagem_rotacionada = pygame.transform.rotate(
            self.imagem_original,
            -angulo
        )

        return imagem_rotacionada

    def mover(self):
        self.x += self.direcao_x * self.velocidade
        self.y += self.direcao_y * self.velocidade

    def saiu_da_tela(self, largura_tela, altura_tela):
        if self.x < -20:
            return True

        if self.x > largura_tela + 20:
            return True

        if self.y < -20:
            return True

        if self.y > altura_tela + 20:
            return True

        return False

    def obter_retangulo(self):
        if self.imagem is not None:
            retangulo = self.imagem.get_rect(
                center=(self.x, self.y)
            )

            return retangulo

        return pygame.Rect(
            self.x - self.raio,
            self.y - self.raio,
            self.raio * 2,
            self.raio * 2
        )

    def desenhar(self, tela):
        if self.imagem is not None:
            retangulo = self.imagem.get_rect(
                center=(self.x, self.y)
            )

            tela.blit(
                self.imagem,
                retangulo
            )

        else:
            pygame.draw.circle(
                tela,
                self.cor,
                (int(self.x), int(self.y)),
                self.raio
            )


class ArmaBase:
    def __init__(self, nome, dano, intervalo_ataque):
        self.nome = nome
        self.dano = dano
        self.intervalo_ataque = intervalo_ataque
        self.tempo_ultimo_ataque = 0

    def pode_atacar(self):
        tempo_atual = pygame.time.get_ticks()

        if tempo_atual - self.tempo_ultimo_ataque >= self.intervalo_ataque:
            self.tempo_ultimo_ataque = tempo_atual
            return True

        return False

    def aumentar_dano(self):
        self.dano += 5

    def reduzir_cooldown(self):
        self.intervalo_ataque -= 80

        if self.intervalo_ataque < 150:
            self.intervalo_ataque = 150

    def atualizar(self, jogador, inimigos, projeteis):
        pass

    def desenhar(self, tela, jogador):
        pass


class LancaDoCaboclo(ArmaBase):
    def __init__(self):
        super().__init__("Lança do Caboclo", dano=20, intervalo_ataque=700)

    def atualizar(self, jogador, inimigos, projeteis):
        if not self.pode_atacar():
            return

        jogador_x, jogador_y = jogador.obter_centro()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        diferenca_x = mouse_x - jogador_x
        diferenca_y = mouse_y - jogador_y

        distancia = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)

        if distancia != 0:
            direcao_x = diferenca_x / distancia
            direcao_y = diferenca_y / distancia

            projetil = Projetil(
                jogador_x,
                jogador_y,
                direcao_x,
                direcao_y,
                self.dano
            )

            projeteis.append(projetil)


class SombrinhaGiratoria(ArmaBase):
    imagem_cache = None

    def __init__(self):
        super().__init__("Sombrinha Giratória", dano=10, intervalo_ataque=350)

        self.angulo = 0
        self.distancia_do_jogador = 70

        self.largura = 60
        self.altura = 60
        self.raio = 18

        self.velocidade_giro = 4
        self.cor = COR_SOMBRINHA

        self.x = 0
        self.y = 0

        self.imagem_original = self.carregar_imagem()

    def carregar_imagem(self):
        if SombrinhaGiratoria.imagem_cache is not None:
            return SombrinhaGiratoria.imagem_cache

        caminho_imagem = (
            Path(__file__).resolve().parent
            / "assets"
            / "sombrinha_giratoria.png"
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

        SombrinhaGiratoria.imagem_cache = imagem

        return imagem

    def atualizar_posicao(self, jogador):
        centro_jogador_x, centro_jogador_y = jogador.obter_centro()

        self.x = centro_jogador_x + math.cos(math.radians(self.angulo)) * self.distancia_do_jogador
        self.y = centro_jogador_y + math.sin(math.radians(self.angulo)) * self.distancia_do_jogador

        self.angulo += self.velocidade_giro

        if self.angulo >= 360:
            self.angulo = 0

    def atualizar(self, jogador, inimigos, projeteis):
        self.atualizar_posicao(jogador)

        if not self.pode_atacar():
            return

        retangulo_sombrinha = self.obter_retangulo()

        for inimigo in inimigos:
            retangulo_inimigo = inimigo.obter_retangulo()

            if retangulo_sombrinha.colliderect(retangulo_inimigo):
                inimigo.receber_dano(self.dano)

    def aumentar_alcance(self):
        self.distancia_do_jogador += 15

    def obter_retangulo(self):
        return pygame.Rect(
            self.x - self.raio,
            self.y - self.raio,
            self.raio * 2,
            self.raio * 2
        )

    def desenhar(self, tela, jogador):
        if self.imagem_original is not None:
            imagem_rotacionada = pygame.transform.rotate(
                self.imagem_original,
                -self.angulo
            )

            retangulo = imagem_rotacionada.get_rect(
                center=(self.x, self.y)
            )

            tela.blit(
                imagem_rotacionada,
                retangulo
            )

        else:
            pygame.draw.circle(
                tela,
                self.cor,
                (int(self.x), int(self.y)),
                self.raio
            )