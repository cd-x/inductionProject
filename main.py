import pygame
import time
import random

pygame.init()

display_width=800

display_height=600

white=(255,255,255)

black=(0,0,0)

red=(255,0,0)

green=(0,255,0)

car_width=50

car_height=56


gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Wrong Way(Rajrishi)')

clock=pygame.time.Clock()



carImg=pygame.image.load('f1small.png')

enemyImg1=pygame.image.load('black_small.png')

enemyImg2=pygame.image.load('yellow_trans.png')

enemyImg3=pygame.image.load('pink_small.png')

enemyImg4=pygame.image.load('orange_sport.png')

enemyImg5=pygame.image.load('redsmall.png')


def things_passed(count):
    font=pygame.font.SysFont("comicsansms",25)
    text =font.render("Passed: "+str(count),True,green)
    gameDisplay.blit(text,(0,0))



def car(x,y):
    gameDisplay.blit(carImg,(x,y))

#def things(thingx,thingy,thingw,thingh,color):
    #pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def things(thingx,thingy,enemyImg):
    gameDisplay.blit(enemyImg,(thingx,thingy))

    
def text_objects(text,font):
    textSurface = font.render(text,True,red)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('ARDESTINE.ttf',100)
    TextSurf,TextRect =text_objects(text,largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.8)


    x_change=0

    count=0

    thing_startx=random.randrange(0,display_width)
    thing2_startx=random.randrange(0,display_width)
    thing3_startx=random.randrange(0,display_width)
    thing4_startx=random.randrange(0,display_width)
    thing5_startx=random.randrange(0,display_width)
    
    y_change=0

    
    thing_starty=-500
    thing2_starty=-400
    thing3_starty=-600
    thing4_starty=10000
    thing5_starty=2000
    
    thing_speed=7
    thing2_speed=5
    thing3_speed=8
    thing4_speed=3
    thing5_speed=1
    
    thing_width=50
    thing_height=96
    thing2_width=100
    thing2_height=200
    thing3_width=58
    thing3_height=100

    thing4_width=42
    thing4_height=100
    thing5_width=38
    thing5_height=70
   
    gameExit = False
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type== pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5

                elif event.key ==pygame.K_UP:
                    y_change=-3
                elif event.key ==pygame.K_DOWN:
                    y_change=3
#upper movement handling
            if event.type ==pygame.KEYUP:
                if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
                if event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change=0

               
                
        x=x+x_change
        y=y+y_change
     
        gameDisplay.fill(white)

        #things(thingx,thingy,thingw,thingh,color)
        #things(thing_startx,thing_starty,thing_width,thing_height,black)

        things(thing_startx,thing_starty,enemyImg1)
        things(thing2_startx,thing2_starty,enemyImg2)
        things(thing3_startx,thing3_starty,enemyImg3)
        things(thing4_startx,thing4_starty,enemyImg4)
        things(thing5_startx,thing5_starty,enemyImg5)

        thing_starty+=thing_speed
        thing2_starty+=thing2_speed
        thing3_starty+=thing3_speed
        thing4_starty+=thing4_speed
        thing5_starty+=thing5_speed

        car(x,y)

        things_passed(count)
        
        pygame.display.update()
        
        if x<0 or x+car_width>display_width or y<0 or y+car_height>display_height:
                crash()
                
        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            count+=1

        if thing2_starty>display_height:
            thing2_starty=0-thing2_height
            thing2_startx=random.randrange(0,display_width)
            count+=1

        if thing3_starty>display_height:
            thing3_starty=0-thing3_height
            thing3_startx=random.randrange(0,display_width)
            count+=1

        if thing4_starty>display_height:
            thing4_starty=0-thing4_height
            thing4_startx=random.randrange(0,display_width)
            count+=1

        if thing5_starty>display_height:
            thing5_starty=0-thing5_height
            thing5_startx=random.randrange(0,display_width)
            count+=1 


        if y<thing_starty+thing_height and y>thing_starty and x+car_width>thing_startx and x<thing_startx:
            crash()
        if y<thing_starty+thing_height and y>thing_starty and x+car_width>thing_startx+thing_width and x<thing_startx+thing_width:
            crash()

        if y<thing2_starty+thing2_height and y>thing2_starty and x+car_width>thing2_startx and x<thing2_startx:
            crash()
        if y<thing2_starty+thing2_height and y>thing2_starty and x+car_width>thing2_startx+thing2_width and x<thing2_startx+thing2_width:
            crash()
        if y<thing2_starty+thing2_height and x>thing2_startx and x<thing2_startx+thing2_width and y+car_height>thing2_starty:
            crash()

        if y<thing3_starty+thing3_height and y>thing3_starty and x+car_width>thing3_startx and x<thing3_startx:
            crash()
        if y<thing3_starty+thing3_height and y>thing3_starty and x+car_width>thing3_startx+thing3_width and x<thing3_startx+thing3_width:
            crash()

        if y<thing4_starty+thing4_height and y>thing4_starty and x+car_width>thing4_startx and x<thing4_startx:
            crash()
        if y<thing4_starty+thing4_height and y>thing4_starty and x+car_width>thing4_startx+thing4_width and x<thing4_startx+thing4_width:
            crash()

        if y<thing5_starty+thing5_height and y>thing5_starty and x+car_width>thing5_startx and x<thing5_startx:
            crash()
        if y<thing5_starty+thing3_height and y>thing5_starty and x+car_width>thing5_startx+thing5_width and x<thing5_startx+thing5_width:
            crash()
 
 

               
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
       

    
