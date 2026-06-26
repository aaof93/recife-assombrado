import pygame
import random
import os

from config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    COR_BRANCA,
    COR_CINZA,
    COR_MASCARA
)

from jogador import Jogador
from inimigos import PernaCabeluda, Emparedada, HomemDoSaco
from itens import AlmaCapibaribe, BoloDeRolo, MascaraPapangu
from armas import LancaDoCaboclo, SombrinhaGiratoria
from cartas import criar_baralho_de_aprimoramentos
from sons import GerenciadorDeSons
from cenario import Cenario


class Jogo:
    def __init__(self):
        pygame.init()

        self.largura_tela = LARGURA_TELA
        self.altura_tela = ALTURA_TELA

        self.tela = pygame.display.set_mode(
            (self.largura_tela, self.altura_tela)
        )

        self.titulo = TITULO_JOGO
        pygame.display.set_caption(self.titulo)

        self.relogio = pygame.time.Clock()
        self.rodando = True

        self.fonte = pygame.font.SysFont("Arial", 28)
        self.fonte_media = pygame.font.SysFont("Arial", 24)
        self.fonte_pequena = pygame.font.SysFont("Arial", 20)

        self.estado = "menu"

        self.sons = GerenciadorDeSons()
        self.sons.carregar_musica_menu()

        self.cenario = Cenario("marco_zero.png")

        self.carregar_imagens()
        self.criar_botoes()
        self.criar_botoes_personagens()

    def carregar_imagem(self, nome_arquivo):
        pasta_atual = os.path.dirname(__file__)
        caminho = os.path.join(pasta_atual, "assets", nome_arquivo)

        imagem = pygame.image.load(caminho)
        imagem = imagem.convert_alpha()

        return imagem

    def carregar_imagens(self):
        self.imagem_tela_inicial = self.carregar_imagem("tela_inicial.jpg")
        self.imagem_tela_game_over = self.carregar_imagem("tela_game_over.jpg")

        self.imagem_botao_jogar = self.carregar_imagem("botao_jogar.png")
        self.imagem_botao_descricao = self.carregar_imagem("botao_descricao.png")
        self.imagem_botao_como_jogar = self.carregar_imagem("botao_como_jogar.png")
        self.imagem_botao_jogar_novamente = self.carregar_imagem("botao_jogar_novamente.png")

        self.icone_alma = self.carregar_imagem("alma.png")
        self.icone_bolo = self.carregar_imagem("bolo.png")
        self.icone_mascara = self.carregar_imagem("mascara.png")

        self.imagem_frevo_selecao = self.carregar_imagem("frevo_direita.png")
        self.imagem_caboclo_selecao = self.carregar_imagem("caboclo_esquerda.png")

        self.imagem_tela_inicial = pygame.transform.scale(
            self.imagem_tela_inicial,
            (self.largura_tela, self.altura_tela)
        )

        self.imagem_tela_game_over = pygame.transform.scale(
            self.imagem_tela_game_over,
            (self.largura_tela, self.altura_tela)
        )

        largura_botao = 260
        altura_botao = 65

        self.imagem_botao_jogar = pygame.transform.scale(
            self.imagem_botao_jogar,
            (largura_botao, altura_botao)
        )

        self.imagem_botao_descricao = pygame.transform.scale(
            self.imagem_botao_descricao,
            (largura_botao, altura_botao)
        )

        self.imagem_botao_como_jogar = pygame.transform.scale(
            self.imagem_botao_como_jogar,
            (largura_botao, altura_botao)
        )

        self.imagem_botao_jogar_novamente = pygame.transform.scale(
            self.imagem_botao_jogar_novamente,
            (300, 70)
        )

        tamanho_icone = 30

        self.icone_alma = pygame.transform.scale(
            self.icone_alma,
            (tamanho_icone, tamanho_icone)
        )

        self.icone_bolo = pygame.transform.scale(
            self.icone_bolo,
            (tamanho_icone, tamanho_icone)
        )

        self.icone_mascara = pygame.transform.scale(
            self.icone_mascara,
            (tamanho_icone, tamanho_icone)
        )

        self.imagem_frevo_selecao = pygame.transform.scale(
            self.imagem_frevo_selecao,
            (140, 170)
        )

        self.imagem_caboclo_selecao = pygame.transform.scale(
            self.imagem_caboclo_selecao,
            (140, 170)
        )

    def criar_botoes(self):
        descer_botoes = 40

        self.botao_jogar = self.imagem_botao_jogar.get_rect(
            center=(self.largura_tela // 2, 325 + descer_botoes)
        )

        self.botao_descricao = self.imagem_botao_descricao.get_rect(
            center=(self.largura_tela // 2, 405 + descer_botoes)
        )

        self.botao_como_jogar = self.imagem_botao_como_jogar.get_rect(
            center=(self.largura_tela // 2, 485 + descer_botoes)
        )

        self.botao_jogar_novamente = self.imagem_botao_jogar_novamente.get_rect(
            center=(self.largura_tela // 2, 460)
        )

    def criar_botoes_personagens(self):
        self.retangulo_frevo = self.imagem_frevo_selecao.get_rect(
            center=(self.largura_tela // 2 - 180, 320)
        )

        self.retangulo_caboclo = self.imagem_caboclo_selecao.get_rect(
            center=(self.largura_tela // 2 + 180, 320)
        )

    def iniciar_partida(self, personagem_escolhido):
        self.game_over = False
        self.jogador = Jogador(430, 280, personagem_escolhido)

        self.cenario.trocar_imagem("marco_zero.png")
        self.fase_rua_bom_jesus_ativa = False

        self.total_almas_coletadas = 0
        self.total_bolos_coletados = 0
        self.total_mascaras_coletadas = 0

        self.armas = []
        self.armas.append(LancaDoCaboclo())
        self.armas.append(SombrinhaGiratoria())

        self.inimigos = []
        self.projeteis = []
        self.almas = []
        self.bolos = []
        self.mascaras = []

        self.tempo_ultimo_spawn = 0
        self.intervalo_spawn = 1000

        self.tempo_inicio = pygame.time.get_ticks()
        self.inimigos_derrotados = 0

        self.tela_evolucao_aberta = False
        self.cartas_atuais = []

        self.efeito_onda_ativo = False
        self.tempo_inicio_onda = 0
        self.x_onda = 0
        self.y_onda = 0

        self.tempo_ultimo_chefe = pygame.time.get_ticks()
        self.intervalo_chefe = 30000
        self.primeiro_chefe_apareceu = False

        self.mensagem_chefe_ativa = False
        self.tempo_inicio_mensagem_chefe = 0
        self.duracao_mensagem_chefe = 3000

    def verificar_mudanca_de_fase(self):
        if self.jogador.nivel >= 10 and not self.fase_rua_bom_jesus_ativa:
            self.fase_rua_bom_jesus_ativa = True
            self.cenario.trocar_imagem("rua_bom_jesus.png")
            self.sons.carregar_musica_rua_bom_jesus()

    def criar_posicao_na_borda(self, tamanho):
        borda = random.randint(1, 4)

        if borda == 1:
            x = random.randint(0, self.largura_tela - tamanho)
            y = -tamanho

        elif borda == 2:
            x = random.randint(0, self.largura_tela - tamanho)
            y = self.altura_tela

        elif borda == 3:
            x = -tamanho
            y = random.randint(0, self.altura_tela - tamanho)

        else:
            x = self.largura_tela
            y = random.randint(0, self.altura_tela - tamanho)

        return x, y

    def criar_inimigo_na_borda(self):
        x, y = self.criar_posicao_na_borda(35)

        chance = random.randint(1, 100)

        if chance <= 75:
            inimigo = PernaCabeluda(x, y)
        else:
            inimigo = Emparedada(x, y)

        self.inimigos.append(inimigo)

    def criar_chefe_na_borda(self):
        x, y = self.criar_posicao_na_borda(70)
        chefe = HomemDoSaco(x, y)
        self.inimigos.append(chefe)

        self.mensagem_chefe_ativa = True
        self.tempo_inicio_mensagem_chefe = pygame.time.get_ticks()

    def controlar_spawn_inimigos(self):
        tempo_atual = pygame.time.get_ticks()

        if tempo_atual - self.tempo_ultimo_spawn >= self.intervalo_spawn:
            self.criar_inimigo_na_borda()
            self.tempo_ultimo_spawn = tempo_atual

    def controlar_spawn_chefe(self):
        tempo_atual = pygame.time.get_ticks()
        tempo_de_jogo = tempo_atual - self.tempo_inicio

        if not self.primeiro_chefe_apareceu and tempo_de_jogo >= 10000:
            self.criar_chefe_na_borda()
            self.primeiro_chefe_apareceu = True
            self.tempo_ultimo_chefe = tempo_atual

        elif self.primeiro_chefe_apareceu:
            if tempo_atual - self.tempo_ultimo_chefe >= self.intervalo_chefe:
                self.criar_chefe_na_borda()
                self.tempo_ultimo_chefe = tempo_atual

    def criar_alma(self, inimigo):
        centro_x, centro_y = inimigo.obter_centro()
        alma = AlmaCapibaribe(centro_x, centro_y, inimigo.valor_xp)
        self.almas.append(alma)

    def criar_bolo(self, inimigo):
        centro_x, centro_y = inimigo.obter_centro()
        bolo = BoloDeRolo(centro_x, centro_y)
        self.bolos.append(bolo)

    def criar_mascara(self, inimigo):
        centro_x, centro_y = inimigo.obter_centro()
        mascara = MascaraPapangu(centro_x, centro_y)
        self.mascaras.append(mascara)

    def gerar_recompensa_inimigo(self, inimigo):
        chance = random.randint(1, 100)

        if inimigo.eh_chefe:
            if chance <= 60:
                self.criar_bolo(inimigo)
            else:
                self.criar_alma(inimigo)

        else:
            if chance <= 5:
                self.criar_mascara(inimigo)
            elif chance <= 20:
                self.criar_bolo(inimigo)
            else:
                self.criar_alma(inimigo)

    def gerar_alma_por_mascara(self, inimigo):
        self.criar_alma(inimigo)

    def gerar_cartas_de_aprimoramento(self):
        todas_as_cartas = criar_baralho_de_aprimoramentos()

        self.cartas_atuais = random.sample(todas_as_cartas, 3)
        self.tela_evolucao_aberta = True

    def escolher_carta(self, indice):
        if indice < len(self.cartas_atuais):
            carta = self.cartas_atuais[indice]
            carta.aplicar(self.jogador, self.armas)

            self.cartas_atuais = []
            self.tela_evolucao_aberta = False

    def verificar_clique_menu(self, posicao_mouse):
        if self.botao_jogar.collidepoint(posicao_mouse):
            self.estado = "selecao_personagem"

        elif self.botao_descricao.collidepoint(posicao_mouse):
            self.estado = "descricao"

        elif self.botao_como_jogar.collidepoint(posicao_mouse):
            self.estado = "como_jogar"

    def verificar_clique_selecao_personagem(self, posicao_mouse):
        if self.retangulo_frevo.collidepoint(posicao_mouse):
            self.iniciar_partida("frevo")
            self.estado = "jogando"
            self.sons.carregar_musica_gameplay()

        elif self.retangulo_caboclo.collidepoint(posicao_mouse):
            self.iniciar_partida("caboclo")
            self.estado = "jogando"
            self.sons.carregar_musica_gameplay()

    def verificar_clique_game_over(self, posicao_mouse):
        if self.botao_jogar_novamente.collidepoint(posicao_mouse):
            self.estado = "selecao_personagem"

    def verificar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    posicao_mouse = pygame.mouse.get_pos()

                    if self.estado == "menu":
                        self.verificar_clique_menu(posicao_mouse)

                    elif self.estado == "selecao_personagem":
                        self.verificar_clique_selecao_personagem(posicao_mouse)

                    elif self.estado == "game_over":
                        self.verificar_clique_game_over(posicao_mouse)

            if evento.type == pygame.KEYDOWN:
                if self.estado == "descricao":
                    if evento.key == pygame.K_ESCAPE:
                        self.estado = "menu"

                elif self.estado == "como_jogar":
                    if evento.key == pygame.K_ESCAPE:
                        self.estado = "menu"

                elif self.estado == "selecao_personagem":
                    if evento.key == pygame.K_ESCAPE:
                        self.estado = "menu"

                elif self.estado == "jogando":
                    if self.tela_evolucao_aberta:
                        if evento.key == pygame.K_1:
                            self.escolher_carta(0)

                        elif evento.key == pygame.K_2:
                            self.escolher_carta(1)

                        elif evento.key == pygame.K_3:
                            self.escolher_carta(2)

    def verificar_colisao_jogador_inimigos(self):
        retangulo_jogador = self.jogador.obter_retangulo()

        for inimigo in self.inimigos:
            retangulo_inimigo = inimigo.obter_retangulo()

            if retangulo_jogador.colliderect(retangulo_inimigo):
                self.jogador.receber_dano(inimigo.dano)

    def verificar_colisao_jogador_almas(self):
        retangulo_jogador = self.jogador.obter_retangulo()
        almas_coletadas = []

        for alma in self.almas:
            retangulo_alma = alma.obter_retangulo()

            if retangulo_jogador.colliderect(retangulo_alma):
                subiu_nivel = self.jogador.ganhar_xp(alma.valor_xp)
                almas_coletadas.append(alma)
                self.total_almas_coletadas += 1

                if subiu_nivel:
                    self.verificar_mudanca_de_fase()
                    self.gerar_cartas_de_aprimoramento()

        for alma in almas_coletadas:
            if alma in self.almas:
                self.almas.remove(alma)

    def verificar_colisao_jogador_bolos(self):
        retangulo_jogador = self.jogador.obter_retangulo()
        bolos_coletados = []

        for bolo in self.bolos:
            retangulo_bolo = bolo.obter_retangulo()

            if retangulo_jogador.colliderect(retangulo_bolo):
                self.jogador.curar(bolo.cura)
                bolos_coletados.append(bolo)
                self.total_bolos_coletados += 1

        for bolo in bolos_coletados:
            if bolo in self.bolos:
                self.bolos.remove(bolo)

    def verificar_colisao_jogador_mascaras(self):
        retangulo_jogador = self.jogador.obter_retangulo()
        mascaras_coletadas = []

        for mascara in self.mascaras:
            retangulo_mascara = mascara.obter_retangulo()

            if retangulo_jogador.colliderect(retangulo_mascara):
                self.ativar_onda_papangu(mascara.x, mascara.y)
                mascaras_coletadas.append(mascara)
                self.total_mascaras_coletadas += 1

        for mascara in mascaras_coletadas:
            if mascara in self.mascaras:
                self.mascaras.remove(mascara)

    def ativar_onda_papangu(self, x, y):
        self.efeito_onda_ativo = True
        self.tempo_inicio_onda = pygame.time.get_ticks()
        self.x_onda = x
        self.y_onda = y

        inimigos_eliminados = []

        for inimigo in self.inimigos:
            if not inimigo.eh_chefe:
                inimigos_eliminados.append(inimigo)

        for inimigo in inimigos_eliminados:
            if inimigo in self.inimigos:
                self.gerar_alma_por_mascara(inimigo)
                self.inimigos.remove(inimigo)
                self.inimigos_derrotados += 1

    def verificar_colisao_projeteis_inimigos(self):
        projeteis_remover = []
        inimigos_remover = []

        for projetil in self.projeteis:
            retangulo_projetil = projetil.obter_retangulo()

            for inimigo in self.inimigos:
                retangulo_inimigo = inimigo.obter_retangulo()

                if retangulo_projetil.colliderect(retangulo_inimigo):
                    inimigo.receber_dano(projetil.dano)
                    projeteis_remover.append(projetil)

                    if inimigo.esta_morto():
                        inimigos_remover.append(inimigo)

                    break

        for projetil in projeteis_remover:
            if projetil in self.projeteis:
                self.projeteis.remove(projetil)

        for inimigo in inimigos_remover:
            if inimigo in self.inimigos:
                self.gerar_recompensa_inimigo(inimigo)
                self.inimigos.remove(inimigo)
                self.inimigos_derrotados += 1

    def remover_inimigos_mortos(self):
        inimigos_vivos = []

        for inimigo in self.inimigos:
            if inimigo.esta_morto():
                self.gerar_recompensa_inimigo(inimigo)
                self.inimigos_derrotados += 1
            else:
                inimigos_vivos.append(inimigo)

        self.inimigos = inimigos_vivos

    def remover_projeteis_fora_da_tela(self):
        projeteis_validos = []

        for projetil in self.projeteis:
            if not projetil.saiu_da_tela(self.largura_tela, self.altura_tela):
                projeteis_validos.append(projetil)

        self.projeteis = projeteis_validos

    def verificar_game_over(self):
        if self.jogador.vida_atual <= 0:
            self.game_over = True
            self.estado = "game_over"

    def atualizar_inimigos(self):
        for inimigo in self.inimigos:
            inimigo.mover(self.jogador)

    def atualizar_projeteis(self):
        for projetil in self.projeteis:
            projetil.mover()

    def atualizar_armas(self):
        for arma in self.armas:
            arma.atualizar(
                self.jogador,
                self.inimigos,
                self.projeteis
            )

    def atualizar_efeito_onda(self):
        if self.efeito_onda_ativo:
            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_inicio_onda > 500:
                self.efeito_onda_ativo = False

    def atualizar_mensagem_chefe(self):
        if self.mensagem_chefe_ativa:
            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_inicio_mensagem_chefe > self.duracao_mensagem_chefe:
                self.mensagem_chefe_ativa = False

    def atualizar(self):
        if self.estado != "jogando":
            return

        if self.game_over:
            return

        if self.tela_evolucao_aberta:
            return

        self.jogador.mover(self.largura_tela, self.altura_tela)

        self.controlar_spawn_inimigos()
        self.controlar_spawn_chefe()

        self.atualizar_armas()
        self.atualizar_inimigos()
        self.atualizar_projeteis()
        self.atualizar_efeito_onda()
        self.atualizar_mensagem_chefe()

        self.verificar_colisao_jogador_inimigos()
        self.verificar_colisao_projeteis_inimigos()
        self.verificar_colisao_jogador_almas()
        self.verificar_colisao_jogador_bolos()
        self.verificar_colisao_jogador_mascaras()

        self.remover_inimigos_mortos()
        self.remover_projeteis_fora_da_tela()
        self.verificar_game_over()

    def desenhar_barra_de_vida(self):
        largura_barra = 200
        altura_barra = 20
        x_barra = 20
        y_barra = 20

        proporcao_vida = self.jogador.vida_atual / self.jogador.vida_maxima
        largura_vida_atual = largura_barra * proporcao_vida

        pygame.draw.rect(
            self.tela,
            COR_CINZA,
            (x_barra, y_barra, largura_barra, altura_barra)
        )

        pygame.draw.rect(
            self.tela,
            (0, 200, 0),
            (x_barra, y_barra, largura_vida_atual, altura_barra)
        )

        pygame.draw.rect(
            self.tela,
            COR_BRANCA,
            (x_barra, y_barra, largura_barra, altura_barra),
            2
        )

        texto = self.fonte_pequena.render(
            f"HP {self.jogador.vida_atual}/{self.jogador.vida_maxima}",
            True,
            COR_BRANCA
        )

        self.tela.blit(texto, (230, 18))

    def desenhar_barra_de_xp(self):
        largura_barra = 300
        altura_barra = 14
        x_barra = 20
        y_barra = self.altura_tela - 30

        proporcao_xp = self.jogador.xp_atual / self.jogador.xp_para_proximo_nivel
        largura_xp_atual = largura_barra * proporcao_xp

        pygame.draw.rect(
            self.tela,
            (70, 70, 70),
            (x_barra, y_barra, largura_barra, altura_barra)
        )

        pygame.draw.rect(
            self.tela,
            (0, 180, 255),
            (x_barra, y_barra, largura_xp_atual, altura_barra)
        )

        pygame.draw.rect(
            self.tela,
            COR_BRANCA,
            (x_barra, y_barra, largura_barra, altura_barra),
            2
        )

        texto = self.fonte_pequena.render(
            f"Nível {self.jogador.nivel} - XP {self.jogador.xp_atual}/{self.jogador.xp_para_proximo_nivel}",
            True,
            COR_BRANCA
        )

        self.tela.blit(texto, (x_barra + largura_barra + 15, y_barra - 5))

    def desenhar_tempo(self):
        tempo_atual = pygame.time.get_ticks()
        segundos = (tempo_atual - self.tempo_inicio) // 1000

        texto = self.fonte_pequena.render(
            f"Tempo: {segundos}s",
            True,
            COR_BRANCA
        )

        self.tela.blit(texto, (20, 50))

    def desenhar_quantidade_inimigos(self):
        texto = self.fonte_pequena.render(
            f"Inimigos: {len(self.inimigos)}",
            True,
            COR_BRANCA
        )

        self.tela.blit(texto, (20, 75))

    def desenhar_inimigos_derrotados(self):
        texto = self.fonte_pequena.render(
            f"Derrotados: {self.inimigos_derrotados}",
            True,
            COR_BRANCA
        )

        self.tela.blit(texto, (20, 100))

    def desenhar_armas(self):
        y = 125

        for arma in self.armas:
            texto = self.fonte_pequena.render(
                f"Arma: {arma.nome} | Dano: {arma.dano} | CD: {arma.intervalo_ataque}",
                True,
                COR_BRANCA
            )

            self.tela.blit(texto, (20, y))
            y += 25

    def desenhar_mensagem_chefe(self):
        if self.mensagem_chefe_ativa:
            texto = self.fonte.render(
                "O Homem do Saco apareceu!",
                True,
                (255, 220, 80)
            )

            retangulo_texto = texto.get_rect(
                center=(self.largura_tela // 2, 80)
            )

            pygame.draw.rect(
                self.tela,
                (80, 40, 20),
                (
                    retangulo_texto.x - 20,
                    retangulo_texto.y - 10,
                    retangulo_texto.width + 40,
                    retangulo_texto.height + 20
                )
            )

            pygame.draw.rect(
                self.tela,
                COR_BRANCA,
                (
                    retangulo_texto.x - 20,
                    retangulo_texto.y - 10,
                    retangulo_texto.width + 40,
                    retangulo_texto.height + 20
                ),
                2
            )

            self.tela.blit(texto, retangulo_texto)

    def desenhar_contadores_itens(self):
        x_base = self.largura_tela - 100
        y_base = self.altura_tela - 115
        distancia_linhas = 38

        texto_almas = self.fonte_pequena.render(
            f"x {self.total_almas_coletadas}",
            True,
            COR_BRANCA
        )

        texto_bolos = self.fonte_pequena.render(
            f"x {self.total_bolos_coletados}",
            True,
            COR_BRANCA
        )

        texto_mascaras = self.fonte_pequena.render(
            f"x {self.total_mascaras_coletadas}",
            True,
            COR_BRANCA
        )

        self.tela.blit(self.icone_alma, (x_base, y_base))
        self.tela.blit(texto_almas, (x_base + 40, y_base + 5))

        self.tela.blit(self.icone_bolo, (x_base, y_base + distancia_linhas))
        self.tela.blit(texto_bolos, (x_base + 40, y_base + distancia_linhas + 5))

        self.tela.blit(self.icone_mascara, (x_base, y_base + distancia_linhas * 2))
        self.tela.blit(texto_mascaras, (x_base + 40, y_base + distancia_linhas * 2 + 5))

    def desenhar_inimigos(self):
        for inimigo in self.inimigos:
            inimigo.desenhar(self.tela)

    def desenhar_projeteis(self):
        for projetil in self.projeteis:
            projetil.desenhar(self.tela)

    def desenhar_almas(self):
        for alma in self.almas:
            alma.desenhar(self.tela)

    def desenhar_bolos(self):
        for bolo in self.bolos:
            bolo.desenhar(self.tela)

    def desenhar_mascaras(self):
        for mascara in self.mascaras:
            mascara.desenhar(self.tela)

    def desenhar_armas_visuais(self):
        for arma in self.armas:
            arma.desenhar(self.tela, self.jogador)

    def desenhar_efeito_onda(self):
        if self.efeito_onda_ativo:
            tempo_atual = pygame.time.get_ticks()
            tempo_passado = tempo_atual - self.tempo_inicio_onda
            raio = tempo_passado * 2

            pygame.draw.circle(
                self.tela,
                COR_MASCARA,
                (int(self.x_onda), int(self.y_onda)),
                raio,
                4
            )

    def desenhar_tela_evolucao(self):
        fundo = pygame.Surface((self.largura_tela, self.altura_tela))
        fundo.set_alpha(220)
        fundo.fill((10, 10, 10))
        self.tela.blit(fundo, (0, 0))

        titulo = self.fonte.render(
            "Escolha uma carta de aprimoramento",
            True,
            COR_BRANCA
        )

        retangulo_titulo = titulo.get_rect(
            center=(self.largura_tela // 2, 100)
        )

        self.tela.blit(titulo, retangulo_titulo)

        largura_carta = 240
        altura_carta = 260
        espaco = 30
        x_inicial = (
            self.largura_tela
            - (largura_carta * 3)
            - (espaco * 2)
        ) // 2

        y_carta = 180

        for i in range(len(self.cartas_atuais)):
            carta = self.cartas_atuais[i]
            x_carta = x_inicial + i * (largura_carta + espaco)

            pygame.draw.rect(
                self.tela,
                (60, 60, 90),
                (x_carta, y_carta, largura_carta, altura_carta)
            )

            pygame.draw.rect(
                self.tela,
                COR_BRANCA,
                (x_carta, y_carta, largura_carta, altura_carta),
                3
            )

            numero = self.fonte.render(
                str(i + 1),
                True,
                (255, 230, 0)
            )

            self.tela.blit(numero, (x_carta + 15, y_carta + 15))

            titulo_carta = self.fonte_media.render(
                carta.titulo,
                True,
                COR_BRANCA
            )

            self.tela.blit(titulo_carta, (x_carta + 20, y_carta + 80))

            descricao = self.fonte_pequena.render(
                carta.descricao,
                True,
                (220, 220, 220)
            )

            self.tela.blit(descricao, (x_carta + 20, y_carta + 130))

        instrucao = self.fonte_pequena.render(
            "Pressione 1, 2 ou 3 para escolher",
            True,
            COR_BRANCA
        )

        retangulo_instrucao = instrucao.get_rect(
            center=(self.largura_tela // 2, 500)
        )

        self.tela.blit(instrucao, retangulo_instrucao)

    def desenhar_menu(self):
        self.tela.blit(self.imagem_tela_inicial, (0, 0))

        self.tela.blit(self.imagem_botao_jogar, self.botao_jogar)
        self.tela.blit(self.imagem_botao_descricao, self.botao_descricao)
        self.tela.blit(self.imagem_botao_como_jogar, self.botao_como_jogar)

    def desenhar_selecao_personagem(self):
        self.tela.fill((15, 15, 25))

        titulo = self.fonte.render(
            "Escolha seu personagem",
            True,
            COR_BRANCA
        )

        retangulo_titulo = titulo.get_rect(
            center=(self.largura_tela // 2, 80)
        )

        self.tela.blit(titulo, retangulo_titulo)

        pygame.draw.rect(
            self.tela,
            (60, 60, 90),
            (
                self.retangulo_frevo.x - 25,
                self.retangulo_frevo.y - 25,
                self.retangulo_frevo.width + 50,
                self.retangulo_frevo.height + 90
            )
        )

        pygame.draw.rect(
            self.tela,
            COR_BRANCA,
            (
                self.retangulo_frevo.x - 25,
                self.retangulo_frevo.y - 25,
                self.retangulo_frevo.width + 50,
                self.retangulo_frevo.height + 90
            ),
            3
        )

        pygame.draw.rect(
            self.tela,
            (60, 60, 90),
            (
                self.retangulo_caboclo.x - 25,
                self.retangulo_caboclo.y - 25,
                self.retangulo_caboclo.width + 50,
                self.retangulo_caboclo.height + 90
            )
        )

        pygame.draw.rect(
            self.tela,
            COR_BRANCA,
            (
                self.retangulo_caboclo.x - 25,
                self.retangulo_caboclo.y - 25,
                self.retangulo_caboclo.width + 50,
                self.retangulo_caboclo.height + 90
            ),
            3
        )

        self.tela.blit(self.imagem_frevo_selecao, self.retangulo_frevo)
        self.tela.blit(self.imagem_caboclo_selecao, self.retangulo_caboclo)

        texto_frevo = self.fonte_media.render(
            "Passista de Frevo",
            True,
            COR_BRANCA
        )

        texto_caboclo = self.fonte_media.render(
            "Caboclo de Lança",
            True,
            COR_BRANCA
        )

        atributo_frevo = self.fonte_pequena.render(
            "Mais velocidade, menos vida",
            True,
            (220, 220, 220)
        )

        atributo_caboclo = self.fonte_pequena.render(
            "Mais vida, menos velocidade",
            True,
            (220, 220, 220)
        )

        self.tela.blit(
            texto_frevo,
            texto_frevo.get_rect(center=(self.retangulo_frevo.centerx, 440))
        )

        self.tela.blit(
            atributo_frevo,
            atributo_frevo.get_rect(center=(self.retangulo_frevo.centerx, 490))
        )

        self.tela.blit(
            texto_caboclo,
            texto_caboclo.get_rect(center=(self.retangulo_caboclo.centerx, 440))
        )

        self.tela.blit(
            atributo_caboclo,
            atributo_caboclo.get_rect(center=(self.retangulo_caboclo.centerx, 490))
        )

        instrucao = self.fonte_pequena.render(
            "Clique em um personagem para começar. ESC volta ao menu.",
            True,
            (255, 220, 80)
        )

        self.tela.blit(
            instrucao,
            instrucao.get_rect(center=(self.largura_tela // 2, 540))
        )

    def desenhar_descricao(self):
        self.tela.fill((15, 15, 25))

        titulo = self.fonte.render(
            "Descrição",
            True,
            COR_BRANCA
        )

        texto_1 = self.fonte_pequena.render(
            "Sobrevivência Pernambucana é um jogo de sobrevivência em arena.",
            True,
            COR_BRANCA
        )

        texto_2 = self.fonte_pequena.render(
            "O jogador enfrenta criaturas inspiradas na cultura e no folclore local.",
            True,
            COR_BRANCA
        )

        texto_3 = self.fonte_pequena.render(
            "Colete almas para ganhar XP, escolha cartas e sobreviva ao Homem do Saco.",
            True,
            COR_BRANCA
        )

        voltar = self.fonte_pequena.render(
            "Pressione ESC para voltar ao menu.",
            True,
            (255, 220, 80)
        )

        self.tela.blit(titulo, (370, 120))
        self.tela.blit(texto_1, (120, 220))
        self.tela.blit(texto_2, (120, 260))
        self.tela.blit(texto_3, (120, 300))
        self.tela.blit(voltar, (300, 470))

    def desenhar_como_jogar(self):
        self.tela.fill((15, 15, 25))

        titulo = self.fonte.render(
            "Como jogar",
            True,
            COR_BRANCA
        )

        texto_1 = self.fonte_pequena.render(
            "W, A, S, D: mover o personagem.",
            True,
            COR_BRANCA
        )

        texto_2 = self.fonte_pequena.render(
            "Mouse: mirar a Lança do Caboclo.",
            True,
            COR_BRANCA
        )

        texto_3 = self.fonte_pequena.render(
            "Colete almas azuis para ganhar XP e subir de nível.",
            True,
            COR_BRANCA
        )

        texto_4 = self.fonte_pequena.render(
            "Ao subir de nível, pressione 1, 2 ou 3 para escolher uma carta.",
            True,
            COR_BRANCA
        )

        texto_5 = self.fonte_pequena.render(
            "Bolo de Rolo cura vida. Máscara de Papangu elimina inimigos comuns.",
            True,
            COR_BRANCA
        )

        voltar = self.fonte_pequena.render(
            "Pressione ESC para voltar ao menu.",
            True,
            (255, 220, 80)
        )

        self.tela.blit(titulo, (360, 100))
        self.tela.blit(texto_1, (120, 200))
        self.tela.blit(texto_2, (120, 240))
        self.tela.blit(texto_3, (120, 280))
        self.tela.blit(texto_4, (120, 320))
        self.tela.blit(texto_5, (120, 360))
        self.tela.blit(voltar, (300, 470))

    def desenhar_game_over(self):
        self.tela.blit(self.imagem_tela_game_over, (0, 0))
        self.tela.blit(self.imagem_botao_jogar_novamente, self.botao_jogar_novamente)

    def desenhar_jogo(self):
        self.cenario.desenhar(self.tela)

        self.desenhar_almas()
        self.desenhar_bolos()
        self.desenhar_mascaras()

        self.jogador.desenhar(self.tela)
        self.desenhar_inimigos()
        self.desenhar_projeteis()
        self.desenhar_armas_visuais()
        self.desenhar_efeito_onda()

        self.desenhar_barra_de_vida()
        self.desenhar_tempo()
        self.desenhar_quantidade_inimigos()
        self.desenhar_inimigos_derrotados()
        self.desenhar_armas()
        self.desenhar_barra_de_xp()
        self.desenhar_mensagem_chefe()
        self.desenhar_contadores_itens()

        if self.tela_evolucao_aberta:
            self.desenhar_tela_evolucao()

    def desenhar(self):
        if self.estado == "menu":
            self.desenhar_menu()

        elif self.estado == "selecao_personagem":
            self.desenhar_selecao_personagem()

        elif self.estado == "descricao":
            self.desenhar_descricao()

        elif self.estado == "como_jogar":
            self.desenhar_como_jogar()

        elif self.estado == "jogando":
            self.desenhar_jogo()

        elif self.estado == "game_over":
            self.desenhar_game_over()
            self.sons.gameover()

        pygame.display.flip()

    def executar(self):
        while self.rodando:
            self.verificar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)

        pygame.quit()