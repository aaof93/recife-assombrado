import pygame
import sys

pygame.init()

# Configurações da Janela
LARGURA_TELA = 1280
ALTURA_TELA = 720
FPS = 60

class Jogo:
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Sobrevivência Pernambucana")
        self.relogio = pygame.time.Clock()
        self.rodando = True

    def gerenciar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
        pass

    def desenhar(self):
        self.tela.fill((30, 30, 30)) # Fundo cinza escuro
        pygame.display.flip()

    def executar(self):
        while self.rodando:
            self.gerenciar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()