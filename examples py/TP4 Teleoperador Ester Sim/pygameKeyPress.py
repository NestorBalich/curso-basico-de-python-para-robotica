# -*- coding: UTF-8 -*-
#28-10-2022 teleoperador de robot para simulador Ester Sim
#utilizando clase de comunicacion apicom_EsterSim
#by Nestor Balich
from class_apicom_EsterSim import *
import pygame
import keyboard
import os

#configuramos variables de entorno
url_server = 'http://8.219.78.29:8000/Ester' #sevidor de api no modificar
apikey = "acc$2g1" #apiKey no modificar
user_id ="Grupo UAI" #usario habilitado no modificar

robot_id = "robot0"  #ingresa numero de robot
robot_name = "mi_nombre" #ingresa tu nombre

# lee la clave la primera vez y la guarda en un archivo
rb = apicom_EsterSim(url_server,apikey,user_id,robot_id,robot_name,True)
robot_key = rb.get_object_key()

# si ya tenes la clave poder descomentar esta linea y ponerla manualmente
#robot_key ='50c472b0-52ea-11ed-95db-53b7051d344d'

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
vel = 5

run = True
while run:
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
        
           

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        rb.req_put(robot_key,"izquierda","10")
        print("izquierda")
    if keys[pygame.K_DOWN] :
        rb.req_put(robot_key,"derecha","10")
        print("derecha")
    if keys[pygame.K_UP] :
        rb.req_put(robot_key,"izquierda","10")
        print("izquierda")
    if keys[pygame.K_LEFT] :
        rb.req_put(robot_key,"retroceder","10")
        print("retroceder")
    if keys[pygame.K_RIGHT] :
        rb.req_put(robot_key,"avanzar","10")
        print("avanzar")
    if keys[pygame.K_p] :
        rb.req_put(robot_key,"patada","50")
        print("patada")
    
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        
    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.flip()

pygame.quit()
exit()