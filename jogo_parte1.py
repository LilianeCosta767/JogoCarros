import pygame
from random import randint
pygame.init()
# limite direita = 450
# limite esquerda = 150
x = 300
y = 100
pos_x = 180
pos_y_policia = 300
pos_y_ambulancia = 700
pos_y_carroPreto = 1500
timer = 0
tempo_segundo = 0

velocidade = 20
velocidade_outros = 20

fundo = pygame.image.load('tela.png')
carro = pygame.image.load('carro.png')
policia = pygame.image.load('car1.png')
ambulancia = pygame.image.load('car2.png')
taxi = pygame.image.load('car3.png')
carroPreto = pygame.image.load('car4.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect() # retangulo atrás do texto
pos_texto.center = 65,50

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while(janela_aberta):
    pygame.time.delay(50) # tempo para executar o código
    # criando a condição de fechar a janela
    for event in pygame.event.get(): # para com um evento
        if event.type == pygame.QUIT:
            janela_aberta = False
        
    # criando a movimentação
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 440: # se a tecla de seta pra direita for pressionada
        x+=velocidade
    if comandos[pygame.K_LEFT] and x >= 160: # se a tecla de seta pra esquerda for pressionada
        x-=velocidade

    # detecta colisão
    if((x-50 < pos_x and pos_y_policia == y)):
        # y - 1200
        exit()

    # posição dos carros animados
    if (pos_y_policia < -200) and (pos_y_ambulancia < -200) and (pos_y_carroPreto < -200):
        pos_y_policia = randint(700, 1000)
        pos_y_ambulancia = randint(1300, 2000)
        pos_y_carroPreto = randint(2300, 3000)

    if(timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y_policia -= velocidade_outros
    pos_y_ambulancia -= velocidade_outros + 2
    pos_y_carroPreto -= velocidade_outros + 10

    janela.blit(fundo, (0,0)) # a posição 0,0 começa no canto superior esquerdo da tela
    janela.blit(carro, (x,y))
    janela.blit(policia, (pos_x, pos_y_policia))
    janela.blit(ambulancia, (pos_x + 150, pos_y_ambulancia))
    janela.blit(carroPreto, (pos_x + 290, pos_y_carroPreto))
    janela.blit(texto,pos_texto)

    pygame.display.update() # atualiza a tela depois criar o desenho 

pygame.quit()