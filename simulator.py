import asyncio
import platform
import pygame
import math
from math import sin, cos

# Constants
cm = 4  # 4 pixels = 1 cm
mass_p1 = 10
mass_p2 = 10
f_qarsh_1_paym = 10
f_qarsh_2_paym = 10
f_glorman_1_paym = 20
f_glorman_2_paym = 20

# Initialize forces
f_qarsh_1 = 0
f_glorman_1 = 0
f_hrum = 0
alfa_hrum = 0
f_qarsh_2 = 0
f_glorman_2 = 0

def is_point_in_rotated_square(point, center, angle, side_length=10 * cm):
    rel_x = point.x - center.x
    rel_y = point.y - center.y
    cos_a = math.cos(-angle)
    sin_a = math.sin(-angle)
    unrotated_x = rel_x * cos_a - rel_y * sin_a
    unrotated_y = rel_x * sin_a + rel_y * cos_a
    half_side = side_length / 2
    return (-half_side <= unrotated_x <= half_side) and (-half_side <= unrotated_y <= half_side)

def calculate_dat_value(dat_pos, center, angle, step):
    max_iter = 1000
    step *= cm
    point_outside = dat_pos.copy()
    length = 0
    for _ in range(max_iter):
        point_outside.x -= step * math.sin(angle)
        point_outside.y -= step * math.cos(angle)
        length += abs(step)
        if is_point_in_rotated_square(point_outside, center, angle):
            low = (length - abs(step)) / cm
            high = length / cm
            for _ in range(100):
                mid = (low + high) / 2
                test_point = dat_pos.copy()
                test_point.x -= (mid * cm) * math.sin(angle)
                test_point.y -= (mid * cm) * math.cos(angle)
                if is_point_in_rotated_square(test_point, center, angle):
                    high = mid
                else:
                    low = mid
            return (low + high) / 2
    return None

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
FPS = 60

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player1_pos = center.copy()
player2_pos = center.copy()
d_f_c = ((70 * cm) ** 2 - (50 * cm)) ** 0.5
player1_pos.y += d_f_c - 5 * cm
player2_pos.y -= d_f_c - 5 * cm
score = [0, 0]
alfa = 0
beta = 0
v_1_x = 0
v_2_x = 0
v_1_y = 0
v_2_y = 0
start_time = pygame.time.get_ticks()

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
f_lriv_1_ys = []

