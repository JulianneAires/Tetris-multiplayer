# importando bibliotecas
import pygame, sys
from button import Button
from tetrisnet import play

# inicializando o pygame
pygame.init()

# configurações de música
'''pygame.mixer.init()
pygame.mixer.music.load ("soundtrack/Original Tetris theme (Tetris Soundtrack).mp3")
pygame.mixer.music.set_volume (0.7)
pygame.mixer.music.play()
mute = False'''

#definindo tamanho e titulo da janela
largura = 400
altura = 600
tela = pygame.display.set_mode((largura, altura))  # "SCREEN"
pygame.display.set_caption("Tetris Menu")  #título

# imagem de fundo (background)
fundo = pygame.image.load("imports/backgroundMenu.png")


# estilizando texto (fonte)
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("imports/font.ttf", size)


# def para as opções do jogo
def options():
    while True:
        # ativando funcionalidades do mouse
        mouse = pygame.mouse.get_pos()
        # preenchendo a tela coma cor preta
        #tela.fill("Black")
        fundoopc = pygame.image.load("imports/backgroundMenu.png")
        tela.blit(fundoopc, (0, 0))


        # definindo e posicionando texto na tela (respectivamente)
        OPC_TEXT = get_font(50).render("OPTIONS", True, "#A898E9")
        OPC_RECT = OPC_TEXT.get_rect(center=(200, 90))

        # CRIANDO OS BOTÕES  (definindo: cor, font, tamanho, posição)
        # bt - mudo
        MUTE_BUTTON = Button(image=pygame.image.load("imports/buttonBlue.png"),
                             pos=(200, 200),
                             text_input="MUTE",
                             font=get_font(28),
                             base_color="White",
                             hovering_color="#000000")
        # bt - reiniciar
        REI_BUTTON = Button(
            image=pygame.image.load("imports/buttonPurple.png"),
            pos=(200, 300),
            text_input="RESTART",
            font=get_font(28),
            base_color="White",
            hovering_color="#000000")
        
        # bt - sair
        SAIR_BUTTON = Button(
            image=pygame.image.load("imports/buttonYellow.png"),
            pos=(200, 400),
            text_input="BACK",
            font=get_font(28),
            base_color="White",
            hovering_color="#000000")
        
        # mostrar texto na tela (o 'blit' é tipo o 'print')
        tela.blit(OPC_TEXT, OPC_RECT)

        #muda a cor da fonte dos botoes qnd o mouse passa por cima
        for button in [MUTE_BUTTON, REI_BUTTON, SAIR_BUTTON]:
            button.changeColor(mouse)
            #atualizando tela
            button.update(tela)

        # quando apertar o X a janela se fecha
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # chamando funções
            if event.type == pygame.MOUSEBUTTONDOWN:

                # mutar
                if MUTE_BUTTON.checkForInput(mouse):
                    if mute == False:
                        pygame.mixer.music.pause()
                        mute = True
                    else:
                        pygame.mixer.music.unpause()
                        mute = False

                #reiniciar o jogo
                if REI_BUTTON.checkForInput(mouse):
                    play()

                if SAIR_BUTTON.checkForInput(mouse):
                    main_menu ()
                    
            #atualizando a tela
            pygame.display.update()


#def para menu
def main_menu():
    while True:
        # colorindo tela de fundo
        tela.blit(fundo, (0, 0))
        # acionando mouse
        mouse = pygame.mouse.get_pos()
        # definindo e posicionando texto na tela (respectivamente)
        MENU_TEXT = get_font(50).render("MENU", True, "#A898E9")
        MENU_RECT = MENU_TEXT.get_rect(center=(200, 90))

        # CRIANDO OS BOTÕES  (definindo: cor, font, tamanho, posição)
        # bt - jogar
        PLAY_BUTTON = Button(
            image=pygame.image.load("imports/buttonBlue.png"),
            pos = (200, 200),
            text_input="PLAY",
            font=get_font(28),
            base_color="White",
            hovering_color="#000000")
        
        # bt - opições
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("imports/buttonPurple.png"),
            pos=(200, 300),
            text_input="OPTIONS",
            font=get_font(28),
            base_color="White",
            hovering_color="#000000")
        # bt - sair
        QUIT_BUTTON = Button(image=pygame.image.load("imports/buttonYellow.png"),
                             pos=(200, 400),
                             text_input="QUIT",
                             font=get_font(28),
                             base_color="White",
                             hovering_color="#000000")

        # mostrar texto na tela (o 'blit' é tipo o 'print')
        tela.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse)

            #atualizando tela
            button.update(tela)

    # quando apertar o X a janela se fecha e está chamando as funções
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse):
                    play()
                if OPTIONS_BUTTON.checkForInput(mouse):
                    options()
                if QUIT_BUTTON.checkForInput(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
