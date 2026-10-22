import math
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Tom")
clock = pygame.time.Clock()

# Colors
BG = (190, 225, 245)
GRAY = (130, 135, 145)
DARK = (50, 55, 65)
WHITE = (250, 250, 250)
PINK = (245, 155, 170)
BLUE = (80, 155, 235)
BLACK = (25, 25, 30)

tom_x, tom_y = WIDTH // 2, HEIGHT // 2 + 50
target_x, target_y = tom_x, tom_y
mood = "curious"
message = "Move your mouse or click Tom!"
blink_timer = 0
blink = False
start_time = pygame.time.get_ticks()


def draw_tom(x, y, time_ms):
    """Draw a cartoon gray cat with eyes that follow the pointer."""
    bob = math.sin(time_ms / 300) * 5
    x, y = int(x), int(y + bob)

    # Ears
    pygame.draw.polygon(screen, GRAY, [(x - 65, y - 75), (x - 55, y - 145), (x - 15, y - 95)])
    pygame.draw.polygon(screen, GRAY, [(x + 15, y - 95), (x + 55, y - 145), (x + 65, y - 75)])
    pygame.draw.polygon(screen, PINK, [(x - 52, y - 92), (x - 48, y - 125), (x - 28, y - 96)])
    pygame.draw.polygon(screen, PINK, [(x + 28, y - 96), (x + 48, y - 125), (x + 52, y - 92)])

    # Head and muzzle
    pygame.draw.ellipse(screen, GRAY, (x - 75, y - 105, 150, 145))
    pygame.draw.ellipse(screen, WHITE, (x - 42, y - 10, 40, 28))
    pygame.draw.ellipse(screen, WHITE, (x + 2, y - 10, 40, 28))

    # Eyes track the mouse
    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - x, my - (y - 45)
    length = max(1, math.hypot(dx, dy))
    pupil_x = dx / length * 6
    pupil_y = dy / length * 4

    if blink:
        pygame.draw.line(screen, DARK, (x - 42, y - 48), (x - 15, y - 48), 5)
        pygame.draw.line(screen, DARK, (x + 15, y - 48), (x + 42, y - 48), 5)
    else:
        pygame.draw.ellipse(screen, WHITE, (x - 45, y - 65, 35, 48))
        pygame.draw.ellipse(screen, WHITE, (x + 10, y - 65, 35, 48))
        pygame.draw.circle(screen, BLUE, (int(x - 28 + pupil_x), int(y - 42 + pupil_y)), 10)
        pygame.draw.circle(screen, BLUE, (int(x + 28 + pupil_x), int(y - 42 + pupil_y)), 10)
        pygame.draw.circle(screen, BLACK, (int(x - 28 + pupil_x), int(y - 42 + pupil_y)), 5)
        pygame.draw.circle(screen, BLACK, (int(x + 28 + pupil_x), int(y - 42 + pupil_y)), 5)

    # Nose and mouth
    pygame.draw.polygon(screen, PINK, [(x - 9, y - 5), (x + 9, y - 5), (x, y + 5)])
    pygame.draw.arc(screen, DARK, (x - 13, y - 2, 13, 15), math.pi, 2 * math.pi, 2)
    pygame.draw.arc(screen, DARK, (x, y - 2, 13, 15), math.pi, 2 * math.pi, 2)

    # Whiskers
    for side in (-1, 1):
        for offset in (0, 10, 20):
            pygame.draw.line(
                screen, WHITE,
                (x + side * 35, y + offset - 3),
                (x + side * 85, y + offset - 12 + (offset // 10) * 8),
                2,
            )

    # Body and paws
    pygame.draw.ellipse(screen, GRAY, (x - 80, y + 25, 160, 130))
    pygame.draw.ellipse(screen, GRAY, (x - 60, y + 125, 55, 28))
    pygame.draw.ellipse(screen, GRAY, (x + 5, y + 125, 55, 28))


def main():
    global target_x, target_y, mood, message, blink, blink_timer

    running = True
    font = pygame.font.SysFont(None, 30)

    while running:
        dt = clock.tick(60)
        now = pygame.time.get_ticks()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                distance = math.hypot(mouse_x - tom_x, mouse_y - (tom_y - 35))
                if distance < 110:
                    mood = "happy"
                    message = "You petted Tom!"
                    target_x = WIDTH // 2 + (mouse_x - WIDTH // 2) * 0.25
                    target_y = HEIGHT // 2 + 50
                else:
                    message = "Click Tom to pet him!"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mood = "excited"
                    message = "Tom says: Meow!"
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Tom gently follows the pointer, while staying on screen
        target_x = max(110, min(WIDTH - 110, mouse_x))
        target_y = max(220, min(HEIGHT - 170, mouse_y + 80))
        tom_x += (target_x - tom_x) * 0.035
        tom_y += (target_y - tom_y) * 0.035

        # Occasional blink
        blink_timer += dt
        blink = (blink_timer % 3200) < 140

        screen.fill(BG)

        # Floor
        pygame.draw.rect(screen, (145, 195, 215), (0, HEIGHT - 65, WIDTH, 65))
        pygame.draw.ellipse(screen, (120, 165, 185), (tom_x - 90, tom_y + 135, 180, 25))

        draw_tom(tom_x, tom_y, now)

        label = font.render(message, True, DARK)
        screen.blit(label, (20, 20))

        hint = pygame.font.SysFont(None, 22).render(
            "Move mouse to guide Tom • Click to pet • Space for a meow • Esc to quit",
            True, DARK
        )
        screen.blit(hint, (20, HEIGHT - 35))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()