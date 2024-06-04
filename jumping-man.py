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
            pause_button.draw(screen)

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
    varDict = {"Grid x Height": 0, "Grid y Height": 0, "How many ticks to play?": 0}

    # Button class
    class Button:
        def __init__(self, text, pos, size, color, text_color):
            self.text = text
            self.pos = pos
            self.size = size
            self.color = color
            self.text_color = text_color
            self.rect = pygame.Rect(pos, size)
            self.font = pygame.font.Font(None, 36)
            self.text_surf = self.font.render(text, True, text_color)
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            screen.blit(self.text_surf, self.text_rect)

        def is_clicked(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
            return False

    # Input box class
    class InputBox:

        def __init__(self, x, y, w, h, label='Label', text=''):
            self.touched = False
            self.rect = pygame.Rect(x, y, w, h)
            self.color = (200, 200, 200)
            self.text = text
            self.txt_surface = font.render(text, True, WHITE)
            self.active = False

        def handle_event(self, event: pygame.event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input box rect.
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                    if not self.touched:
                        self.text = ''
                        self.touched = True
                    # self.txt_surface = font.render(self.text, True, WHITE)
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = BLACK if self.active else (200, 200, 200)
                
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        # varDict[self.text]
                        self.text = ''  # Clear the input box
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
            # Re-render the text.
            self.txt_surface = font.render(self.text, True, WHITE)

        def update(self):
            # Resize the box if the text is too long.
            width = max(200, self.txt_surface.get_width()+10)
            self.rect.w = width

        def draw(self, screen):
            # Blit the text.
            screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
            # Blit the rect.
            pygame.draw.rect(screen, self.color, self.rect, 2)

    # Set up display
    width, height = 1080, 700
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
    pause_button = Button("Pause", (width-100, height-40), (100, 40), GREEN, BLACK)

    # Create an input box
    input_box_x = InputBox(height/2, 100, 140, 32, text="Grid x Height")
    input_box_y = InputBox(height/2, 200, 140, 32, text="Grid y Height")
    input_box_age_limit = InputBox(height/2, 300, 140, 32, text="How many ticks to play?")

    screen.fill(BLACK)
    screen1 = True
    while screen1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen1 = False
                pygame.quit()
                sys.exit()
            input_box_x.handle_event(event)
            input_box_y.handle_event(event)
            input_box_age_limit.handle_event(event)
        input_box_x.update()
        input_box_y.update()
        input_box_age_limit.update()
        input_box_x.draw(screen)
        input_box_y.draw(screen)
        input_box_age_limit.draw(screen)
        pygame.display.flip()

    pygame.time.wait(1000)

    paused = False
    # Main loop
    running = True
    clock = pygame.time.Clock()
    
    age = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pause_button.is_clicked(event):
                paused = not paused
                pause_button.text = "Resume" if paused else "Pause"
                pause_button.text_surf = pause_button.font.render(pause_button.text, True, pause_button.text_color)
                pause_button.text_rect = pause_button.text_surf.get_rect(center=pause_button.rect.center)
        

        # Clear screen
        screen.fill(BLACK)
        pause_button.draw(screen)
        
        # Blit text surfaces to the screen
        # Render text
        xHeight = 11
        yHeight = 11
        thisGrid = [[0 for i in range(2 * yHeight + 1)] for j in range(2 * xHeight + 1)]
        pause_button.draw(screen)
        if not paused:
            if age == 11:
                age = 1
            else:
                age += 1
            
            
            printGrid(gridPlotter(thisGrid, age))
            pause_button.draw(screen)
            pygame.time.wait(1000)
            
            # Update display
            pygame.display.flip()
            screen.fill(BLACK)
            # screen.blit(font.render("--"*100, True, RED))
            # screen.blit(font.render("--" * 100, True, RED))
            clock.tick(30)

    # Quit Pygame
    pygame.quit()
    sys.exit()
