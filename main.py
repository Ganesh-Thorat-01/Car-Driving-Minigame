import pygame
import random

def main_menu():
    global screen2
    pygame.init()
    screen2=pygame.display.set_mode((467,598))
    pygame.display.set_caption("Car Driving")
    icon=pygame.image.load("Images\\icon.ico")
    pygame.display.set_icon(icon)
    screen2.fill((0,0,0))

    font_menu=pygame.font.Font("freesansbold.ttf",30)
    text_menu=font_menu.render("M A I N   M E N U",True,"white")
    textRect_menu=text_menu.get_rect()
    textRect_menu.center=(250,200)

    font_exit=pygame.font.Font("freesansbold.ttf",30)
    text_exit=font_exit.render("E X I T",True,"white","black")
    textRect_exit=text_exit.get_rect()
    textRect_exit.center=(250,300)

    font_start=pygame.font.Font("freesansbold.ttf",30)
    text_start=font_start.render("S T A R T",True,"white","sky blue")
    textRect_start=text_start.get_rect()
    textRect_start.center=(250,260)

    running2=True
    while running2:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running2=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_KP_ENTER or event.key==pygame.K_RIGHT:
                    running2=False
                    gameloop()
                
                if event.key==pygame.K_DOWN:
                    running2=False
                    
        screen2.blit(text_menu,textRect_menu)
        screen2.blit(text_start,textRect_start)
        screen2.blit(text_exit,textRect_exit)
        
        pygame.display.update()


def Car():
    global car_x

    screen.blit(car,(car_x,380))
    if car_x<=30:
        car_x=50
    if car_x>=330:
        car_x=330

def barrier():
    global barrier_y,barrier_x,barrier_list,running,score,HI
    time1=5
    screen.blit(barrier_img,(barrier_x,barrier_y))
    barrier_y+=0.9
    if barrier_y>=598:
        barrier_y=-180
        barrier_x=random.choice(barrier_list)

    if car_x>=barrier_x-70 and car_x<=barrier_x+170 and barrier_y>=360 and barrier_y<=590 :
        running=False
        if score>HI:
            HI=score

        gameover()
    
def gameover():

    pygame.display.set_caption("Car Driving")
    screen1 = pygame.display.set_mode((467, 598))
    time1=5
    font_over=pygame.font.Font("freesansbold.ttf",30)
    text_over=font_over.render("G A M E  O V E R",True,"blue")
    textRect_over=text_over.get_rect()
    textRect_over.center=(233,299)
    running1=True
    while running1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running1=False
        screen1.blit(bgimg,(0,0))
        screen1.blit(text_over,textRect_over)
        screen1.blit(score_text,(180,340))
        
        time1-=0.003
        if time1<0:
            running1=False
            main_menu()
        pygame.display.update()
        
        
def background():
    global screen,bg_y,bg_y1

    screen.blit(bgimg,(0,bg_y))
    screen.blit(bgimg1,(0,bg_y1))
    screen.blit(score_text,score_rect)
    screen.blit(HI_text,HI_rect)
    bg_y+=0.9
    bg_y1+=0.9

    if bg_y>=598:
        bg_y=-598
    if bg_y1>=598:
        bg_y1=-598


def gameloop():
    global screen,bgimg,bgimg1,car,running,car_x,barrier_img,barrier_y,barrier_x,barrier_list
    global bg_y,bg_y1,game_over_text,over_rect,score_text,score_rect,score,HI,HI_text,HI_rect
    pygame.init()
    
    pygame.display.set_caption("Car Driving")
    screen=pygame.display.set_mode((467 ,598))
    car=pygame.image.load("Images\\Car.png")
    car=pygame.transform.scale(car,(100,210))
    bgimg=pygame.image.load("Images\\Road.jpg")
    bgimg1=bgimg
    
    barrier_img=pygame.image.load("Images\\Barrier.png")
    barrier_img=pygame.transform.scale(barrier_img,(170,30))

    score_font=pygame.font.Font("freesansbold.ttf",30)
    score_text=score_font.render(f"Score: {int(score)}",True,"red")
    score_rect=score_text.get_rect()
    score_rect.center=(350,30)

    HI_font=pygame.font.Font("freesansbold.ttf",30)
    HI_text=HI_font.render(f"HI: {int(HI)}",True,"red")
    HI_rect=HI_text.get_rect()
    HI_rect.center=(330,70)


    bg_y=0
    bg_y1=-598
    car_x=80
    barrier_y=-20
    barrier_x=45
    barrier_list=[45,250]
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    car_x+=75
                if event.key==pygame.K_LEFT:
                    car_x-=75
                if event.key==pygame.K_ESCAPE:
                    running=False
                    main_menu()
        score+=0.006
        if score>HI:
            HI=score
        score_text=score_font.render(f"Score: {int(score)}",True,"red")
        HI_text=HI_font.render(f"HI: {int(HI)}",True,"red")
        background()
        Car()
        barrier()
        pygame.display.update()
score=0
HI=0
main_menu()