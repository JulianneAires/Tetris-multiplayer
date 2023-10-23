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

cores_formas = {
    0: (0, 255, 0),  # Barra (verde)
    1: (255, 0, 0),  # Quadrado (vermelho)
    2: (0, 255, 255),  # L (ciano)
    3: (255, 255, 0),  # L invertido (amarelo)
    4: (255, 165, 0),  # T (laranja)
    5: (255, 0, 128),  # Z (rosa)
    6: (128, 0, 255)  # Z invertido (cinza)
}

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

def desenhar_forma(forma, x, y, cores_formas ):
    for linha in range(len(forma)):
        for coluna in range(len(forma[linha])):
            if forma[linha][coluna]:
                pygame.draw.rect(tela, cores_formas , (x + coluna * 30, y + linha * 30, 30, 30))
                pygame.draw.rect(tela, preto, (x + coluna * 30, y + linha * 30, 30, 30), 2)

def desenhar_grade(surface):
    cor_grade = (128, 128, 128)
    espacamento = 30
    # Linhas horizontais
    for linha in range(altura // espacamento):
        pygame.draw.line(surface, cor_grade, (0, linha * espacamento), (largura, linha * espacamento))

    # Linhas verticais
    for coluna in range(largura // espacamento):
        pygame.draw.line(surface, cor_grade, (coluna * espacamento, 0), (coluna * espacamento, altura))

def colisao(forma, x, y, grid):
    for linha in range(len(forma)):
        for coluna in range(len(forma[linha])):
            if forma[linha][coluna]:
                pos_x = (x + coluna * 30) // 30
                pos_y = (y + linha * 30) // 30

                # Verifica se a posição está fora dos limites da tela
                if (
                    pos_x < 0
                    or pos_x >= len(grid[0])
                    or pos_y >= len(grid)
                    or grid[pos_y][pos_x] != (0, 0, 0)
                ):
                    return True
    return False

def girar_forma(forma):
    return list(zip(*forma[::-1]))


def main():
    global grid

    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    x, y = largura // 2 - 15, 0
    forma_atual = criar_forma()
    cor_atual = cores_formas[formas.index(forma_atual)]
    velocidade_queda = 2
    tempo_queda = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 30
            if colisao(forma_atual, x, y, grid):
                x += 30
        if keys[pygame.K_RIGHT]:
            x += 30
            if colisao(forma_atual, x, y, grid):
                x -= 30
        if keys[pygame.K_DOWN]:
            y += 30
            if colisao(forma_atual, x, y, grid):
                y -= 30
   
        if keys[pygame.K_SPACE]:
            forma_atual = girar_forma(forma_atual)
        if not colisao(forma_atual, x, y + 30, grid):
            tempo_queda += 1
            if tempo_queda >= velocidade_queda:
                y += 30
                tempo_queda = 0
        else:
            # Bloqueia o bloco caso ele tenha chegado ao fim 
            for linha in range(len(forma_atual)):
                for coluna in range(len(forma_atual[linha])):
                    if forma_atual[linha][coluna]:
                        grid[(y + linha * 30) // 30][(x + coluna * 30) // 30] = cor_atual

            # Verifica se tem fileiras completas pra eliminar
            linhas_completas = []
            for linha in range(len(grid)):
                if all(c != (0, 0, 0) for c in grid[linha]):
                    linhas_completas.append(linha)
            for linha_completa in linhas_completas:
                del grid[linha_completa]
                grid.insert(0, [(0, 0, 0) for _ in range(10)])

            # Gere um novo bloco
            forma_atual = criar_forma()
            x, y = largura // 2 - 15, 0

        tela.fill(preto)
        desenhar_grade(tela)  # Desenhe a grade no fundo
        for linha in range(len(grid)):
            for coluna in range(len(grid[linha])):
                if grid[linha][coluna] != (0, 0, 0):
                    pygame.draw.rect(tela, grid[linha][coluna], (coluna * 30, linha * 30, 30, 30))
                    pygame.draw.rect(tela, preto, (coluna * 30, linha * 30, 30, 30), 2)

        desenhar_forma(forma_atual, x, y, cor_atual)

        pygame.display.update()
        clock.tick(5)

if __name__ == "__main__":
    main()
