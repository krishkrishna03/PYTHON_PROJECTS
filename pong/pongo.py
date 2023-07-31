import pygame
import random

pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Define Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dy):
        self.rect.y += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

# Define Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.vx = 5 * random.choice([1, -1])
        self.vy = 5 * random.choice([1, -1])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.vy *= -1

# Create paddles and ball
player_paddle = Paddle(10, screen_height // 2 - 25)
computer_paddle = Paddle(screen_width - 20, screen_height // 2 - 25)
ball = Ball()

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player_paddle, computer_paddle, ball)

# Game loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move(-5)
    if keys[pygame.K_DOWN]:
        player_paddle.move(5)

    # AI for computer paddle
    if ball.vx > 0:
        if computer_paddle.rect.centery < ball.rect.centery:
            computer_paddle.move(5)
        elif computer_paddle.rect.centery > ball.rect.centery:
            computer_paddle.move(-5)

    # Update ball movement
    ball.update()

    # Ball collision with paddles
    if pygame.sprite.collide_rect(ball, player_paddle) or pygame.sprite.collide_rect(ball, computer_paddle):
        ball.vx *= -1

    # Ball out of bounds
    if ball.rect.left < 0 or ball.rect.right > screen_width:
        ball = Ball()
        all_sprites.add(ball)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
