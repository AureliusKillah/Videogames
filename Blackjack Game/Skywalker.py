import pygame, sys, random
from pygame.locals import *


a = False
b = False
comienzo = True
verdadero = False

jugador = []
crupier = []

score1 = 0
score2 = 0
final = ''
iluminati = False
skywalker = 0

pygame.init()
reloj = pygame.time.Clock()


ventana = pygame.display.set_mode((800, 400), 0,32)

aliens = ['boton5.png','boton6.png']

botones = ['boton1.png','boton2.png','boton4.png']

cover = ['2T.png','3T.png','4T.png','5T.png','6T.png', '7T.png','8T.png',
         '9T.png','10T.png','AT.png','JT.png','KT.png','QT.png','2P.png',
         '3P.png','4P.png','5P.png','6P.png', '7P.png','8P.png','9P.png',
         '10P.png','AP.png','JP.png','KP.png','QP.png','2K.png','3K.png',
         '4K.png','5K.png','6K.png', '7K.png','8K.png','9K.png','10K.png',
         'AK.png','JK.png','KK.png','QK.png','2D.png','3D.png','4D.png',
         '5D.png','6D.png', '7D.png','8D.png','9D.png','10D.png','AD.png',
         'JD.png','KD.png','QD.png']

fuente = pygame.font.SysFont(None, 28)

objeto = pygame.Rect(300, 100, 200, 100)
objetojugador = pygame.Rect(100, 250, 65, 90)
objetocrupier = pygame.Rect(100, 50, 65, 90)
objetoboton = pygame.Rect(100, 350, 100, 30)

def dash():
    global cover
    cover = ['2T.png','3T.png','4T.png','5T.png','6T.png', '7T.png','8T.png',
             '9T.png','10T.png','AT.png','JT.png','KT.png','QT.png','2P.png',
             '3P.png','4P.png','5P.png','6P.png', '7P.png','8P.png','9P.png',
             '10P.png','AP.png','JP.png','KP.png','QP.png','2K.png','3K.png',
             '4K.png','5K.png','6K.png', '7K.png','8K.png','9K.png','10K.png',
             'AK.png','JK.png','KK.png','QK.png','2D.png','3D.png','4D.png',
             '5D.png','6D.png', '7D.png','8D.png','9D.png','10D.png','AD.png',
             'JD.png','KD.png','QD.png']

def dash2():
    global cover
    random.shuffle(cover)
    random.shuffle(cover)
    random.shuffle(cover)
    random.shuffle(cover)
    random.shuffle(cover)

def codigo(n=None):
    global imagen1,objetojugador,objetocrupier
    if n == None:
        imagen2 = pygame.transform.scale(imagen1, (65, 95))
        ventana.blit(imagen2,objetocrupier)
        pygame.display.update()
        reloj.tick(900000000)
        imagen1 = pygame.image.load(jugador[x])
        imagen2 = pygame.transform.scale(imagen1, (65, 95))
        ventana.blit(imagen2,objetojugador)
        pygame.display.update()
    if n == 1:
        if x == 0:
            objetojugador.x = 100
            objetocrupier.x = 100
        imagen2 = pygame.transform.scale(imagen1, (65, 95))
        ventana.blit(imagen2,objetocrupier)
        imagen1 = pygame.image.load(jugador[x])
        imagen2 = pygame.transform.scale(imagen1, (65, 95))
        ventana.blit(imagen2,objetojugador)
    
def variable(k=None):
    if k == None:
        if len(jugador) > len(crupier):
            return len(jugador)
        else:
            return len(crupier)

def contar(a):
    if len(a) == 7:
        return 10
    else:
        try:
            dry = int(a[0])
            return dry
        except:
            if a[0] != 'A':
                return 10
            else:
                return 11

def gta6():
    global score2,crupier,final,verdadero,iluminati
    if verdadero and final == '':
        while score2 < score1:
            trying = cover.pop()
            crupier.append(trying)
            score2 += contar(trying)
        else:
            if score2 > 21:
                final = fuente.render('Ganaste!',True, (255,255,255))
                iluminati = True
            else:
                if score2 == score1:
                    final = fuente.render('Empate',True, (255,255,255))
                    iluminati = True
                else:
                    final = fuente.render('el crupier tiene {}, Perdiste'.format(score2),True, (255,255,255))
                    iluminati = True
    else:
        if score1 == 21:
            final = fuente.render('Ganaste!',True, (255,255,255))
            iluminati = True
            verdadero = True
        elif score1 > 21:
            final = fuente.render('tienes {}, Perdiste'.format(score1),True, (255,255,255))
            iluminati = True
            verdadero = True

