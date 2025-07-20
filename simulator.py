import pygame
import math
from math import sin,cos
# 4px = 1cm
cm = 4
def is_point_in_rotated_square(point, center, angle, side_length = 10 * cm):
    # Step 1: Translate point relative to center
    rel_x = point.x - center.x
    rel_y = point.y - center.y

    # Step 2: Unrotate the point
    cos_a = math.cos(-angle)
    sin_a = math.sin(-angle)
    unrotated_x = rel_x * cos_a - rel_y * sin_a
    unrotated_y = rel_x * sin_a + rel_y * cos_a

    # Step 3: Check if inside axis-aligned square
    half_side = side_length / 2
    return (-half_side <= unrotated_x <= half_side) and (-half_side <= unrotated_y <= half_side)

def calculate_dat_value(dat_pos, center, angle, step):
    length = 0
    point = dat_pos.copy()
    for i in range(1000):
        point.x -= step * sin(angle) * cm
        point.y -= step * cos(angle) * cm
        length += step
        if is_point_in_rotated_square(point, center, angle):
            return length
    return None

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True
dt = 0

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player1_pos = center.copy()
player2_pos = center.copy()

d_f_c = ((70 * cm) ** 2 - (50 * cm)) ** 0.5
player1_pos.y += d_f_c - 5 * cm
player2_pos.y -= d_f_c - 5 * cm

score = [0 , 0]

alfa = 0
beta = 0

start_time = pygame.time.get_ticks()  # Get time in milliseconds

p1_dat1_value = []
p1_dat2_value = []
p1_dat3_value = []
p1_dat4_value = []
p1_dat5_value = []

p2_dat1_value = []
p2_dat2_value = []
p2_dat3_value = []
p2_dat4_value = []
p2_dat5_value = []

