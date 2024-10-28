#Imports
import random
import time
import turtle as trtl

#------------------------------------------------------------------


#variables
wn = trtl.Screen()

#block colors
yellow = r"""C:\Users\NTTDATA\My Drive\AP CSP Files\tetris_files\yellowBlock.gif"""
orange = r"""C:\Users\NTTDATA\My Drive\AP CSP Files\tetris_files\orangeBlock.gif"""
red = r"""C:\Users\NTTDATA\My Drive\AP CSP Files\tetris_files\redBlock.gif"""
blue = r"""C:\Users\NTTDATA\My Drive\AP CSP Files\tetris_files\blueBlock.gif"""
border = r"""C:\Users\NTTDATA\My Drive\AP CSP Files\tetris_files\borderBlock.gif"""
light_blue = r"""C:\Users\NTTDATA\My Drive\AP CSP Files\tetris_files\lightBlueBlock.gif"""

wn.addshape(yellow)
wn.addshape(orange)
wn.addshape(red)
wn.addshape(blue)
wn.addshape(light_blue)
wn.addshape(border)


#Global variables setup
current_shape = ""
y = 0
x = 0
start = 0
score = 0

#Other setups
wn.tracer(0)

wn.bgcolor("black")

scribe = trtl.Turtle()
scribe.pu()
scribe.color("white")
scribe.goto(0, -385)

wn.tracer(1)

wn.setup(460, 780)

#starting game map
map_list = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    ]
#-----------------------------------------------------------------

#Game status and UI function
def print_map_status():
    global current_shape
    global score
    for row in map_list: #prints the current map in the terminal for debugging
        print(row)

    #prints a few of the global variables
    print(len(map_list), "rows")
    print( f"Current Shape: {current_shape}", f"Score: {score}", sep= "\n")

    print("\n\n")

def print_game(): #used to print the game using turtle so that the user can see on the screen/canvas

    wn.clear()
    wn.bgcolor("black") #resetting screen
    wn.tracer(0)
    
    update_score()#updates the scribe turtle with the current score
    # wn.bgcolor("black")

    row_num = 0
    x = -20 #used to position the entire map perfectly inside the window

    #top border
    for i in range(10):
        block = trtl.Turtle()
        block.pu()
        block.shape(border)
        block.goto(-149+ x + 37 * i, 363)
    
    # left border
    for y in range(len(map_list) + 1):
        block = trtl.Turtle()
        block.pu()
        block.shape(border)
        block.goto(-186+ x, 363 - 37*y)
    #right border
    for y in range(len(map_list)+1):
        block = trtl.Turtle()
        block.pu()
        block.shape(border)
        block.goto(223+ x, 363 - 37*y)

    #this is where the algorithm reads the map_list, determines the corresponding turtle, and adds it to turtle screen where the user can see
    for row in map_list:
        col_num = 0
       
        for space in row:

            block = trtl.Turtle()
            block.pu()
            
            if space == 0: #empty space
                block.ht()
           
            elif space == 1: #horizontal t block
                block.shape(yellow)
           
            elif space == 2: # horizontal l block
                block.shape(orange)
           
            elif space == 3: #vertical t block
                block.shape(blue)
           
            elif space == 4: #square block
                block.shape(red)
           
            elif space == 5: #vertical line block
                block.shape(light_blue)
           
            else: #border block on the bottom
                block.shape(border)

            block.goto(-149+ x + 37*col_num, 326-37*row_num) #based on the col and row (x,y) the block mirrors on the turtle screen

            col_num += 1
        
        row_num += 1

    wn.tracer(1)

#------------------------------------------------------------------

