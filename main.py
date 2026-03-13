import pygame

from dataclasses import dataclass

pygame.init()
display = pygame.display.set_mode((1920, 1080))
running = True
clock = pygame.time.Clock()
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
        self.image = pygame.image.load("fighter1_default.png")
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.x = x
        self.y = y
        self.controls = controls
        self.health = 100
        self.speed = 1
        self.jumpheight = 10
        self.gravity = 1
        self.controls = controls
        self.attack = ""
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
        self.image = pygame.image.load("fighter1_punch.png")
        self.image = pygame.transform.scale(self.image, (400, 400))
        #For 1-2 seconds, it changes to this image then back to default
        #Check for hitbox, x-position difference to see if it hits,
        #y position for punch vs kick, -10 health once
        #potential blocking/dodging mechanics?

player1 = Player(350, 420, Controls(
    left = pygame.K_a,
    right = pygame.K_d,
    up = pygame.K_w,
    down = pygame.K_s
    punch = pygame.K_Q
    kick = pygame.K_E
    ))

player2 = Player(1200, 420, Controls(
    left = pygame.K_LEFT,
    right = pygame.K_RIGHT,
    up = pygame.K_UP,
    down = pygame.K_DOWN
    punch = pygame.K_Q
    kick = pygame.K_E
    ))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    display.fill((0, 200, 200))
    pygame.draw.rect(display, (100, 0, 0), land)

    player1.movement(keys)
    display.blit(player1.image, (player1.x, player1.y))

    player2.movement(keys)
    display.blit(player2.image, (player2.x, player2.y))

    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(315, 125, 410, 50))
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(320, 130, player1.health * 4, 40))
    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(1155, 125, 410, 50))
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(1160, 130, player2.health * 4, 40))
    pygame.display.flip()
    clock.tick(240)