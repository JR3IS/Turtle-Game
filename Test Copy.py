import turtle
import random
import time

score = 0
high_score = 0
scr = None
delay = 0.025

# Set up screen
win = turtle.Screen()
win.title("TURTLE")
win.bgcolor('darkblue')
win.setup(width=1.0,height=1.0)
win.tracer(3)

# Draw border
def drawBorder():
    mypen = turtle.Turtle()
    mypen.penup()
    mypen.setpos(-290,-290)
    mypen.color('white')
    mypen.hideturtle()
    mypen.pendown()
    mypen.pensize(3)
    for side in range(4) :
        mypen.forward(600)
        mypen.left(90)
    mypen.hideturtle()

# Draw scoreboard 
def drawScoreboard():
    global scr
    if scr is None:
        scr = turtle.Turtle()
        scr.speed(0)
        scr.hideturtle()
        scr.penup()
        scr.color('white')
    else:
        scr.clear()  # Clear the previous scoreboard
    scr.goto(0, 330)
    scr.write(f"Score: {score} High Score: {high_score}", align='center', font=('courier', 15, 'normal'))

# Create Player
def createPlayer():  
    player = turtle.Turtle()
    player.color('green')
    player.shape('turtle')
    player.shapesize(stretch_wid=2, stretch_len=2, outline=1)
    player.penup()
    player.speed(0) 
    return player

# Create Obstacles
def createObstacle():    
    obstacle = turtle.Turtle()
    obstacle.color('red')
    obstacle.shape('turtle')
    obstacle.penup()
    obstacle.speed(0)
    obstacle.setpos(random.randint(-290,290),random.randint(-290,290))
    obstacle.right(random.randint(0,360))
    return obstacle

# Create Goal
def createGoal():  
    goal = turtle.Turtle()
    goal.speed(0)
    goal.shape("circle")
    goal.color("green")
    goal.penup()
    goal.setpos(random.randint(-290,290),random.randint(-290,290))
    goal.right(random.randint(0,360))
    return goal

# Set speed variables
player_speed = 2
obstacle_speed = 1

# Define movement functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global player_speed
    player_speed += 1

def decreasespeed(): 
    global player_speed
    player_speed -= 1

# Check collision
def isCollision(t1,t2):
    if t1.distance(t2) < 20:
        return True
    else : 
        return False
    
# Set keyboard bindings 
turtle.listen()

# Main game loop
def main_game_loop():
    global player, obstacles, goal, game_over, delay, player_speed, obstacle_speed  # Make variables global
    
    # Create game objects
    drawBorder()
    drawScoreboard()
    player = createPlayer()
    obstacles = []
    goal = createGoal()
    
    # Set game state to NOT game over
    game_over = False
    
    # Bind movement functions to player object
    turtle.onkey(turnleft, 'Left')
    turtle.onkey(turnright, 'Right')
    turtle.onkey(increasespeed, 'Up')
    turtle.onkey(decreasespeed, 'Down')
    
    # Start the game loop
    while True:
        
        # Move the player
        player.forward(player_speed)
    
        # Player: Check Boundaries
        if player.xcor() > 290 or player.xcor() <-290 :
            player.right(180)
        if player.ycor() > 290 or player.ycor() <-290 :
            player.right(180)
        
        # Obstacles Setup
        for obstacle in obstacles :
            # Move the obstacles
            obstacle.forward(obstacle_speed)
            # Obstacles: Check Boundaries
            if obstacle.xcor() > 290 or obstacle.xcor() <-290 :
                obstacle.right(180)
            if obstacle.ycor() > 290 or obstacle.ycor() <-290 :
                obstacle.right(180)
            
        # Check collision with goal
        if isCollision(player,goal):
            goal.goto(random.randint(-290,290),random.randint(-290,290))
            goal.right(random.randint(0,360))
            # Add a new obstacle
            obstacles.append(createObstacle())  
            # Adjust the timing
            if delay >= 0.001:
                delay -= 0.001
            else :
                player_speed += 0.2
                obstacle_speed += 0.1
            # Update score
            global score, high_score
            score += 100
            if high_score < score:
                high_score = score
            drawScoreboard()
       
        # Check collisions with obstacles 
        if any(isCollision(player, obs) for obs in obstacles):
            # Hide game objects
            player.hideturtle()
            goal.hideturtle()
            for obs in obstacles:
                    obs.hideturtle()
            # Reset score
            score = 0
            # Game over screen
            turtle.hideturtle()
            turtle.color("white")
            turtle.goto(0, 0)
            turtle.write(" Game Over", align="center", font=("Courier", 24, "normal"))
            game_over = True
            break
        
        # Apply the delay
        time.sleep(delay)

def reset_game():
    global game_over, player_speed, obstacle_speed, delay
    if game_over:
        # Clear everything
        player.clear()
        for obstacle in obstacles:
            obstacle.clear()
        goal.clear()
        turtle.clear()
        # Reset delay
        delay = 0.025
        # Reset speed variables
        player_speed = 2
        obstacle_speed = 1
        # Recreate game elements and start new game loop
        main_game_loop()


# Bind reset function
game_over = True  # Initialize game_over to True
turtle.onkey(reset_game, 'r')

# Call the main game loop to start the game
main_game_loop()

# Keep the window open
win.mainloop()