#Shape Generation functions
def generate_shape(): #used to determine next shape and reset x and y translation variables
    global current_shape
    global x
    global y
    global start

    x = 0
    y = 0

    add_point()

    current_shape = random.choice(["H-L", "H-T", "V-T", "Square", "Vertical"]) #choose a random next shape

    start = random.randint(2,7) #choose a random start location when starting at the top
    
    if current_shape == "H-T": #horizontal T
        create_clear_HT(start, x, y, 1)
        
    elif current_shape == "H-L": #horizontal L
        create_clear_HL(start, x, y, 2)

    elif current_shape == "V-T": #vertical T
        create_clear_VT(start, x, y, 3)

    elif current_shape == "Square": #square
        create_clear_square(start, x, y, 4)

    elif current_shape == "Vertical": #vertical line
        create_clear_vertical(start, x, y, 5)

    else: #in case there is an error, easier to debug when adding new shapes
        print("shape error")

#Shape creating and clearing functions, used to take the numbers off the map_list and add them back in a new position
def create_clear_HL(starting_col, x, y, val): #creates or clears horizontal L block
    map_list[0+y][starting_col+x] = val
    map_list[1+y][starting_col+x] = val
    map_list[1+y][starting_col+1+x] = val
    map_list[1+y][starting_col+2+x] = val

def create_clear_HT(starting_pos, x, y, val): #creates or clears horizontal T block
    map_list[0+y][starting_pos+1 + x] = val
    map_list[1+y][starting_pos+0+ x] = val
    map_list[1+y][starting_pos+1+ x] = val
    map_list[1+y][starting_pos+2+ x] = val

def create_clear_VT(starting_pos, x, y, val): #creates or clears Vertical T block
    map_list[0+y][starting_pos+ 0 + x] = val
    map_list[1+y][starting_pos+ 0 + x] = val
    map_list[1+y][starting_pos+ 1 + x] = val
    map_list[2+y][starting_pos+ 0 + x] = val

def create_clear_square(starting_pos, x, y, val): #creates or clears Square block
    map_list[0+y][starting_pos+ 0 + x] = val
    map_list[0+y][starting_pos+ 1 + x] = val
    map_list[1+y][starting_pos+ 0 + x] = val
    map_list[1+y][starting_pos+ 1 + x] = val    

def create_clear_vertical(starting_pos, x, y, val): #creates or clears vertical line block
    map_list[0+y][starting_pos+ 0 + x] = val
    map_list[1+y][starting_pos+ 0 + x] = val
    map_list[2+y][starting_pos+ 0 + x] = val
    map_list[3+y][starting_pos+ 0 + x] = val  

#------------------------------------------------------------------
#Vertical block controls
def down_vertical():
    global y
    global x
    global start
    global current_shape
    
    if map_list[3+y + 1][start + 0 + x] == 0:

        create_clear_vertical(start, x, y, 0)
        y += 1
        create_clear_vertical(start, x, y, 5)
        
    else: #every DOWN movement function will have this at the end to enure that the program checks if the game ends, then generates a new shape if the game does not end
        print("generating shape...")
        end_game()
        generate_shape()

def left_vertical():
    global y
    global x
    global start
    
    if (start + 0 + x)- 1 >= 0:

        available = 0

        for i in range(0,4):
            
            if map_list[y + i][(start + 0 + x) - 1] == 0:
                available += 1

        if available == 4:
            
            create_clear_vertical(start, x, y, 0)
            x -= 1
            create_clear_vertical(start, x, y, 5)   

def right_vertical():
    global y
    global x
    global start
    
    if (start + 0 + x)+ 1 <= 9:

        available = 0

        for i in range(0,4):
            
            if map_list[y + i][(start + 0 + x) + 1] == 0:
                available += 1

        if available == 4:
            
            create_clear_vertical(start, x, y, 0)
            x += 1
            create_clear_vertical(start, x, y, 5)   