while True:
    for x in pygame.event.get():
        if x.type == QUIT:
            pygame.quit()
            sys.exit()
        if x.type == MOUSEBUTTONUP:
            if not a: 
                if (x.pos[0] in range(350,450)) and (x.pos[1] in range(200,235)):
                    a = True
            else:
                if (x.pos[0] in range(100,200)) and (x.pos[1] in range(350,380)):
                    if verdadero:
                        dash()
                        jugador = []
                        crupier = []
                        comienzo = True
                        score1 = 0
                        score2 = 0
                        verdadero = False
                        final = ''
                        iluminati = False
                    else:
                        trying = cover.pop()
                        score1 += contar(trying)
                        jugador.append(trying)
                        
                elif (x.pos[0] in range(250,350)) and (x.pos[1] in range(350,380)):
                    verdadero = True
                    iluminati = True
                
                elif (x.pos[0] in range(350,450)) and (x.pos[1] in range(350,380)) and (('AD.png' in jugador) or ('AK.png' in jugador) or ('AP.png' in jugador) or ('AT.png' in jugador)):
                    score1 -= 10
                    verdadero = True
                    iluminati = True

    ventana.fill((0,117,0))

    if a:
        if comienzo:
            dash2()
            while len(jugador) < 2:
                if len(crupier) != 0:
                    for x in range(len(jugador)):
                        if x == 0:
                            imagen1 = pygame.image.load('walker.png')
                            codigo()
                            objetojugador.x += 80
                            objetocrupier.x += 80 
                        else:
                            imagen1 = pygame.image.load(crupier[x])
                            codigo()
                            objetojugador.x = 100
                            objetocrupier.x = 100
                    else:
                        trying = cover.pop()
                        crupier.append(trying)
                        score2 += contar(trying)
                        trying = cover.pop()
                        jugador.append(trying)
                        score1 += contar(trying)                    
                else:
                    trying = cover.pop()
                    crupier.append(trying)
                    score2 += contar(trying)
                    trying = cover.pop()
                    jugador.append(trying)
                    score1 += contar(trying)   
            else:
                comienzo = False
        else:
            dk = variable()
            for x in range(dk):
                if x == 0:
                    if iluminati:
                        imagen1 = pygame.image.load(crupier[x])
                        codigo(1)
                        objetojugador.x += 80
                        objetocrupier.x += 80
                    else:
                        imagen1 = pygame.image.load('walker.png')
                        codigo(1)
                        objetojugador.x += 80
                        objetocrupier.x += 80
                else:
                    if len(jugador) != len(crupier):
                        if len(jugador) > len(crupier):
                            if x > (len(crupier) - 1):
                                imagen1 = pygame.image.load(jugador[x])
                                imagen2 = pygame.transform.scale(imagen1, (65, 95))
                                ventana.blit(imagen2,objetojugador)
                                if x != (len(jugador) - 1):
                                    objetojugador.x += 80
                            else:
                                imagen1 = pygame.image.load(crupier[x])
                                codigo(1)
                                objetojugador.x += 80
                                objetocrupier.x += 80
                        elif len(jugador) < len(crupier):
                            if x > (len(jugador) - 1):
                                imagen1 = pygame.image.load(crupier[x])
                                imagen2 = pygame.transform.scale(imagen1, (65, 95))
                                ventana.blit(imagen2,objetocrupier)
                                if x != (len(crupier) - 1):
                                    objetocrupier.x += 80
                            else:
                                imagen1 = pygame.image.load(crupier[x])
                                codigo(1)
                                objetojugador.x += 80
                                objetocrupier.x += 80
                    else:
                        if x == (len(jugador) - 1):
                            imagen1 = pygame.image.load(crupier[x])
                            imagen2 = pygame.transform.scale(imagen1, (65, 95))
                            ventana.blit(imagen2,objetocrupier)
                            imagen1 = pygame.image.load(jugador[x])
                            imagen2 = pygame.transform.scale(imagen1, (65, 95))
                            ventana.blit(imagen2,objetojugador)
                            objetojugador.x = 100
                            objetocrupier.x = 100
                        else:
                            imagen1 = pygame.image.load(crupier[x])
                            imagen2 = pygame.transform.scale(imagen1, (65, 95))
                            ventana.blit(imagen2,objetocrupier)
                            imagen1 = pygame.image.load(jugador[x])
                            imagen2 = pygame.transform.scale(imagen1, (65, 95))
                            ventana.blit(imagen2,objetojugador)
                            objetojugador.x += 80
                            objetocrupier.x += 80
            for x in botones:
                if not verdadero:
                    imagen = pygame.image.load(x)
                    boton = pygame.transform.scale(imagen, (100, 30))
                    ventana.blit(imagen,objetoboton)
                    if x == 'boton2.png' and (not (('AD.png' in jugador) or ('AK.png' in jugador) or ('AP.png' in jugador) or ('AT.png' in jugador))):
                        objetoboton.x = 100
                        break
                    else:
                        if x == 'boton4.png':
                            objetoboton.x = 100
                        else:
                            objetoboton.x += 150
                else:
                    imagen = pygame.image.load('boton3.png')
                    boton = pygame.transform.scale(imagen, (100, 30))
                    ventana.blit(imagen,objetoboton)

            Dx = fuente.render('{}'.format(score1),True, (255,255,255))
            score = imagen.get_rect()
            score.x = 60
            score.y = 250
            ventana.blit(Dx, score)

        gta6()
        if type(final) != type(''):
            ventana.blit(final,(100,190))
    else:
        objeto = pygame.Rect(300, 100, 200, 100)
        lol = pygame.image.load('Blackjack.jpg')
        ventana.blit(lol,objeto)
        objeto = pygame.Rect(350, 200, 100, 33)
        for x in aliens:
            lol = pygame.image.load(x)
            ventana.blit(lol,objeto)
            objeto.y += 50


    pygame.display.update()
    reloj.tick(600)