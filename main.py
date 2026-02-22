import pygame

pygame.init()
display = pygame.display.set_mode((1920, 1080))
running = True
clock = pygame.time.Clock()
player1 = pygame.Rect(500, 500, 50, 50)
player2 = pygame.Rect(1200, 500, 50, 50)
player1_health = 100
player2_health = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1.x -= 1
    if keys[pygame.K_d]:
        player1.x += 1
    if keys[pygame.K_SPACE]:
        player1.y -= 1
    display.fill((255, 255, 255))
    pygame.draw.rect(display, (0, 0, 255), player1)
    pygame.draw.rect(display, (255, 0, 0), player2)
    pygame.display.flip()
    clock.tick(240)