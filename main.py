import pygame


#initialise the game
pygame.init()


#variables to to create the screen
WIDTH, HEIGHT = 800,800
ROWS,COLS = 8,8
screen = pygame.display.set_mode((WIDTH,HEIGHT))


# variables used to create the board
board_colour = (137,81,41) #colour brown
board_outline = (0,0,0)    #colour blck
square_wid = WIDTH//COLS
square_height = HEIGHT//  ROWS

# variables for markers
player = 1
markers = [[0] * COLS for _ in range(ROWS)]
clicked = False
pos = tuple()
black = (0,0,0)
white = (255, 255, 255)


# Variable to control loop
running = True 

# all functions are placed under this comment

# create board function
def board():
    screen.fill(board_colour)
    for x in range(0,WIDTH,square_wid):
            for y in range(0, HEIGHT, square_height):
                pygame.draw.rect(screen, board_outline,pygame.Rect(x,y,square_wid,square_height),2)

# create markers
def draw_markers():
    for i in range(ROWS):
        for j in range(COLS):
            centre_x = (((i+1) +i) / 2) * 100
            centre_y = (((j+1) +j) / 2) * 100
            if markers[i][j] == 1:
                pygame.draw.circle(screen, black, (centre_x, centre_y),30)
            elif markers[i][j] == 2:
                 pygame.draw.circle(screen, white, (centre_x, centre_y),30)
            

while running:

    # screen.fill(board_colour)
    board()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
             clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
             clicked = False
             pos = pygame.mouse.get_pos() #get x,y coordinate of the mouse position
             x,y = pos

             if markers[x//square_wid][y // square_height] == 0:
                  markers[x//square_wid][y // square_height] = player
                  player = (player % 2) + 1
                  
                
    pygame.display.update()

print(markers)