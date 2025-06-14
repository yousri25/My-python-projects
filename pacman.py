import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Clone")
clock = pygame.time.Clock()

# Load Pac-Man image
pacman = pygame.Surface((GRID_SIZE, GRID_SIZE))
pygame.draw.circle(pacman, YELLOW, (GRID_SIZE // 2, GRID_SIZE // 2), GRID_SIZE // 2)

# Game variables
pacman_pos = [1, 1]  # Starting position (x, y)
direction = [0, 0]   # Movement direction (x, y)

# Define the maze (1 = wall, 0 = empty, 2 = dot)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
    [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Function to draw the maze
def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:  # Wall
                pygame.draw.rect(screen, BLUE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            elif cell == 2:  # Dot
                pygame.draw.circle(screen, WHITE, (x * GRID_SIZE + GRID_SIZE // 2, y * GRID_SIZE + GRID_SIZE // 2), 3)

# Function to check collisions
def check_collision(new_x, new_y):
    if maze[new_y][new_x] == 1:  # Wall
        return True
    return False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                direction = [1, 0]

    # Move Pac-Man
    new_x = pacman_pos[0] + direction[0]
    new_y = pacman_pos[1] + direction[1]

    # Check for collisions
    if not check_collision(new_x, new_y):
        pacman_pos[0] = new_x
        pacman_pos[1] = new_y

        # Collect dots
        if maze[new_y][new_x] == 2:
            maze[new_y][new_x] = 0

    # Draw everything
    screen.fill(BLACK)
    draw_maze()
    screen.blit(pacman, (pacman_pos[0] * GRID_SIZE, pacman_pos[1] * GRID_SIZE))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()