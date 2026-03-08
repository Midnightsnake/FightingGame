import pygame

from dataclasses import dataclass

pygame.init()
display = pygame.display.set_mode((1920, 1080))
running = True
clock = pygame.time.Clock()
powers = {"Punch, Kick"}
land = pygame.Rect(0, 800, 2000, 200)
player1_outline = pygame.Rect(495, 495, 110, 110)
player2_outline = pygame.Rect(1195, 495, 110, 110)
player1 = pygame.Rect(500, 500, 100, 100)
player2 = pygame.Rect(1200, 500, 100, 100)
player1_health = 100
player2_health = 100
player1_healthoutline = pygame.Rect(495, 455, player1_health + 10, 30)
player2_healthoutline = pygame.Rect(1195, 455, player2_health + 10, 30)
player1_healthbar = pygame.Rect(500, 460, player1_health, 20)
player2_healthbar = pygame.Rect(1200, 460, player2_health, 20)

@dataclass
class Controls:
    left: int
    right: int
    up: int
    down: int
    #punch: int
    #kick: int

class Player:
    def __init__(self, x, y, controls):
        self.image = pygame.image.load("Fighter1.png")
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

player1 = Player(500, 500, Controls(
    left = pygame.K_a,
    right = pygame.K_d,
    up = pygame.K_w,
    down = pygame.K_s
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

    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(495, 45, player1.health + 10, 30))
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(500, 50, player1.health, 20))
    pygame.display.flip()
    clock.tick(240)