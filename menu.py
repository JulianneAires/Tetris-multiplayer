# importando bibliotecas
import pygame, sys
from button import Button

# inicializando o pygame
pygame.init()

# configurações de música
pygame.mixer.init()
pygame.mixer.music.load ("soundtrack/Original Tetris theme (Tetris Soundtrack).mp3")
pygame.mixer.music.set_volume (0.7)
pygame.mixer.music.play()
mute = False


#definindo tamanho e titulo da janela
largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))# "SCREEN"
pygame.display.set_caption("Menu") #título

# imagem de fundo (background)
fundo = pygame.image.load("imports/tetris.jfif")

# estilizando texto (fonte)
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("imports/font.ttf", size)

# na def PLAY bota a def do jogo prontinho.
'''
# função pra tudo funcionar 
def play():
    # laço infinito
    while True:
      #acionando omouse
        mouse = pygame.mouse.get_pos()
      #preenchendo a tela da janel com cor (preto)
        tela.fill("black")

        PLAY_BUTTON = Button(image=pygame.image.load("imports/botao-start.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
      
        PLAY_TEXT = get_font(45).render("tela de PLAY", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        tela.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()  
'''



# def para as opções do jogo
def options():
    global mute
    while True:
        # ativando funcionalidades do mouse
        mouse = pygame.mouse.get_pos()
        # preenchendo a tela coma cor preta
        tela.fill("Black")
      
        # definindo e posicionando texto na tela (respectivamente)
        OPC_TEXT = get_font(70).render("<OPÇÕES>", True, "White")
        OPC_RECT = OPC_TEXT.get_rect(center=(640, 100))
      
        # CRIANDO OS BOTÕES  (definindo: cor, font, tamanho, posição)
        # bt - mudo
        MUTE_BUTTON = Button(image=pygame.image.load("imports/botao-mudo.png"), pos=(640, 250), 
                            text_input=" MUTE", font=get_font(50), base_color="White", hovering_color="#000000")
        # bt - reiniciar
        REI_BUTTON = Button(image=pygame.image.load("imports/botao-sair.png"), pos=(640, 550), 
                            text_input="REINICIAR", font=get_font(50), base_color="White", hovering_color="#000000")
        # bt - sair
        SAIR_BUTTON = Button(image=pygame.image.load("imports/botao-sair.png"), pos=(640, 400), 
                            text_input="VOLTAR", font=get_font(50), base_color="White", hovering_color="#000000")
        # mostrar texto na tela (o 'blit' é tipo o 'print')
        tela.blit(OPC_TEXT, OPC_RECT)

        #FAZENDO ALGUMA COISA QUE NÃO SEI (AINDA)
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
                if MUTE_BUTTON.checkForInput(mouse):
                        if mute == False:
                             pygame.mixer.music.pause()
                             mute = True  
                        else:
                             pygame.mixer.music.unpause() 
                             mute = False                 
                if REI_BUTTON.checkForInput(mouse):
                        options() #reiniciar()
                if SAIR_BUTTON.checkForInput(mouse):
                        pygame.quit()
                        sys.exit()
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
        MENU_TEXT = get_font(80).render("MAIN MENU", True, "#FF69B4")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
      
        # CRIANDO OS BOTÕES  (definindo: cor, font, tamanho, posição)
        # bt - jogar
        PLAY_BUTTON = Button(image=pygame.image.load("imports/botao-start.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(50), base_color="White", hovering_color="#000000")
        # bt - opições
        OPTIONS_BUTTON = Button(image=pygame.image.load("imports/botao-opcao.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(50), base_color="White", hovering_color="#000000")
        # bt - sair
        QUIT_BUTTON = Button(image=pygame.image.load("imports/botao-sair.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(50), base_color="White", hovering_color="#000000")
      
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