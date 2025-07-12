import pygame  # type: ignore

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player1_pos = center.copy()
player2_pos = center.copy()
player1_pos.y += 50
player2_pos.y -= 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.circle(screen, "yellow", center, 300)
    pygame.draw.circle(screen, "black", center, 170)
    pygame.draw.circle(screen, "red", center, 150)
    # Draw rectangles centered at player positions
    pygame.draw.rect(screen, "blue", (player1_pos.x, player1_pos.y, 10, 10))
    pygame.draw.rect(screen, "blue", (player2_pos.x, player2_pos.y, 10, 10))
    ex_player1_pos= player1_pos.copy()
    ex_player2_pos=player2_pos.copy()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player2_pos.y -= 100 * dt
    if keys[pygame.K_s]:
        player2_pos.y += 100 * dt
    if keys[pygame.K_a]:
        player2_pos.x -= 100 * dt
    if keys[pygame.K_d]:
        player2_pos.x += 100 * dt
    if keys[pygame.K_i]:
        player1_pos.y -= 100 * dt
    if keys[pygame.K_k]:
        player1_pos.y += 100 * dt
    if keys[pygame.K_j]:
        player1_pos.x -= 100 * dt
    if keys[pygame.K_l]:
        player1_pos.x += 100 * dt
    if player2_pos.x+8>=player1_pos.x>=player2_pos.x-8 and player2_pos.y+8>=player1_pos.y>=player2_pos.y-8:
        player1_pos=ex_player1_pos.copy()
        player2_pos=ex_player2_pos.copy()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
