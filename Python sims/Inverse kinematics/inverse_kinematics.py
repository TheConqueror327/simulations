import pygame, math

def to_screen(p: list):
    return [p[0] + screen_width / 2, -p[1] + screen_height - 200]

def from_screen(p: list):
    return [p[0] - screen_width / 2, -(p[1] - screen_height + 200)]

def IK_2DoF(l1: int, l2: int, P: list):
    d = math.sqrt(P[0] ** 2 + P[1] ** 2)
    if l1 + l2 >= d:
        theta = math.atan2(P[1], P[0])
        alpha = math.acos((l1 ** 2 + d ** 2 - l2 ** 2) / (2 * l1 * d))
        beta = math.acos((l2 ** 2 + d ** 2 - l1 ** 2) / (2 * l2 * d))
        phi_1 = alpha + theta
        phi_2 = beta - theta
        return [phi_1, phi_2]
    else:
        print('The length of the Arm is too short!')

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

l1 = 160
l2 = 80

base_coordinates = [0, 0]
end_coordinates = [200, 60]

is_dragging = False

def draw_arm(arm_1_length: int, angles: list, P: list):
    midpoint_coordinates = [arm_1_length * math.cos(angles[0]), arm_1_length * math.sin(angles[0])]
    pygame.draw.line(screen, 'white', to_screen(base_coordinates), to_screen(midpoint_coordinates))
    pygame.draw.line(screen, 'white', to_screen(midpoint_coordinates), to_screen(P))
    pygame.draw.circle(screen, 'white', to_screen(midpoint_coordinates), 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_dragging = False
    if is_dragging:
        end_coordinates = from_screen(list(pygame.mouse.get_pos()))
    screen.fill("purple")
    pygame.draw.circle(screen, 'red', to_screen(base_coordinates), l1 + l2)
    pygame.draw.circle(screen, 'purple', to_screen(base_coordinates), abs(l1 - l2))
    if l1-l2<=((end_coordinates[0]**2) + (end_coordinates[1]**2))**0.5<=l1+l2:
        draw_arm(l1, IK_2DoF(l1, l2, end_coordinates), end_coordinates)
        pygame.draw.circle(screen, 'white', to_screen(end_coordinates), 5)

    pygame.draw.circle(screen, 'white', to_screen(base_coordinates), 5)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()