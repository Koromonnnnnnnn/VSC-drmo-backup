import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 120, 20
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
BRICK_ROWS = 4
BRICK_COLS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

# Game variables
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10


class Brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250), random.randrange(
            100, 250), random.randrange(100, 250))
        self.isDead = False

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.xpos,
                         self.ypos, BRICK_WIDTH, BRICK_HEIGHT))

    def check_collision(self, ball_x, ball_y):
        if (ball_x + BALL_RADIUS > self.xpos and
            ball_x - BALL_RADIUS < self.xpos + BRICK_WIDTH and
            ball_y + BALL_RADIUS > self.ypos and
                ball_y - BALL_RADIUS < self.ypos + BRICK_HEIGHT):
            return True
        return False


bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = Brick(col * BRICK_WIDTH, row * BRICK_HEIGHT)
        bricks.append(brick)

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5
ball_dy = 5

# Lives and game over
lives = 5
game_over = False

while not game_over:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle_x += 5
    if keys[pygame.K_LEFT]:
        paddle_x -= 5

    if ball_y + BALL_RADIUS > HEIGHT:
        # Ball out of bounds, reset it
        lives -= 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = 5
        ball_dy = 5

        if lives == 0:
            game_over = True

    if ball_x + BALL_RADIUS > WIDTH:
        # Ball out of bounds, reset it
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = 5
        ball_dy = 5

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Broken Paddle interaction - Only registered half of the paddle
    # if ball_x + BALL_RADIUS > paddle_x and ball_x - BALL_RADIUS < paddle_x + PADDLE_WIDTH and ball_y + BALL_RADIUS > paddle_y:
    # if ball_x > paddle_x + PADDLE_WIDTH / 2:
    # angle = (ball_x - (paddle_x + PADDLE_WIDTH / 2)) / (PADDLE_WIDTH / 2)
    # ball_dx = 5 * angle
    # ball_dy = -ball_dy

    # Fixed Paddle
    if (ball_x + BALL_RADIUS > paddle_x and
        ball_x - BALL_RADIUS < paddle_x + PADDLE_WIDTH and
        ball_y + BALL_RADIUS > paddle_y and
            ball_y - BALL_RADIUS < paddle_y + PADDLE_HEIGHT):
        ball_dy = -ball_dy  # Bounce off the paddle

    # Brick interaction
    for brick in bricks:
        if not brick.isDead and brick.check_collision(ball_x, ball_y):
            brick.isDead = True
            ball_dy = -ball_dy

    # Render section
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y,
                     PADDLE_WIDTH, PADDLE_HEIGHT))

    for brick in bricks:
        if not brick.isDead:
            brick.draw()

    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()

pygame.quit()
