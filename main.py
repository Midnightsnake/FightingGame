import pygame

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player1_outline.x -= 1
        player1.x -= 1
        player1_healthoutline.x -= 1
        player1_healthbar.x -= 1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player1_outline.x += 1
        player1.x += 1
        player1_healthoutline.x += 1
        player1_healthbar.x += 1
    if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        player1_outline.y -= 1
        player1.y -= 1
        player1_healthoutline.y -= 1
        player1_healthbar.y -= 1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player1_outline.y += 1
        player1.y += 1
        player1_healthoutline.y += 1
        player1_healthbar.y += 1
    display.fill((0, 200, 200))
    pygame.draw.rect(display, (100, 0, 0), land)
    pygame.draw.rect(display, (0, 0, 0), player1_outline)
    pygame.draw.rect(display, (0, 0, 0), player2_outline)
    pygame.draw.rect(display, (0, 0, 255), player1)
    pygame.draw.rect(display, (255, 0, 0), player2)
    pygame.draw.rect(display, (0, 0, 0), player1_healthoutline)
    pygame.draw.rect(display, (0, 0, 0), player2_healthoutline)
    pygame.draw.rect(display, (0, 255, 0), player1_healthbar)
    pygame.draw.rect(display, (0, 255, 0), player2_healthbar)
    pygame.display.flip()
    clock.tick(240)