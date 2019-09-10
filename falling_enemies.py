# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:32:53 2019

@author: mdeepan

Falling Enemies - Escape wisely
"""

import pygame
import sys
import random

pygame.init()

width = 800
height = 600
player_size = 50
player_pos = [width/2, height-1.5*player_size]
enemy_size = 50
enemy_pos = [random.randint(0, width - enemy_size), 0]
screen = pygame.display.set_mode((width, height))
enemy_list = [enemy_pos]
speed = 5
game_over = False
clock = pygame.time.Clock()
score = 0
var = 50
myfont = pygame.font.SysFont("monospace", 35)

def set_level(score, speed):
    speed = score/5 + 2
    return speed

def create_enemies(enemy_list, var):
    if speed < 5:
        level = 0.1
    else:
        level = speed/var
    if len(enemy_list) <= 10 and random.random() < level:
        enemy_list.append([random.randint(0, width - enemy_size), 0])
        
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (0,0,255), (enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

def drop_enemies(enemy_list, score, speed):
    for idx, enemy_pos in enumerate(enemy_list):
        if (enemy_pos[0] > 0 and enemy_pos[1] < height):
            enemy_pos[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_checker(enemy_list):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    
    if ((e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size))):
        if ((e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size))):
            print("Found collision")
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x,y]
    
    screen.fill((0,0,0)) 
    
    create_enemies(enemy_list, var)
    draw_enemies(enemy_list)
    speed = set_level(score, speed)
    score = drop_enemies(enemy_list, score, speed)   
    print(str(score)+", "+str(speed))
    text = "Score: " + str(score)
    label = myfont.render(text, 1, (255,255,0))
    screen.blit(label, (width-200, height-40))
    
    if collision_checker(enemy_list):
        game_over = True
    
    pygame.draw.rect(screen, (255,0,0), (player_pos[0],player_pos[1],player_size,player_size))
    clock.tick(25)
    pygame.display.update()
    
