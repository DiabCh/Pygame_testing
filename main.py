import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
TILE_SIZE = 16
WIDTH = 25
HEIGHT = 25


EMPTY = 0
WALL = 1
SPECIAL = 2

screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))


class GameMap():
    def __init__(self) -> None:
        self.map = self.__create_map()


    def __create_map(self):
        map_data = []

        for y in range(HEIGHT):
            row = []
            for x in range(WIDTH):
                if x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:
                    row.append(WALL)  # create a border of walls
                elif random.random() < 0.2:
                    row.append(WALL)  # add random walls
                elif random.random() < 0.05:
                    row.append(SPECIAL)  # add random special areas
                else:
                    row.append(EMPTY)  # create empty spaces
            map_data.append(row)

        return map_data


# Define tile types

# Create the map
map_data = GameMap()
# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the map
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if map_data.map[y][x] == WALL:
                color = (128, 128, 128)  # gray walls
            elif map_data.map[y][x] == SPECIAL:
                color = (255, 0, 0)  # red special areas
            else:
                color = (255, 255, 255)  # white empty spaces
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Flip the display
    pygame.display.flip()

# Clean up Pygame
pygame.quit()