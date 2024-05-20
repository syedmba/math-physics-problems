import pygame
import sys


def printGrid(grid):
    font_size = 20
   
    font = pygame.font.Font(None, font_size)

    for row_index, row in enumerate(grid):
        for col_index, element in enumerate(row):
            if element != 0:
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            text_surface = font.render(str(element), True, color)
            # Calculate position
            position = (col_index * font_size * 2, row_index * font_size * 2)
            screen.blit(text_surface, position)

    # for i in range(len(grid)):
    #     for j in range(len(grid)):
    #         if grid[i][j] != 0:
    #             color = (0, 255, 0)
    #         else:
    #             color = (255, 255, 255)
    #         font.render(str(grid[i][j]) + " "*(6 - len(str(grid[i][j]))), True, color)


def gridPlotter(grid, time): # assuming grid is (2n + 1) x (2n + 1)
    if time <= 0:
        zeroGrid = [[0 for i in range(len(grid))] for j in range(len(grid))]
        zeroGrid[int((len(grid) - 1)/2)][int((len(grid) - 1)/2)] = 1
        # print(f"grid is now {grid}.")
        return zeroGrid
    else:
        prevGrid = gridPlotter(grid, time - 1)
        newGrid = [[0 for i in range(len(grid))] for j in range(len(grid))]
        # print(f"prevGrid is {prevGrid}.")
        for row in range(1, len(grid) - 1):  # don't want to deal with boundary cases YET
            for col in range(1, len(grid) - 1):
                newGrid[row][col] = prevGrid[row][col - 1] + prevGrid[row - 1][col] + prevGrid[row][col + 1] + prevGrid[row + 1][col]
        # print(f"grid is now {newGrid}.")
        return newGrid
    

if __name__ == '__main__':

    pygame.init()
    pygame.font.init()

    # Set up display
    width, height = 1080, 1680
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jumping Man Problem")

    # Define colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    # Load a font
    font_size = 20
    font = pygame.font.Font(None, font_size)


    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BLACK)
        
        # Blit text surfaces to the screen
        # Render text
        xHeight = 11
        yHeight = 11
        thisGrid = [[0 for i in range(2 * yHeight + 1)] for j in range(2 * xHeight + 1)]
        for age in range(1, 11):
            printGrid(gridPlotter(thisGrid, age))
            pygame.time.wait(1000)
            
            # Update display
            pygame.display.flip()
            screen.fill(BLACK)
            # screen.blit(font.render("--"*100, True, RED))
            # screen.blit(font.render("--" * 100, True, RED))
        

    # Quit Pygame
    pygame.quit()
    sys.exit()