async def main():
    global alfa, beta, f_qarsh_1, f_glorman_1, f_qarsh_2, f_glorman_2
    global v_1_x, v_1_y, v_2_x, v_2_y, player1_pos, player2_pos, start_time
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Time delta in seconds
        ex_player1_pos = player1_pos.copy()
        ex_player2_pos = player2_pos.copy()
        ex_alfa = alfa
        ex_beta = beta
        alfa_r = math.radians(alfa)
        beta_r = math.radians(beta)

        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            f_qarsh_2 = -f_qarsh_2_paym
            f_glorman_2 = -f_glorman_2_paym
        elif keys[pygame.K_w]:
            f_qarsh_2 = f_qarsh_2_paym
            f_glorman_2 = f_glorman_2_paym
        else:
            f_qarsh_2 = 0
            f_glorman_2 = 0
        if keys[pygame.K_a]:
            beta += 1
        if keys[pygame.K_d]:
            beta -= 1
        if keys[pygame.K_k]:
            f_qarsh_1 = f_qarsh_1_paym
            f_glorman_1 = f_glorman_1_paym
        elif keys[pygame.K_i]:
            f_qarsh_1 = -f_qarsh_1_paym
            f_glorman_1 = -f_glorman_1_paym
        else:
            f_qarsh_1 = 0
            f_glorman_1 = 0
        if keys[pygame.K_j]:
            alfa += 1
        if keys[pygame.K_l]:
            alfa -= 1

        # Calculate forces
        f_lriv_1_y = (f_glorman_1 + f_qarsh_1) * cos(alfa_r)
        f_lriv_1_x = (f_glorman_1 + f_qarsh_1) * sin(alfa_r)
        f_lriv_2_y = (f_glorman_2 + f_qarsh_2) * cos(beta_r)
        f_lriv_2_x = (f_glorman_2 + f_qarsh_2) * sin(beta_r)

        # Calculate accelerations (reduced scaling factor for balanced speed)
        a_1_x = f_lriv_1_x / mass_p1 * 10  # Adjusted from *100 to *10
        a_1_y = f_lriv_1_y / mass_p1 * 10
        a_2_x = f_lriv_2_x / mass_p2 * 10
        a_2_y = f_lriv_2_y / mass_p2 * 10

        # Update velocities
        v_1_x += a_1_x * dt
        v_1_y += a_1_y * dt
        v_2_x += a_2_x * dt
        v_2_y += a_2_y * dt

        # Update positions
        player1_pos.x += v_1_x * dt
        player1_pos.y += v_1_y * dt
        player2_pos.x += v_2_x * dt
        player2_pos.y += v_2_y * dt

        # Datchikner (sensors)
        p1_dat2 = player1_pos.copy()
        p2_dat2 = player2_pos.copy()
        p2_dat2.x += 5 * cm * math.sin(beta_r)
        p2_dat2.y += 5 * cm * math.cos(beta_r)
        p1_dat2.x -= 5 * cm * math.sin(alfa_r)
        p1_dat2.y -= 5 * cm * math.cos(alfa_r)
        p1_dat1 = p1_dat2.copy()
        p1_dat3 = p1_dat2.copy()
        p2_dat1 = p2_dat2.copy()
        p2_dat3 = p2_dat2.copy()
        p1_dat1.x -= 3.5 * cm * cos(alfa_r)
        p1_dat1.y += 3.5 * cm * sin(alfa_r)
        p1_dat3.x += 3.5 * cm * cos(alfa_r)
        p1_dat3.y -= 3.5 * cm * sin(alfa_r)
        p2_dat1.x += 3.5 * cm * cos(beta_r)
        p2_dat1.y -= 3.5 * cm * sin(beta_r)
        p2_dat3.x -= 3.5 * cm * cos(beta_r)
        p2_dat3.y += 3.5 * cm * sin(beta_r)
        p1_dat4 = player1_pos.copy()
        p1_dat4.x += 5 * cm * cos(alfa_r) - 3 * sin(alfa_r) * cm
        p1_dat4.y -= 5 * cm * sin(alfa_r) + 3 * cos(alfa_r) * cm
        p1_dat5 = p1_dat4.copy()
        p1_dat5.x -= 10 * cm * cos(alfa_r)
        p1_dat5.y += 10 * cm * sin(alfa_r)
        p2_dat4 = player2_pos.copy()
        p2_dat4.x -= 5 * cm * cos(beta_r) - 3 * sin(beta_r) * cm
        p2_dat4.y += 5 * cm * sin(beta_r) + 3 * cos(beta_r) * cm
        p2_dat5 = p2_dat4.copy()
        p2_dat5.x += 10 * cm * cos(beta_r)
        p2_dat5.y -= 10 * cm * sin(beta_r)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing
        screen.fill("white")
        pygame.draw.circle(screen, "yellow", center, 100 * cm)
        pygame.draw.circle(screen, "white", center, 72 * cm)
        pygame.draw.circle(screen, "black", center, 70 * cm)
        pygame.draw.circle(screen, "white", p1_dat1, 2)
        pygame.draw.circle(screen, "white", p1_dat2, 2)
        pygame.draw.circle(screen, "white", p1_dat3, 2)
        pygame.draw.circle(screen, "white", p1_dat4, 2)
        pygame.draw.circle(screen, "white", p1_dat5, 2)
        pygame.draw.circle(screen, "white", p2_dat1, 2)
        pygame.draw.circle(screen, "white", p2_dat2, 2)
        pygame.draw.circle(screen, "white", p2_dat3, 2)
        pygame.draw.circle(screen, "white", p2_dat4, 2)
        pygame.draw.circle(screen, "white", p2_dat5, 2)
        p1_surf = pygame.Surface((10 * cm, 10 * cm), pygame.SRCALPHA)
        pygame.draw.rect(p1_surf, "green", (0, 0, 10 * cm, 10 * cm))
        p1_rotated = pygame.transform.rotate(p1_surf, alfa)
        p1_rect = p1_rotated.get_rect(center=(player1_pos.x, player1_pos.y))
        screen.blit(p1_rotated, p1_rect)
        p2_surf = pygame.Surface((10 * cm, 10 * cm), pygame.SRCALPHA)
        pygame.draw.rect(p2_surf, "red", (0, 0, 10 * cm, 10 * cm))
        p2_rotated = pygame.transform.rotate(p2_surf, beta)
        p2_rect = p2_rotated.get_rect(center=(player2_pos.x, player2_pos.y))
        screen.blit(p2_rotated, p2_rect)

        # Collision detection with bounce
        p1_mask = pygame.mask.from_surface(p1_rotated)
        p2_mask = pygame.mask.from_surface(p2_rotated)
        offset = (p2_rect.left - p1_rect.left, p2_rect.top - p1_rect.top)
        if p1_mask.overlap(p2_mask, offset):
            damping = 0.8
            v_1_x *= -damping
            v_1_y *= -damping
            v_2_x *= -damping
            v_2_y *= -damping

        # Scoring
        dist_p1 = player1_pos.distance_to(center)
        dist_p2 = player2_pos.distance_to(center)
        if dist_p1 > 72 * cm:
            score[0] += 1
            player1_pos = center.copy()
            player2_pos = center.copy()
            player1_pos.y += d_f_c - 5 * cm
            player2_pos.y -= d_f_c - 5 * cm
            alfa = 0
            beta = 0
            v_1_x = v_1_y = v_2_x = v_2_y = 0  # Reset velocities
        if dist_p2 > 72 * cm:
            score[1] += 1
            player1_pos = center.copy()
            player2_pos = center.copy()
            player1_pos.y += d_f_c - 5 * cm
            player2_pos.y -= d_f_c - 5 * cm
            alfa = 0
            beta = 0
            v_1_x = v_1_y = v_2_x = v_2_y = 0  # Reset velocities

        # Sensor data collection
        current_time = pygame.time.get_ticks()
        elapsed = current_time - start_time
        if elapsed > 100:
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
        f_lriv_1_ys.append(f_lriv_1_y)
        pygame.display.flip()
        await asyncio.sleep(1.0 / FPS)

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
    print(f_lriv_1_ys)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
