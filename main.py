import pygame

from dataclasses import dataclass

pygame.init()
display = pygame.display.set_mode((1920, 1080))
font1 = pygame.font.SysFont(None, 32)
font2 = pygame.font.SysFont(None, 52)
text1 = font1.render("Settings", True, (0, 0, 0))
text2 = font2.render("Settings (Incomplete)", True, (0, 0, 0))
text3 = font1.render("Tutorial", True, (0, 0, 0))
text4 = font1.render("Characters", True, (0, 0, 0))
running = True
clock = pygame.time.Clock()
settings_visible = False
character = 1
#8 different possible characters to choose from, each with 2 unique powers
powers = {"Punch, Kick"}
land = pygame.Rect(0, 800, 2000, 200)

@dataclass
class Controls:
    left: int
    right: int
    up: int
    down: int
    punch: int
    kick: int

class Player:
    def __init__(self, x, y, controls):
        self.image_default = pygame.image.load("fighter1_default.png")
        self.image_default = pygame.transform.scale(self.image_default, (400, 400))
        self.image_punch = pygame.image.load("fighter1_punch.png")
        self.image_punch = pygame.transform.scale(self.image_punch, (400, 400))
        self.image_kick = pygame.image.load("fighter1_kick.png")
        self.image_kick = pygame.transform.scale(self.image_kick, (400, 400))
        self.image = self.image_default
        self.attack_time = 0
        self.currently_attacking = False
        self.x = x
        self.y = y
        self.controls = controls
        self.health = 100
        self.speed = 1
        self.jumpheight = 10
        self.gravity = 1
        self.controls = controls
    def movement(self, keys):
        if keys[self.controls.left]:
            self.x -= 1
        if keys[self.controls.right]:
            self.x += 1
        if keys[self.controls.up]:
            self.y -= 1
        if keys[self.controls.down]:
            self.y += 1
    def attack(self, keys):

        if keys[self.controls.punch] and self.currently_attacking == False:
            self.currently_attacking = True
            self.image = self.image_punch
            self.attack_time = 60

        if keys[self.controls.kick] and self.currently_attacking == False:
            self.currently_attacking = True
            self.image = self.image_kick
            self.attack_time = 60
        if self.attack_time > 0:
            self.attack_time -= 1
        else:
            self.image = self.image_default
            self.currently_attacking = False

player1 = Player(350, 420, Controls(
    left = pygame.K_a,
    right = pygame.K_d,
    up = pygame.K_w,
    down = pygame.K_s,
    punch = pygame.K_q,
    kick = pygame.K_e,
    ))

player2 = Player(1200, 420, Controls(
    left = pygame.K_LEFT,
    right = pygame.K_RIGHT,
    up = pygame.K_UP,
    down = pygame.K_DOWN,
    punch = pygame.K_q,
    kick = pygame.K_e,
    ))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if settings_rect.collidepoint(mousepos):
                settings_visible = True
    keys = pygame.key.get_pressed()
    
    display.fill((0, 200, 200))
    pygame.draw.rect(display, (100, 0, 0), land)

    player1.movement(keys)
    display.blit(player1.image, (player1.x, player1.y))

    player1.attack(keys)

    player2.movement(keys)
    display.blit(player2.image, (player2.x, player2.y))

    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(365, 125, 410, 50))
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(370, 130, player1.health * 4, 40))
    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(1145, 125, 410, 50))
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(1150, 130, player2.health * 4, 40))
    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(220, 125, 110, 110))
    settings_rect = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(225, 130, 100, 100))
    display.blit(text1, (230, 165))
    if settings_visible == True:
        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(615, 120, 460, 660))
        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(620, 125, 450, 650))
        display.blit(text2, (650, 170))
        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(625, 220, 110, 110))
        pygame.draw.rect(display, (0, 255, 255), pygame.Rect(630, 225, 100, 100))
        display.blit(text3, (640, 260))
        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(625, 340, 110, 110))
        pygame.draw.rect(display, (0, 150, 255), pygame.Rect(630, 345, 100, 100))
        display.blit(text4, (640, 380))
    pygame.display.flip()
    clock.tick(240)