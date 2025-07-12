import pygame
#2px=1cm
# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player1_pos = center.copy()
player2_pos = center.copy()
d_f_c=(140**2-100)**(1/2)
player1_pos.y += d_f_c-20 #plyusy nerqev minusy verev: nerqevi sumo
player2_pos.y -= d_f_c

while running:
    p1_dat1=player1_pos.copy()
    p1_dat2=player1_pos.copy()
    p1_dat3=player1_pos.copy()
    p1_dat4=player1_pos.copy()
    p1_dat5=player1_pos.copy()
    p1_dat1.x+=7 #paymanakan 3.5cm kentronic
    p1_dat1.y-=10
    p1_dat3.x-=7
    p1_dat3.y-=10
    p1_dat2.y-=10
    p1_dat4.x-=10
    p1_dat4.y-=4 #paymanakan 2cm kentronic
    p1_dat5.x+=10
    p1_dat5.y-=4
    p2_dat1=player1_pos.copy()
    p2_dat2=player1_pos.copy()
    p2_dat3=player1_pos.copy()
    p2_dat4=player1_pos.copy()
    p2_dat5=player1_pos.copy()
    p2_dat1.x+=7 #paymanakan 3.5cm kentronic
    p2_dat1.y+=10
    p2_dat3.x-=7
    p2_dat3.y+=10
    p2_dat2.y+=10
    p2_dat4.x+=10
    p2_dat4.y+=4 #paymanakan 2cm kentronic
    p2_dat5.x+=10
    p2_dat5.y+=4
    if player2_pos.x+10>=p1_dat1.x>=player2_pos.x-10:
        p1_dat1_v=abs(p1_dat1.y-p2_dat2.y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.circle(screen, "yellow", center, 300)
    pygame.draw.circle(screen, "white", center, 144)
    pygame.draw.circle(screen, "black", center, 140)
    # Draw rectangles centered at player positions
    pygame.draw.rect(screen, "red", (player1_pos.x-10, player1_pos.y, 20, 20))
    pygame.draw.rect(screen, "red", (player2_pos.x-10, player2_pos.y, 20, 20))
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
    if player2_pos.x+10>=player1_pos.x>=player2_pos.x-10 and player2_pos.y+10>=player1_pos.y>=player2_pos.y-10:
        player1_pos=ex_player1_pos.copy()
        player2_pos=ex_player2_pos.copy()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
