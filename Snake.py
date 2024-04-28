import pygame
import random
import sys
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
while True:
    score = 0
    food_x = random.randint(1,39)
    food_y = random.randint(1,29)
    food = pygame.Rect(food_x*20,food_y*20,20,20)
    snake_coordinates = [[0,0]]
    snake_direction = ''
    font = pygame.font.SysFont('Times new roman',28)
    while True:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
            if(event.type==pygame.KEYDOWN):
                if((event.key==pygame.K_w or event.key==pygame.K_UP) and snake_direction!='down'):
                    snake_direction = 'up'
                elif((event.key==pygame.K_s or event.key==pygame.K_DOWN) and snake_direction!='up'):
                    snake_direction = 'down'
                elif((event.key==pygame.K_a or event.key==pygame.K_LEFT) and snake_direction!='right'):
                    snake_direction = 'left'
                elif((event.key==pygame.K_d or event.key==pygame.K_RIGHT) and snake_direction!='left'):
                    snake_direction = 'right'
        score_display = font.render(f'Score: {score}',False,(255,255,255))
        previous_coordinate=[snake_coordinates[0][0],snake_coordinates[0][1]]
        if(snake_direction=='up'):
            snake_coordinates[0][1]-=20
        elif(snake_direction=='down'):
            snake_coordinates[0][1]+=20
        elif(snake_direction=='left'):
            snake_coordinates[0][0]-=20
        elif(snake_direction=='right'):
            snake_coordinates[0][0]+=20
        if(snake_coordinates[0][0]<0 or snake_coordinates[0][0]>800 or snake_coordinates[0][1]<0 or snake_coordinates[0][1]>600 or len(snake_coordinates)!=len(set(tuple(coordinate) for coordinate in snake_coordinates))):
            break
        if(snake_coordinates[0][0]==food.x and snake_coordinates[0][1]==food.y):
            score+=1
            food_x = random.randint(1,39)
            food_y = random.randint(1,29)
            food.topleft = (food_x*20,food_y*20)
            if(snake_direction=='up'):
                snake_coordinates.append([snake_coordinates[-1][0],snake_coordinates[-1][1]+20])
            elif(snake_direction=='down'):
                snake_coordinates.append([snake_coordinates[-1][0],snake_coordinates[-1][1]-20])
            elif(snake_direction=='left'):
                snake_coordinates.append([snake_coordinates[-1][0]+20,snake_coordinates[-1][1]])
            elif(snake_direction=='right'):
                snake_coordinates.append([snake_coordinates[-1][0]-20,snake_coordinates[-1][1]])
        for i in range(1,len(snake_coordinates)):
            current_coordinate = snake_coordinates[i]
            snake_coordinates[i] = previous_coordinate
            previous_coordinate = current_coordinate
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(128,0,0),food)
        for coordinate in snake_coordinates:
            pygame.draw.rect(screen,(0,128,0),pygame.Rect(coordinate[0],coordinate[1],20,20))
        screen.blit(score_display,(650,0))
        pygame.display.update()
        clock.tick(20)
