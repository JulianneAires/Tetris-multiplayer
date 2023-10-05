import pygame
import random

pygame.init()

# Configurações da tela
largura, altura = 400, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TetrisNet")
clock = pygame.time.Clock()

# Cores
preto = (0, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

 # Formatos
formas = [
    [[1, 1, 1, 1]],  # Barra
    [[1, 1], [1, 1]],  # Quadrado
    [[1, 1, 1], [0, 1, 0]],  # L
    [[1, 1, 1], [1, 0, 0]],  # L invertido
    [[1, 1, 1], [0, 0, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]]  # Z invertido
]

def criar_forma():
    return random.choice(formas)
 
def desenhar_forma(forma, x, y):
    for linha in range(len(forma)):
        for coluna in range(len(forma[linha])):
            if forma[linha][coluna]:
                pygame.draw.rect(tela, azul, (x + coluna * 30, y + linha * 30, 30, 30))
                pygame.draw.rect(tela, preto, (x + coluna * 30, y + linha * 30, 30, 30), 2)

while True: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

    pygame.display.update()
    clock.tick(60)
    x, y = largura // 2 - 15, 0
    forma_atual = criar_forma()
    desenhar_forma(forma_atual, x, y)
