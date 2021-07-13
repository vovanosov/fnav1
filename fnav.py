import pygame, pygame.mixer
import random
import time

def inter1 (x1, y1, x2, y2, db1, db2):
    if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db1 and y1 < y2 + db2:
        return 1
    else:
        return 0

def inter (x1, y1, x2, y2, db1, db2, ds): #Пересечение двух объектов. В основном это для нажатия кнопок
    if x1 > x2 - db1 and x1 < x2 + db2 and y2 < ds + y1:
        return 1
    else:
        return 0
        
def inter2 (x1, y1, x2, y2, db1, db2, db3):
    if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db3 and y1 < y2 + db3:
        return 1
    else:
        return 0

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((1280,720),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.Surface((1280,720))
myroom = pygame.image.load("./data/myroom.png")
cambutton = pygame.image.load("./data/cambutton.png")
planshet = pygame.image.load("./data/planshet.png")
vova = pygame.image.load("./data/vova.png")
lose = pygame.image.load("./data/lose.png")
napad = pygame.image.load("./data/napad.png")
mask = pygame.image.load("./data/mask.png")
maskbut = pygame.image.load("./data/maskbut.png")
baterry = pygame.image.load("./data/baterry.png")
palka = pygame.image.load("./data/pal.png")
warning = pygame.image.load("./data/warning.png")
red = pygame.image.load("./data/red.png")
am = pygame.image.load("./data/6am.png")
nachalo = pygame.image.load("./data/Begin.png")
phone = pygame.image.load("./data/phone.png")
win = pygame.image.load("./data/win.png")
gameover = pygame.image.load("./data/gameover.png")


videofile = []
video = []
videofilea = []
videoa = []

j = [1,2,3,4,5,6,7,8,9,10]

for gg in range (0, 10):
    video.append(gg)
    videoa.append(gg)

for g in range (0, 10):
    videofile.append("./data/"+ str(j[g]) +".png")
    video[g] = pygame.image.load(videofile[g])
    videofilea.append("./data/a"+ str(j[g]) +".png")
    videoa[g] = pygame.image.load(videofilea[g])
    
poz = []

for g in range (0, 10):
    poz.append(True)

Begin = True #Пока Begin = True программа работает
cam = False # цикл Камера

cambutton.set_colorkey((0,255,0))
planshet.set_colorkey((0,255,0))
mask.set_colorkey((0,255,0))
maskbut.set_colorkey((0,255,0))
baterry.set_colorkey((0,255,0))
warning.set_colorkey((0,255,0))

vovapoz = 9 #Вовина позиция в камере
pv = 1

losee = False

maska = 1

def button():
    pygame.mixer.init()
    button = pygame.mixer.Sound('./data/button.wav')
    button.play()




toks = 0 #Токсичность

batt = 3000
batt2 = 6

clock = 0 #время


level = 1
levell = 1

xpal = []
palind = 280
kolpal = 5

for i in range (0,6):
    palind += 24
    xpal.append(palind)

beg = True #пока beg = True цикл меню будет работать

f = open("./data/xxx.txt", "r")
levell = f.read()
f.close()

level = int(levell)

pygame.mixer.init()
gamebegin = pygame.mixer.Sound('./data/begin.wav')
gamebegin.play(loops=-1)


while beg == True: #цикл меню
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONUP: #Нажатие клавиши мыши
            x,y = e.pos
           
            if inter2 (x,y,272,200,1,250,30): #Нажатие кнопки "новая игра"
                button() #звук кнопки
                beg = False #Выход из цикла меню
                level = 1 #возвращаемся в 1 ночь
                levell = level
                f = open("./data/xxx.txt", "w")
                f.write(str(levell))
                f.close()
                
                num = pygame.font.SysFont('monospace', 50)
                night = num.render('Night: ' + str(level) , True, (255, 255, 255))
                
                screen.fill ((0,0,0))
                screen.blit(night, (500,350))
                window.blit(screen, (0,0))
                pygame.display.update()
                #time.sleep (3)
                
                gamebegin = pygame.mixer.stop()
                
            if inter2 (x,y,256,326,1,266,30): #Нажатие кнопки продолжить
                beg = False
                button()
                num = pygame.font.SysFont('monospace', 50)
                night = num.render('Night: ' + str(level) , True, (255, 255, 255))
                screen.fill ((0,0,0))
                screen.blit(night, (500,350))
                window.blit(screen, (0,0))
                pygame.display.update()
                time.sleep (3)
                
                gamebegin = pygame.mixer.stop()
                
            if inter2 (x,y,326,569,1,144,30): #Нажатие кнопки выход
                beg = False
                Begin = False
            
    screen.fill ((255,255,255))
    screen.blit(nachalo, (0,0))
    window.blit(screen, (0,0))
    pygame.display.update()
    
    
if level == 1:
    nspeed = 1000
if level == 2:
    nspeed = 800
if level == 3:
    nspeed = 600
if level == 4:
    nspeed = 400
if level == 5:
    nspeed = 200
    
speed = nspeed #Скорость передвижения Вовы равна nspeed


if level == 1: # Оператор разговаривает с тобой в 1 ночь
    pygame.mixer.init()
    night1 = pygame.mixer.Sound('./data/Night1.wav')
    night1.play() 
      
    
    
if level == 2: # Оператор разговаривает с тобой в 2 ночь
    pygame.mixer.init()
    night1 = pygame.mixer.Sound('./data/Night2.wav')
    night1.play() 
      
     
    
if level == 3: # Оператор разговаривает с тобой в 3 ночь
    pygame.mixer.init()
    night1 = pygame.mixer.Sound('./data/Night3.wav')
    night1.play() 
      
    
    
if level == 4: # Оператор разговаривает с тобой в 4 ночь
    pygame.mixer.init()
    night1 = pygame.mixer.Sound('./data/Night4.wav')
    night1.play() 
      
   
  
pygame.mixer.init()
buzzlight = pygame.mixer.Sound('./data/buzzlight.wav')
buzzlight.play(loops=-1) 

xphone = 1000 # X кнопки "завершить разговор"
  
menu = False # При выигрыше или проигрыше, вы возвращаетесь в меню и menu = True

class room(): #Хозяин дачи сидит у себя в комнате

    while Begin == True:
        for j in pygame.event.get():
            if j.type == pygame.KEYUP and j.key == pygame.K_ESCAPE:
               Begin = False
           
                
            if j.type == pygame.MOUSEBUTTONUP: #Нажатие клавиши мыши
               x,y = j.pos
               
               if inter2 (x, y, 300, 10, 1, 562, 60): #Кнопка "маска"
                    maska += 1 
                    if maska % 2 == 0: #Маска надета
                        pygame.mixer.init()
                        nadmask = pygame.mixer.Sound('./data/nadmask.wav')
                        nadmask.play()
                        
                    if maska % 2 != 0: #Маска снята
                        pygame.mixer.init()
                        snmask = pygame.mixer.Sound('./data/snmask.wav')
                        snmask.play()
                        
                        
               if inter2 (x, y, 1000, 100, 1, 190, 84): #Вы завершили разговор
                    xphone = 10000
                    night1 = pygame.mixer.stop()
                    buzzlight.play(loops=-1) 

               
               if inter2 (x, y, 300, 625, 1, 562, 60) and maska % 2 != 0: #Вы нажали на кнопку "камера"
                    button()
                    
                    cam = True
                    
                    if maska % 2 == 0:
                        maska += 1
                   
                    
                    while cam == True: #Вы зашли в камеру
                        for jj in pygame.event.get():
                            if jj.type == pygame.MOUSEBUTTONUP:
                               x,y = jj.pos
                        
                               if inter (x, y, 300, 625, 1, 562, 30): 
                                    button()
                                    cam = False
                               
                               if inter1 (x, y, 26, 58, 1, 77): #Button camera 1
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[0] = True
                                    
                               if inter1 (x, y, 146, 58, 1, 77): #Button camera 2
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[1] = True
                                    
                               if inter1 (x, y, 26, 151, 1, 77): #Button camera 3
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[2] = True
                                    
                               if inter1 (x, y, 146, 151, 1, 77): #Button camera 4
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[3] = True
                                    
                               if inter1 (x, y, 26, 250, 1, 77): #Button camera 5
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[4] = True
                                    
                               if inter1 (x, y, 146, 250, 1, 77): #Button camera 6
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[5] = True
                                    
                               if inter1 (x, y, 26, 350, 1, 77): #Button camera 7
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[6] = True
                                    
                               if inter1 (x, y, 146, 350, 1, 77): #Button camera 8
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[7] = True
                                    
                               if inter1 (x, y, 26, 450, 1, 77): #Button camera 9
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[8] = True
                                    
                               if inter1 (x, y, 146, 450, 1, 77): #Button camera 10
                                    button()
                                    for ii in range (0, 10):
                                        poz[ii] = False
                                    poz[9] = True
                                     
                        
                        
                        pv += 1
                        
                            
                        speed = nspeed 
                        
                        
                                
                        if vovapoz == -2:
                            cam = False
                            
                        
                            
                        if pv % speed == 0:
                            vovapoz -= 1
                            if vovapoz < -2:
                                vovapoz = 9
                           
                        batt -= 1
        
                        if batt % 500 == 0:
                            batt2 = batt // 500
                            
                           
                            
                        if batt2 <= 0:
                            cam = False
                            
                        clock += 1
                            
                        num = pygame.font.SysFont('monospace', 100)
                        cl = num.render('' + str(clock//4000) + " AM" , True, (0, 0, 0))
                        
                        if clock // 4000 == 6:
                            cam = False
                          
                        if toks != 0 and maska % 2 != 0:
                            toks -= 1                          
                        
                        screen.fill ((0,140,0)) 
                       
                        
                        
                        for i in range (0, 10):
                            
                            
                            if poz[i] == True and vovapoz == i:
                                screen.blit(videoa[i], (0,0))
                                num = pygame.font.SysFont('monospace', 50)
                                cammera = num.render('' + str(i+1) , True, (0, 0, 0))
                                
                            if poz[i] == True and vovapoz == i and i == 2:
                                
                                screen.blit(baterry, (300,400))
                                
                                if inter1 (x,y,300,400,1,150) and batt2 < 6: #Нажатие на кнопку зарядки батареи
                                    pygame.mixer.init()
                                    box = pygame.mixer.Sound('./data/Blip3.wav')
                                    box.play()
                                    batt2 += 1
                                    batt += 500
                                    x = 0
                                    y = 0
                                    
                               
                                for i in range (0,batt2):
                                    screen.blit(palka, (xpal[i],405))
                                
                                
                            if poz[i] == True and vovapoz != i:
                                screen.blit(video[i], (0,0))
                                num = pygame.font.SysFont('monospace', 50)
                                cammera = num.render('' + str(i+1) , True, (0, 0, 0))
                                
                                if i == 2:
                                    
                                    if inter1 (x,y,300,400,1,150) and batt2 < 6: #Нажатие на кнопку зарядки батареи
                                        pygame.mixer.init()
                                        box = pygame.mixer.Sound('./data/Blip3.wav')
                                        box.play()
                                        batt2 += 1
                                        batt += 500
                                        x = 0
                                        y = 0
                                        
                                        
                                    
                                    screen.blit(baterry, (300,400))
                                   
                                    
                                    for i in range (0,batt2):
                                        screen.blit(palka, (xpal[i],405))
                                    
                            
                            
                                    
                        if batt2 <= 3:
                            screen.blit(warning, (1100,600))   
                        
                        
                        screen.blit(planshet, (0,0))
                        screen.blit(cambutton, (300,625))
                        screen.blit(red, (1000,50))
                        screen.blit(cl, (1000,42))
                        screen.blit(cammera, (1200,145))
                        
                        window.blit(screen, (0,0))
                        pygame.display.update()
                            
        batt -= 1
        
        
        
        if batt % 500 == 0:
            batt2 = batt // 500
                        
        if vovapoz != -2:
            pv += 1
            if pv % speed == 0:
                vovapoz -= 1
                
       
                #if vovapoz < -1:
                #    vovapoz = 9
                
        if toks != 0 and maska % 2 != 0:
            toks -= 1
        
        num = pygame.font.SysFont('monospace', 50)
        toksic = num.render('' + str(toks) , True, (237, 28, 36))
        
        clock += 1
        
        if clock // 4000 == 6:
            menu = True
            buzzlight = pygame.mixer.pause()
            level += 1
            levell = level
            f = open("./data/xxx.txt", "w")
            f.write(str(levell))
            f.close()
            pygame.mixer.init()
            pygame.mixer.music.load("./data/clok.wav")
            pygame.mixer.music.play()
            screen.blit(am, (0,0))
            window.blit(screen, (0,0))
            pygame.display.update()
            time.sleep (10)
            
            clock = 0
            
            if level == 6:
                pygame.mixer.init()
                winn = pygame.mixer.Sound('./data/win.wav')
                winn.play() 
                level -= 1
                levell = level
                f = open("./data/xxx.txt", "w")
                f.write(str(levell))
                f.close()
                screen.blit(win, (0,0))
                window.blit(screen, (0,0))
                pygame.display.update()
                time.sleep(24)
                winn = pygame.mixer.stop()
                  
                
            
           
            
            
        screen.fill ((0,140,0)) 
        
        
        if vovapoz == -1: # Вова у вас в комнате
            screen.blit(napad, (0,0))
            screen.blit(cambutton, (300,625))
            screen.blit(maskbut, (300,10))
            
            
        if vovapoz == -2 and maska % 2 == 0: #Вова ушел из комнаты
            vovapoz = random.randint(1,4)
            
        if vovapoz == -2 or batt2 <= 0: # Если батарея закончилась или вова рядом с вами то вы умираете
            menu = True
            pygame.mixer.init()
            buzzlight = pygame.mixer.pause()
            pygame.mixer.init()
            pygame.mixer.music.load("./data/Scream.wav")
            pygame.mixer.music.play()
            cam = False
            screen.blit(lose, (0,0))
            window.blit(screen, (0,0))
            pygame.display.update()
            time.sleep (3)
            
            pygame.mixer.init()
            pygame.mixer.music.load("./data/gameover.wav")
            pygame.mixer.music.play()
            screen.blit(gameover, (0,0))
            
            window.blit(screen, (0,0))
            pygame.display.update()
            time.sleep (5)
            pygame.mixer.music.stop()
                        
        if vovapoz > -1: 
            screen.blit(myroom, (0,0))
            screen.blit(cambutton, (300,625))
            screen.blit(maskbut, (300,10))
            
        if maska % 2 == 0: #Вы надели маску 
        
            toks += 1 # токсичность начинает повышаться
            screen.blit(mask, (0,0)) 
            screen.blit(maskbut, (300,10))
            screen.blit(toksic, (300,140)) 
            
            if toks == 1500: #Если токсичность равна 1500 то вы умираете
                menu = True
                pygame.mixer.init()
                buzzlight = pygame.mixer.pause()
                pygame.mixer.init()
                pygame.mixer.music.load("./data/Scream.wav")
                pygame.mixer.music.play()
                cam = False
                screen.blit(lose, (0,0))
                window.blit(screen, (0,0))
                pygame.display.update()
                time.sleep (3)
                
                pygame.mixer.init()
                pygame.mixer.music.load("./data/gameover.wav")
                pygame.mixer.music.play()
                screen.blit(gameover, (0,0))
                
                window.blit(screen, (0,0))
                pygame.display.update()
                time.sleep (5)
                pygame.mixer.music.stop()
               
                
                
        if menu == True: # При выигрыше или проигрыше вы возвращаетесь в меню
            menu = False
            poz = []

            for g in range (0, 10):
                poz.append(True)

            Begin = True #Пока Begin = True программа работает
            cam = False

            vovapoz = 9
            pv = 1

            losee = False

            maska = 1

            def button():
                pygame.mixer.init()
                button = pygame.mixer.Sound('./data/button.wav')
                button.play()


            nspeed = 200
            speed = nspeed

            toks = 0

            batt = 3000
            batt2 = 3000

            clock = 0

            
            beg = True
            
            pygame.mixer.init()
            gamebegin = pygame.mixer.Sound('./data/begin.wav')
            gamebegin.play(loops=-1)
            
            batt = 3000
            batt2 = 6
            
            xpal = []
            palind = 280
            
            xphone = 1000

            for i in range (0,6):
                palind += 24
                xpal.append(palind)
            
            while beg == True:
                for e in pygame.event.get():
                    if e.type == pygame.MOUSEBUTTONUP: #Нажатие клавиши мыши
                        x,y = e.pos
                       
                        if inter2 (x,y,272,200,1,250,30): #Нажатие кнопки "новая игра"
                            button() #звук кнопки
                            beg = False #Выход из цикла меню
                            level = 1 #возвращаемся в 1 ночь
                            levell = level
                            f = open("./data/xxx.txt", "w")
                            f.write(str(levell))
                            f.close()
                            
                            num = pygame.font.SysFont('monospace', 50)
                            night = num.render('Night: ' + str(level) , True, (255, 255, 255))
                            
                            screen.fill ((0,0,0))
                            screen.blit(night, (500,350))
                            window.blit(screen, (0,0))
                            pygame.display.update()
                            #time.sleep (3)
                            
                            gamebegin = pygame.mixer.stop()
                            
                        if inter2 (x,y,256,326,1,266,30): #Нажатие кнопки продолжить
                            beg = False
                            button()
                            num = pygame.font.SysFont('monospace', 50)
                            night = num.render('Night: ' + str(level) , True, (255, 255, 255))
                            screen.fill ((0,0,0))
                            screen.blit(night, (500,350))
                            window.blit(screen, (0,0))
                            pygame.display.update()
                            time.sleep (3)
                            
                            gamebegin = pygame.mixer.stop()
                            
                        if inter2 (x,y,326,569,1,144,30): #Нажатие кнопки выход
                            beg = False
                            Begin = False
                        
                screen.fill ((255,255,255))
                screen.blit(nachalo, (0,0))
                window.blit(screen, (0,0))
                pygame.display.update()
                
                
                
            if level == 1:
                nspeed = 1000
            if level == 2:
                nspeed = 800
            if level == 3:
                nspeed = 600
            if level == 4:
                nspeed = 400
            if level == 5:
                nspeed = 200
            speed = nspeed
            
            if level == 1:
                pygame.mixer.init()
                night1 = pygame.mixer.Sound('./data/Night1.wav')
                night1.play() 
                  
                
                
            if level == 2:
                pygame.mixer.init()
                night1 = pygame.mixer.Sound('./data/Night2.wav')
                night1.play() 
                  
                 
                
            if level == 3:
                pygame.mixer.init()
                night1 = pygame.mixer.Sound('./data/Night3.wav')
                night1.play() 
                  
                
                
            if level == 4:
                pygame.mixer.init()
                night1 = pygame.mixer.Sound('./data/Night4.wav')
                night1.play() 
                  
                
            
            pygame.mixer.init()
            buzzlight = pygame.mixer.Sound('./data/buzzlight.wav')
            buzzlight.play(loops=-1)
                
        if batt2 <= 3:
            screen.blit(warning, (1100,600)) 
            
            
        screen.blit(phone, (xphone,100))
        window.blit(screen, (0,0))
        pygame.display.update()
    

	