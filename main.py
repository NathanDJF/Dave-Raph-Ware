import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

# images
main_menu_img = pygame.image.load(os.path.join('Assets/main menu.png'))
icon_img = pygame.image.load(os.path.join('Assets/icon.png'))

# vayriables
on_main_menu = True

# screenie
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Dave Raph Ware')
pygame.display.set_icon(icon_img)

# main loop
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    if on_main_menu:
        screen.blit(main_menu_img, (0, 0))
    if pygame.mouse.get_pressed()[0] == 1:
        screen.fill((255, 255, 255))
        on_main_menu = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()