while running:
    # Convert degrees to radians
    alfa_r = math.radians(alfa)
    beta_r = math.radians(beta)

    ex_player1_pos = player1_pos.copy()
    ex_player2_pos = player2_pos.copy()
    ex_alfa = alfa
    ex_beta = beta

    alfa_r=math.radians(alfa)
    beta_r=math.radians(beta)

    p1_dat2=player1_pos.copy()
    p2_dat2=player2_pos.copy()

    p2_dat2.x += 5 * cm * math.sin(beta_r)
    p2_dat2.y += 5 * cm * math.cos(beta_r)
    
    p1_dat2.x -= 5 * cm * math.sin(alfa_r)
    p1_dat2.y -= 5 * cm * math.cos(alfa_r)
    
    p1_dat1 = p1_dat2.copy()
    p1_dat3 = p1_dat2.copy()
    p2_dat1 = p2_dat2.copy()
    p2_dat3 = p2_dat2.copy()

    p1_dat1.x -= 3.5 * cm * cos(alfa_r) #paymanakan 3.5cm kentronic
    p1_dat1.y += 3.5 * cm * sin(alfa_r)
    p1_dat3.x += 3.5 * cm * cos(alfa_r)
    p1_dat3.y -= 3.5 * cm * sin(alfa_r)

    p2_dat1.x += 3.5 * cm * cos(beta_r)
    p2_dat1.y -= 3.5 * cm * sin(beta_r)
    p2_dat3.x -= 3.5 * cm * cos(beta_r)
    p2_dat3.y += 3.5 * cm * sin(beta_r)

    p1_dat4=player1_pos.copy()
    p1_dat4.x += 5 * cm * cos(alfa_r) - 3 * sin(alfa_r) * cm
    p1_dat4.y -= 5 * cm * sin(alfa_r) + 3 * cos(alfa_r) * cm #paymanakan 2cm kentronic
    p1_dat5=p1_dat4.copy()
    p1_dat5.x -= 10 * cm * cos(alfa_r)
    p1_dat5.y += 10 * cm * sin(alfa_r)
    

    p2_dat4=player2_pos.copy()
    p2_dat4.x -= 5 * cm * cos(beta_r) - 3 * sin(beta_r) * cm
    p2_dat4.y += 5 * cm * sin(beta_r) + 3 * cos(beta_r) * cm #paymanakan 2cm kentronic
    p2_dat5=p2_dat4.copy()
    p2_dat5.x += 10 * cm * cos(beta_r)
    p2_dat5.y -= 10 * cm * sin(beta_r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player2_pos.y -= 50 * cm * dt * math.cos(beta_r)
        player2_pos.x -= 50 * cm * dt * math.sin(beta_r)
    if keys[pygame.K_w]:
        player2_pos.y += 50 * cm * dt * math.cos(beta_r)
        player2_pos.x += 50 * cm * dt * math.sin(beta_r)
    if keys[pygame.K_a]:
        beta += 1
    if keys[pygame.K_d]:
        beta -= 1
    if keys[pygame.K_i]:
        player1_pos.y -= 50 * cm * dt * math.cos(alfa_r)
        player1_pos.x -= 50 * cm * dt * math.sin(alfa_r)
    if keys[pygame.K_k]:
        player1_pos.y += 50 * cm * dt * math.cos(alfa_r)
        player1_pos.x += 50 * cm * dt * math.sin(alfa_r)
    if keys[pygame.K_j]:
        alfa += 1
    if keys[pygame.K_l]:
        alfa -= 1

    # Drawing
    screen.fill("white")
    pygame.draw.circle(screen, "yellow", center, 100 * cm)
    pygame.draw.circle(screen, "white", center, 72 * cm)
    pygame.draw.circle(screen, "black", center, 70 * cm)

    #Datchiks
    #pygame.draw.circle(screen, "white", p1_dat1, 2)
    #pygame.draw.circle(screen, "white", p1_dat2, 2)
    #pygame.draw.circle(screen, "white", p1_dat3, 2)
    #pygame.draw.circle(screen, "white", p1_dat4, 2)
    #pygame.draw.circle(screen, "white", p1_dat5, 2)
    #pygame.draw.circle(screen, "white", p2_dat1, 2)
    #pygame.draw.circle(screen, "white", p2_dat2, 2)
    #pygame.draw.circle(screen, "white", p2_dat3, 2)
    #pygame.draw.circle(screen, "white", p2_dat4, 2)
    #pygame.draw.circle(screen, "white", p2_dat5, 2)
    
    # --- PLAYER 1 ---
    p1_surf = pygame.Surface((10 * cm, 10 * cm), pygame.SRCALPHA)
    pygame.draw.rect(p1_surf, "green", (0, 0, 10 * cm, 10 * cm))
    p1_rotated = pygame.transform.rotate(p1_surf, alfa)
    p1_rect = p1_rotated.get_rect(center=(player1_pos.x, player1_pos.y))
    screen.blit(p1_rotated, p1_rect)

    # --- PLAYER 2 ---
    p2_surf = pygame.Surface((10 * cm, 10 * cm), pygame.SRCALPHA)
    pygame.draw.rect(p2_surf, "red", (0, 0, 10 * cm, 10 * cm))
    p2_rotated = pygame.transform.rotate(p2_surf, beta)
    p2_rect = p2_rotated.get_rect(center=(player2_pos.x, player2_pos.y))
    screen.blit(p2_rotated, p2_rect)

    # Pixel-perfect collision detection using masks
    p1_mask = pygame.mask.from_surface(p1_rotated)
    p2_mask = pygame.mask.from_surface(p2_rotated)
    offset = (p2_rect.left - p1_rect.left, p2_rect.top - p1_rect.top)

    if p1_mask.overlap(p2_mask, offset):
        # Revert movement and rotation if there's a collision
        player1_pos = ex_player1_pos.copy()
        player2_pos = ex_player2_pos.copy()
        alfa = ex_alfa
        beta = ex_beta

    #Score Calculator
    dist_p1 = player1_pos.distance_to(center)
    dist_p2 = player2_pos.distance_to(center)
    if (dist_p1>72*cm):
        score[0]+=1
        player1_pos = center.copy()
        player2_pos = center.copy()
        player1_pos.y += d_f_c - 5 * cm
        player2_pos.y -= d_f_c - 5 * cm
        alfa = 0
        beta = 0
    if (dist_p2>72*cm):
        score[1]+=1
        player1_pos = center.copy()
        player2_pos = center.copy()
        player1_pos.y += d_f_c - 5 * cm
        player2_pos.y -= d_f_c - 5 * cm
        alfa = 0
        beta = 0
    current_time = pygame.time.get_ticks()
    elapsed = current_time - start_time
    if (elapsed>100):
        # Player 1 dats
        val = calculate_dat_value(p1_dat1, player2_pos, alfa_r, 1)
        if val:
            p1_dat1_value.append(val)

        val = calculate_dat_value(p1_dat2, player2_pos, alfa_r, 1)
        if val:
            p1_dat2_value.append(val)

        val = calculate_dat_value(p1_dat3, player2_pos, alfa_r, 1)
        if val:
            p1_dat3_value.append(val)

        val = calculate_dat_value(p1_dat4, player2_pos, alfa_r, 1)
        if val:
            p1_dat4_value.append(val)

        val = calculate_dat_value(p1_dat5, player2_pos, alfa_r, 1)
        if val:
            p1_dat5_value.append(val)

        # Player 2 dats
        val = calculate_dat_value(p2_dat1, player1_pos, beta_r, -1)
        if val:
            p2_dat1_value.append(abs(val))

        val = calculate_dat_value(p2_dat2, player1_pos, beta_r, -1)
        if val:
            p2_dat2_value.append(abs(val))

        val = calculate_dat_value(p2_dat3, player1_pos, beta_r, -1)
        if val:
            p2_dat3_value.append(abs(val))

        val = calculate_dat_value(p2_dat4, player1_pos, beta_r, -1)
        if val:
            p2_dat4_value.append(abs(val))

        val = calculate_dat_value(p2_dat5, player1_pos, beta_r, -1)
        if val:
            p2_dat5_value.append(abs(val))
        start_time = current_time
    pygame.display.flip()
    dt = clock.tick(60) / 1000
print(f"Score {score[0]} : {score[1]}")
print(f"P1 dat1 : {p1_dat1_value}")
print(f"P1 dat2 : {p1_dat2_value}")
print(f"P1 dat3 : {p1_dat3_value}")
print(f"P1 dat4 : {p1_dat4_value}")
print(f"P1 dat5 : {p1_dat5_value}")

print(f"P2 dat1 : {p2_dat1_value}")
print(f"P2 dat2 : {p2_dat2_value}")
print(f"P2 dat3 : {p2_dat3_value}")
print(f"P2 dat4 : {p2_dat4_value}")
print(f"P2 dat5 : {p2_dat5_value}")