#------------------------------------------------------------------
#Square Controls
def down_sqaure():
    global y
    global x
    global start
    global current_shape
    
    if map_list[1+y + 1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:

        create_clear_square(start, x, y, 0)
        y += 1
        create_clear_square(start, x, y, 4)
        
    
    else:
        available = 0
        
        if map_list[1+y + 1][start+ 0 + x] == 0:
            available += 1

        if map_list[1+y + 1][start+ 1 + x] == 0:
            available += 1

        if available == 2:
            
            create_clear_square(start, x, y, 0)
            y += 1
            create_clear_square(start, x, y, 4)
            
        else:
            print("generating shape...")
            end_game()
            generate_shape()

def left_sqaure():
    global y
    global x
    global start
    
    if (start + 0 + x)- 1 >= 0:

        available = 0
        for i in range(0,2):
            if map_list[1+y + i][start + 0 + x - 1] == 0:
                available += 1

        if available == 2:

            create_clear_square(start, x, y, 0)
            x -= 1
            create_clear_square(start, x, y, 4)

def right_square():
    global y
    global x
    global start
    
    if (start + 1 + x)+ 1 <= 9:

        available = 0
        for i in range(0,2):
            if map_list[1+y + i][start + 1 + x + 1] == 0:
                available += 1

        if available == 2:

            create_clear_square(start, x, y, 0)
            x += 1
            create_clear_square(start, x, y, 4)

#------------------------------------------------------------------

#Vertical (sideways) T block controls
def down_VT():
    global y
    global x
    global start
    global current_shape
    
    if map_list[(2+y) + 1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:

        create_clear_VT(start, x, y, 0)
        y += 1
        create_clear_VT(start, x, y, 3)
        
    
    else:
        available = 0
        
        if map_list[(2+y) + 1][start+ 0 + x] == 0:
            available += 1

        if map_list[1+y + 1][start+ 1 + x] == 0:
            available += 1

        if available == 2:
            
            create_clear_VT(start, x, y, 0)
            y += 1
            create_clear_VT(start, x, y, 3)
            
        else:
            print("generating shape...")
            end_game()
            generate_shape()

def left_VT():
    global y
    global x
    global start
    
    if (start + 0 + x)- 1 >= 0:

        available = 0
        for i in range(0,3):
            if map_list[y + i][start + 0 + x - 1] == 0:
                available += 1

        if available == 3:

            create_clear_VT(start, x, y, 0)
            x -= 1
            create_clear_VT(start, x, y, 3)

def right_VT():
    global y
    global x
    global start
    
    if (start + 1 + x)+ 1 <= 9:

        create_clear_VT(start, x, y, 0)

        available = 0

        for i in range(0,3,2):
            print("value", i)
            
            if map_list[y + i][start + 0 + x + 1] == 0:
                available += 1
                print("top/bottom accepted")
        
        if map_list[(1 + y)][start + 1 + x + 1] == 0:
            available += 1
            print("middle accepted")

        print(available)

        if available == 3:

            x += 1
            create_clear_VT(start, x, y, 3)
        else:
            create_clear_VT(start, x, y, 3)

#------------------------------------------------------------------

# Horizontal L and Horizontal T block controls
def down_HL_HT():
    global y
    global x
    global start
    global current_shape
    
    if map_list[(1+y) + 1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        
        if current_shape == "H-L":

            create_clear_HL(start, x, y, 0)
            y += 1
            create_clear_HL(start, x, y, 2)
        elif current_shape == "H-T":
            
            create_clear_HT(start, x, y, 0)
            y += 1
            create_clear_HT(start, x, y, 1)
    
    else:
        available = 0
        for i in range(0,3):
            if map_list[(1+y) + 1][start+i+ x] == 0:
                available += 1
        
        if available == 3:
            if current_shape == "H-L":

                create_clear_HL(start, x, y, 0)
                y += 1
                create_clear_HL(start, x, y, 2)
            elif current_shape == "H-T":
                
                create_clear_HT(start, x, y, 0)
                y += 1
                create_clear_HT(start, x, y, 1)
        else:
            print("generating shape...")
            end_game()
            generate_shape()

def left_HL_HT():
    global y
    global x
    global start
    
    if (start+x)-1 >= 0:

        if map_list[1+y][(start+x)-1] == 0:
            
            if current_shape == "H-L":
                create_clear_HL(start, x, y, 0)
                x -=1
                create_clear_HL(start, x, y, 2)
                
            elif current_shape == "H-T":
                
                create_clear_HT(start, x, y, 0)
                x -= 1
                create_clear_HT(start, x, y, 1)

def right_HL_HT():
    global y
    global x
    global start
    
    if (start+2+x)+1 <= 9:

        if map_list[1+y][(start+2+x)+1] == 0:
            
            if current_shape == "H-L":
                create_clear_HL(start, x, y, 0)
                x +=1
                create_clear_HL(start, x, y, 2)
                
            elif current_shape == "H-T":
                
                create_clear_HT(start, x, y, 0)
                x += 1
                create_clear_HT(start, x, y, 1)
    
    else:
        print(x, "border limits!")

#------------------------------------------------------------------

#All shape controls
#user input + the current shape define the next movement/action for the tetris game

def move_down(): 
    global current_shape

    if current_shape == "H-L" or current_shape == "H-T":
        down_HL_HT()

    elif current_shape == "V-T":
        down_VT()

    elif current_shape == "Square":
        down_sqaure()

    elif current_shape == "Vertical":
        down_vertical()

    print_game()
    print_map_status()


    wn.onkey(move_down, "Down")
    wn.onkeypress(move_left, "Left")
    wn.onkeypress(move_right, "Right")
    wn.listen()

def move_left():
    global current_shape

    if current_shape == "H-L" or current_shape == "H-T":
        left_HL_HT()

    elif current_shape == "V-T":
        left_VT()

    elif current_shape == "Square":
        left_sqaure()

    elif current_shape == "Vertical":
        left_vertical()

    print_game()
    print_map_status()

    wn.onkeypress(move_down, "Down")
    wn.onkeypress(move_left, "Left")
    wn.onkeypress(move_right, "Right")
    wn.listen()

def move_right():
    global current_shape

    if current_shape == "H-L" or current_shape == "H-T":
        right_HL_HT()

    elif current_shape == "V-T":
        right_VT()

    elif current_shape == "Square":
        right_square()

    elif current_shape == "Vertical":
        right_vertical()

    print_game()
    print_map_status()

    wn.onkeypress(move_down, "Down")
    wn.onkeypress(move_left, "Left")
    wn.onkeypress(move_right, "Right")
    wn.listen()    

#------------------------------------------------------------------

#Score addition and UI

def add_point():# checks every row. If a row is full, then it clears that row and adds one point for the user
    global score

    for row in map_list:
        full = 0

        if row == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]:
            continue
        
        for space in row:
            if space != 0:
                full += 1
        
        if full == 10:
            score += 1
            map_list.remove(row)
            map_list.insert(1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            update_score()

def update_score(): #updates the scribe turtle with the new score, printing it on the turtle screen for the user to see
    global score
    global scribe
    scribe.write(f"Score: {score}", False, "Center", ("Arial", 15, "bold") )

#Game ending functions

def end_game(): #checks the beginning row in the map_list. If it already has values other than 0 in that row when another shape is generated, then the game ends
    global score

    if map_list[0] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        
        end_turtle = trtl.Turtle()
        end_turtle.color("black")
        end_turtle.ht()

        for i in range(1, 700, 20): #creates an increasing circle effect
            wn.tracer(0)
            end_turtle.goto(0, (-1 * i/2)-120)
            end_turtle.begin_fill()
            end_turtle.circle(i)
            end_turtle.end_fill()
            wn.tracer(1)

        #prints game over and final score to the user in red
        scribe.goto(0,0)
        scribe.color("red")
        scribe.write(f"GAME OVER!\nFinal Score: {score}", False, "center", ("Arial", 45, "bold"))
        wn.tracer(1)
        time.sleep(3)
        quit()

#Active Code
generate_shape()

print_game()
print_map_status()

wn.onkey(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.listen()

wn.mainloop()