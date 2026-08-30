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

# variables to keep track of points
player1_score = player2_score = 0
checked_indexes = []

# Variable to control loop
running = True 

# change captipn
pygame.display.set_caption("Seega")

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
            centre_x = (((j+1) +j) / 2) * 100
            centre_y = (((i+1) +i) / 2) * 100
            if markers[i][j] == 1:
                pygame.draw.circle(screen, black, (centre_x, centre_y),30)
            elif markers[i][j] == 2:
                 pygame.draw.circle(screen, white, (centre_x, centre_y),30)
  
# check for points
def track_points():

    global player2_score, player1_score

    # Horizontal check
    for i in range(len(markers)):
        groups = [(markers[i][j], markers[i][j+1], markers[i][j+2]) for j in range(len(markers[i]) -2)]
        
        if (1,2,1) in groups:
            player1_score += 1
        elif (2,1,2) in groups:
            player2_score += 1
    
        
    
    # Vertical check
    for j in range(COLS):
        groups = [(markers[i][j], markers[i+1][j], markers[i+2][j]) for i in range(ROWS -2)]

        if (1,2,1) in groups:
            player1_score += 1
        elif (2,1,2) in groups:
            player2_score += 1

while running:

    # screen.fill(board_colour)
    board()
    draw_markers()
    # track_points()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos() # get x,y coordinate of the mouse position
            x,y = pos

            if markers[y//square_wid][x // square_height] == 0:
                markers[y//square_wid][x // square_height] = player
                player = (player % 2) + 1
            track_points() # Only adjust the scores after the player has made a move to prevent the score from being update for every loop. 
                
    pygame.display.update()

print(markers)

print(player1_score)
print(player2_score)