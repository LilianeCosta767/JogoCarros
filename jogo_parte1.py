import pygame
pygame.init()

x = 300
y = 270
pos_x = 180
pos_y = 260
velocidade = 10
velocidade_outros = 15

fundo = pygame.image.load('tela.png')
carro = pygame.image.load('carro.png')
policia = pygame.image.load('car1.png')
ambulancia = pygame.image.load('car2.png')
taxi = pygame.image.load('car3.png')
carroPreto = pygame.image.load('car4.png')

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
    if comandos[pygame.K_UP]: # se a tecla de seta pra cima for pressionada
        y-=velocidade
    if comandos[pygame.K_DOWN]: # se a tecla de seta pra baixo for pressionada
        y+=velocidade
    if comandos[pygame.K_RIGHT]: # se a tecla de seta pra direita for pressionada
        x+=velocidade
    if comandos[pygame.K_LEFT]: # se a tecla de seta pra esquerda for pressionada
        x-=velocidade

    if (pos_y < -200):
        pos_y = 600

    pos_y -= velocidade_outros

    janela.blit(fundo, (0,0)) # a posição 0,0 começa no canto superior esquerdo da tela
    janela.blit(carro, (x,y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(ambulancia, (pos_x + 150, pos_y))
    janela.blit(taxi, (pos_x + 290, pos_y))

    pygame.display.update() # atualiza a tela depois criar o desenho 

pygame.quit()