import pygame
import time
import sys
import random

pygame.init()
pygame.mixer.init()

white = (255, 255, 255)
brack = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

display_width = 800
display_height = 559
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption("추억의 게임")


clock = pygame.time.Clock()


def background():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/오프닝.png"), (0,0))

def background1():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/학교 운동장.png"), (0,0))

def background2():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/배경.jpg"), (0,0))

def background3():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/문구1.png"), (0,0))

def background4():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/문방구1.jpg"),(0,0))

def background5():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/공.png"), (0, 0))

def background6():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/오버1.png"), (0, 0))

def background7():
    gameDisplay.blit(pygame.image.load("/Users/peach/myenv/오버2.png"), (0, 0))
    
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(txt, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("malgungothic", 20)
    textSurf, textRect = text_objects(txt, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    sys.exit()

def introScreen():
    pygame.mixer.music.load("/Users/peach/myenv/사운드.mp3")
    pygame.mixer.music.play(-1)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        background()

        button("시작", 150, 450, 100, 50, green, orange, gameScreen)
        button("종료", 550, 450, 100, 50, red, orange, quitgame)

        pygame.display.update()
        clock.tick(15)

def gameScreen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("/Users/peach/myenv/학교벨소리 2.mp3")
    pygame.mixer.music.play(0)
    

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()        

        import time
        startTime = time.time()
        while(True):
            nowTime = time.time()
            if nowTime-startTime >=0 and nowTime-startTime <=8:
                gameDisplay.fill(white)
                background1()
                pygame.display.update()
                
            elif nowTime-startTime > 8 and nowTime-startTime <=9:
                img_bg = pygame.image.load("/Users/peach/myenv/배경.jpg")
                img_chara = [
                    pygame.image.load("/Users/peach/myenv/사람.png"),
                    pygame.image.load("/Users/peach/myenv/사람1.png")
                ]
                
                tmr = 0
                while True :
                    tmr = tmr +1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    x = tmr % 60
                    for g in range(1):
                        gameDisplay.blit(img_bg, [g*60-x, 0])
                    gameDisplay.blit(img_chara[tmr%2], [520, 240])
                    pygame.display.update()
                    clock.tick(5)
                    if g*60-x == 0:
                        break
                       
            else : 
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quitgame()

                    gameDisplay.fill(white)
                    background3() 
                    button("START", 350, 300, 100, 50, orange, blue, gameScreen1)  
                    pygame.display.update()
                    clock.tick(15)




def gameScreen1():
    
    pygame.mixer.music.load("/Users/peach/myenv/소리.mp3")
    pygame.mixer.music.play(-1)
   
    x_change=0
    character = pygame.image.load("/Users/peach/myenv/사람1.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (display_width/10)-(character_width/2)
    character_y_pos = display_height - (character_height*1.1)
    character1 = pygame.image.load("/Users/peach/myenv/사람.png")
    character1_size = character1.get_rect().size
    character2= pygame.image.load("/Users/peach/myenv/사람2.png")
    character2_size = character2.get_rect().size
    character2_width = character2_size[0]
    character2_height = character2_size[1]
    character2_x_pos = display_width*0.727
    character2_y_pos = display_height*0.55
    character3 = pygame.image.load("/Users/peach/myenv/사람3.png")
    character3_size = character3.get_rect().size
    character3_width = character3_size[0]
    character3_height = character3_size[1]
    character3_x_pos = display_width*0.727
    character3_y_pos = display_height*0.55
    import time
    startTime = time.time()
     
    gameExit = False

    while not gameExit:
        gameDisplay.fill(white)
        background4()
        nowTime = time.time()
        if nowTime-startTime>30:
            if character_x_pos < display_width*0.64:
                gameScreen4()
                pygame.display.update()
            
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    
                    x_change = 3
                
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    
                    x_change = 0
                    
                
            
        keys = pygame.key.get_pressed()
         
        if keys[pygame.K_SPACE]:
            if keys[pygame.K_RIGHT]:
                gameScreen3()
                pygame.display.update()
            
        if keys[pygame.K_SPACE]:
            gameDisplay.blit(character2, (character2_x_pos, character2_y_pos))
            gameDisplay.blit(character, (character_x_pos, character_y_pos))
        
        elif keys[pygame.K_RIGHT]:
            gameDisplay.blit(character1, (character_x_pos, character_y_pos))
            gameDisplay.blit(character3, (character3_x_pos, character3_y_pos))
        else:
            gameDisplay.blit(character, (character_x_pos, character_y_pos))
            gameDisplay.blit(character3, (character3_x_pos, character3_y_pos))
        character_x_pos += x_change
        pygame.display.update()  
    
            
     
        
       
        
     

        
    
        if character_x_pos>=display_width*0.64:
            gameScreen2()
            pygame.display.update()
        
        
        
        
            
       
        

def gameScreen2():
    
    pygame.mixer.music.stop()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quitgame()
        gameDisplay.fill(white)
        background5()
        

        button("다시", 150, 450, 100, 50, green, orange, gameScreen1)
        button("종료", 550, 450, 100, 50, red, orange, quitgame)
        pygame.display.update()
        
        clock.tick(15)
        
def gameScreen3():
    
    pygame.mixer.music.stop()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quitgame()
        
        gameDisplay.fill(white)
        background6()
        

        button("다시", 150, 450, 100, 50, green, orange, gameScreen1)
        button("종료", 550, 450, 100, 50, red, orange, quitgame)
        pygame.display.update()
        
        clock.tick(15)
       
                                   
def gameScreen4():
    pygame.mixer.music.stop()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quitgame()
        gameDisplay.fill(white)
        background7()

        button("다시", 150, 450, 100, 50, green, orange, gameScreen1)
        button("종료", 550, 450, 100, 50, red, orange, quitgame)
        pygame.display.update()
        
        clock.tick(15)
        
    

introScreen()
