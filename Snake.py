import pygame
import random
import time
import sys
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')
while True:
    food_x=random.randint(1,39)
    food_y=random.randint(1,29)
    food=pygame.Rect(food_x*20,food_y*20,20,20)
    snake_coordinates=[[0,0]]
    direction=''
    while True:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):sys.exit()
            if(event.type==pygame.KEYDOWN):
                if((event.key==pygame.K_w or event.key==pygame.K_UP) and direction!='down'):direction='up'
                elif((event.key==pygame.K_s or event.key==pygame.K_DOWN) and direction!='up'):direction='down'
                elif((event.key==pygame.K_a or event.key==pygame.K_LEFT) and direction!='right'):direction='left'
                elif((event.key==pygame.K_d or event.key==pygame.K_RIGHT) and direction!='left'):direction='right'
        previous_coordinate=[snake_coordinates[0][0],snake_coordinates[0][1]]
        if(direction=='up'):snake_coordinates[0][1]-=20
        elif(direction=='down'):snake_coordinates[0][1]+=20
        elif(direction=='left'):snake_coordinates[0][0]-=20
        elif(direction=='right'):snake_coordinates[0][0]+=20
        if(snake_coordinates[0][0]<0 or snake_coordinates[0][0]>800 or snake_coordinates[0][1]<0 or snake_coordinates[0][1]>600 or len(snake_coordinates)!=len(set(tuple(coordinate) for coordinate in snake_coordinates))):break
        if(snake_coordinates[0][0]==food.x and snake_coordinates[0][1]==food.y):
            food_x=random.randint(1,39)
            food_y=random.randint(1,29)
            food.topleft=(food_x*20,food_y*20)
            if(direction=='up'):snake_coordinates.append([snake_coordinates[-1][0],snake_coordinates[-1][1]+20])
            elif(direction=='down'):snake_coordinates.append([snake_coordinates[-1][0],snake_coordinates[-1][1]-20])
            elif(direction=='left'):snake_coordinates.append([snake_coordinates[-1][0]+20,snake_coordinates[-1][1]])
            elif(direction=='right'):snake_coordinates.append([snake_coordinates[-1][0]-20,snake_coordinates[-1][1]])
        for i in range(1,len(snake_coordinates)):
            current_coordinate=snake_coordinates[i]
            snake_coordinates[i]=previous_coordinate
            previous_coordinate=current_coordinate
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,255,255),food)
        for coordinate in snake_coordinates:pygame.draw.rect(screen,(255,255,255),pygame.Rect(coordinate[0],coordinate[1],20,20))
        time.sleep(0.05)
        pygame.display.update()
