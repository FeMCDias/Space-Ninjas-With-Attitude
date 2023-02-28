import pygame
import math

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Object Trajectory")

# Set up the object
object_pos = [0, 0]
object_size = 20
object_color = (255, 0, 0)
direction = [0, 0]

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse click position
            mouse_pos = pygame.mouse.get_pos()
            # Calculate the distance between the object and the mouse click position
            distance = math.sqrt((mouse_pos[0] - object_pos[0]) ** 2 + (mouse_pos[1] - object_pos[1]) ** 2)
            # Calculate the direction vector from the object to the mouse click position
            direction = [(mouse_pos[0] - object_pos[0]) / distance, (mouse_pos[1] - object_pos[1]) / distance]
    
    # Move the object in the direction of the mouse click position
    object_pos[0] += direction[0] * 5
    object_pos[1] += direction[1] * 5
    
    # Draw the object and the screen
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, object_color, object_pos, object_size)
    pygame.display.flip()

pygame.quit()