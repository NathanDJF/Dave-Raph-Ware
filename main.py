import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

# images
main_menu_img = pygame.image.load(os.path.join('Assets/main menu.png'))
icon_img = pygame.image.load(os.path.join('Assets/icon.png'))
play_button_img = pygame.image.load(os.path.join('Assets/play button.png'))
life_img = pygame.image.load(os.path.join("Assets/life.png"))

# variables
on_main_menu = True
lives_active = False

# screen setup
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Dave Raph Ware')
pygame.display.set_icon(icon_img)

# button class
class Button():
    def __init__(self, x, y, img, allowed):
        self.x = x
        self.y = y
        self.img = img
        self.rect = img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.allowed = allowed
        
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            
            if pygame.mouse.get_pressed()[0] == 0 and self.allowed:
                self.clicked = False
                
        screen.blit(self.img, (self.x, self.y))
        
        return action

# lives class
class Lives():
    def __init__(self, num, image):
        self.num = num
        self.image = image
        self.nums = [lives for lives in range(self.num)]
        self.clicked = False 

    def draw(self):
        screen.fill((255, 255, 255), (300, 450, 600, 100))
        for i, life in enumerate(self.nums):
            screen.blit(self.image, (400 + (i * 100), 450))

        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            if self.nums:
                del self.nums[0]
                print(self.nums)
            self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
play_button = Button(450, 475, play_button_img, False)
lives = Lives(5, life_img)

# main loop
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    
    if on_main_menu:
        screen.blit(main_menu_img, (0, 0))
        if play_button.draw():
            pygame.time.wait(500)
            screen.fill((255, 255, 255))
            on_main_menu = False
            lives_active = True
            
    if lives_active:
        lives.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
