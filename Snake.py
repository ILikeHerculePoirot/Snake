import pygame
import random
import sys
pygame.init()
screen=pygame.display.set_mode((1280,640))
pygame.display.set_caption('Snake')
clock=pygame.time.Clock()
while True:
    score=0
    food=pygame.Rect(random.randint(0,63)*20,random.randint(0,31)*20,20,20)
    snake_coordinates=[[640,320]]
    snake_direction=''
    font=pygame.font.SysFont('Times new roman',28)
    while True:
        turned=False
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
            if(event.type==pygame.KEYDOWN and (not turned)):
                if((event.key==pygame.K_w or event.key==pygame.K_UP) and snake_direction!='down'):
                    snake_direction='up'
                    turned=True
                if((event.key==pygame.K_s or event.key==pygame.K_DOWN) and snake_direction!='up'):
                    snake_direction='down'
                    turned=True
                if((event.key==pygame.K_a or event.key==pygame.K_LEFT) and snake_direction!='right'):
                    snake_direction='left'
                    turned=True
                if((event.key==pygame.K_d or event.key==pygame.K_RIGHT) and snake_direction!='left'):
                    snake_direction='right'
                    turned=True
        score_display=font.render(f'Score: {score}',False,(255,255,255))
        if(snake_coordinates[0][0]==food.x and snake_coordinates[0][1]==food.y):
            score+=1
            food.topleft=(random.randint(1,63)*20,random.randint(1,31)*20)
            if(snake_direction=='up'):
                snake_coordinates.append([snake_coordinates[-1][0],(snake_coordinates[-1][1]+20)%640])
            if(snake_direction=='down'):
                snake_coordinates.append([snake_coordinates[-1][0],(snake_coordinates[-1][1]+620)%640])
            if(snake_direction=='left'):
                snake_coordinates.append([(snake_coordinates[-1][0]+20)%1280,snake_coordinates[-1][1]])
            if(snake_direction=='right'):
                snake_coordinates.append([(snake_coordinates[-1][0]+1260)%1280,snake_coordinates[-1][1]])
        for i in range(len(snake_coordinates)-1,0,-1):
            snake_coordinates[i][0],snake_coordinates[i][1]=snake_coordinates[i-1][0],snake_coordinates[i-1][1]
        if(snake_direction=='up'):
            snake_coordinates[0][1]=(snake_coordinates[0][1]+620)%640
        if(snake_direction=='down'):
            snake_coordinates[0][1]=(snake_coordinates[0][1]+20)%640
        if(snake_direction=='left'):
            snake_coordinates[0][0]=(snake_coordinates[0][0]+1260)%1280
        if(snake_direction=='right'):
            snake_coordinates[0][0]=(snake_coordinates[0][0]+20)%1280
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(128,0,0),food)
        for coordinate in snake_coordinates:
            pygame.draw.rect(screen,(0,128,0),pygame.Rect(coordinate[0],coordinate[1],20,20))
        screen.blit(score_display,(1180,0))
        pygame.display.update()
        if(len(snake_coordinates)!=len(set(tuple(coordinate) for coordinate in snake_coordinates))):
            break
        clock.tick(15)
