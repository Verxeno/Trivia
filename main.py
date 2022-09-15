import time
import random
play = True
trys = 0
points = 0
listp = []
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[39m'
nombre=input('Ingresa tu nombre: ')
time.sleep(0.5)
print('\nHola',BLUE+nombre+RESET)
time.sleep(1)
print('\nBienvenido a la trivia de computación')
time.sleep(1.3)
print('\nPondremos a prueba tu conocimiento sobre los componentes y ajustes para que una PC tenga un buen desempeño')

while play == True:
  trys += 1
  points = 0
  time.sleep(1.3)
  print('\nSi quieres armar una PC sin comprar una tarjeta gráfica, cual tendrías que escoger:\n')
  print('1 - i9-12900K')
  print('2 - i9-12900F')
  print('3 - i9-12900KF\n')
  res =input("Escriba la respuesta: ")
  while res not in ('1','2','3'):
    res = input(YELLOW+"\nLa respuesta no esta entre las opciones, Vuelve a responder: "+RESET)
  if(res == '1'):
    points=points+10
    print(GREEN+'\nCorrecto la i9-12900K tiene gráficos integrados UHD Intel® 770'+RESET)
  else:
    print(RED+'\nIncorrecto'+RESET)
  time.sleep(1.3)
  
  print('\nSi quieres sacarle el mayor rendimiento a tus memorias RAM que se tendría que activar en la BIOS')
  print('\n1 - DLSS\n2 - DOCP\n3 - XRT\n4 - XMP')
  res = input("\nEscriba la respuesta: ")
  while res not in ('1','2','3','4'):
    res = input(YELLOW+"\nLa respuesta no esta entre las opciones, Vuelve a responder: "+RESET)
  if(res == '2' or res == '4'):
    points=points+10
    print(GREEN+'\nCorrecto este ajuste permite que la memoria RAM trabaje con su velocidad máxima'+RESET)
  else:
    points=points+0
    print(RED+'\nIncorrecto'+RESET)
  time.sleep(0.5)
  print(BLUE+'\nConseguiste',points,'puntos!'+RESET,'\n\nIntento', trys)
  print('\nQuieres lanzar los dados y aumentar tu puntaje?',YELLOW+'\nTen cuidado también puede restar tu puntaje'+RESET)
  luck=input('\nSi / No: ').lower()
  while luck not in('si','no'):
    luck=input('Dije. Si / No: ')
  if(luck == 'si'):
    dice = random.randint(-5,5)
    tpoints=points+dice
    listp.append(tpoints)
    listpoint=sum(listp)
    print(BLUE+'\nConseguiste',dice,'puntos con los dados\n\nTu puntaje total es',tpoints,RESET)
    print('\nTu puntaje Total de intentos: ',listpoint)
  else:
    listp.append(points)
    listpoint=sum(listp)
    print('\nTu puntaje Total de intentos: ',listpoint)
  replay=input('\nQuieres intentarlo nuevamente? si / no: ').lower()
  while replay not in('si','no'):
    print(YELLOW+'\nDije. Quieres intentarlo nuevamente? '+RESET)
    replay=input('SI/NO: ').lower()
  if(replay != 'si'):
    print('\nEspero que te hayas divertido')
    listp = []
    play = False