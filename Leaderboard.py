import turtle

# Load Leaderboard
def load_leaderboard():
    leaderboard = []
    try:
        # Open file in read mode
        with open('leaderboard.txt', 'r') as file:
            # Add file info to leaderboard list
            for line in file:
                name, score = line.strip().split(',')
                leaderboard.append((name, int(score)))
    except FileNotFoundError:
        # Create the file if it doesn't exist
        open('leaderboard.txt', 'w').close()
    return leaderboard

# Return Highest Score Value
def get_highest_score():
    leaderboard = load_leaderboard()
    if leaderboard:
        highest_score = max(leaderboard, key=lambda x: x[1])[1]
        return highest_score
    else:
        return None

# Check if there is a new High Score
def check_high_score(score):
        leaderboard_data = load_leaderboard()
        if len(leaderboard_data) < 10 or score > leaderboard_data[-1][1]:
            # Display high score message
            high_score_message = "Insert your name : "
            name = turtle.textinput("New High Score!",high_score_message)
            update_leaderboard(name, score)

# Update Leaderboard
def update_leaderboard(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append((name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    leaderboard = leaderboard[:10]  # Keep only top 10
    with open('leaderboard.txt', 'w') as file:
        for entry in leaderboard:
            file.write(f"{entry[0]},{entry[1]}\n")
            
# Display Leaderboard
def display_leaderboard(callback):
    # Set up screen
    win = turtle.Screen()
    win.title("TURTLE")
    win.bgcolor('darkblue')
    win.setup(width=1.0,height=1.0)
    win.tracer(3)
    
    # Draw border
    def drawBorder():
        global border
        border = turtle.Turtle()
        border.penup()
        border.setpos(-290,-290)
        border.color('white')
        border.hideturtle()
        border.pendown()
        border.pensize(3)
        for side in range(4) :
            border.forward(600)
            border.left(90)
        border.hideturtle()
    drawBorder()
    
    # Draw Leaderboard 
    turtle.penup()
    turtle.goto(-110, 220)
    turtle.color("white")
    # Title
    turtle.write("Leaderboard", font=("Courier", 25, "bold"))
    # Leaderboard
    leaderboard_data = load_leaderboard()
    y = 200
    for i, (name, score) in enumerate(leaderboard_data, 1):
        turtle.goto(-135, y - i * 31)
        turtle.write(f"{i}. {name}: {score}", font=("Courier", 16, "normal"))
    turtle.hideturtle()
    
    # Draw button
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.goto(-145, -150)  
    pen.pendown()
    pen.setheading(0)
    pen.forward(300)
    pen.right(90)
    pen.forward(70)
    pen.right(90)
    pen.forward(300)
    pen.right(90)
    pen.forward(70)
    pen.hideturtle()
    
    # Write button text
    pen.goto(0, -200)  
    pen.write("Menu", font=("Courier", 20, "normal"), align="center")
    
    # Making button clickable
    def btnclick(x, y):
        if -150 < x < 155 and -220 < y < -150:
            # Clear everything
            win.clear()
            # Exit to Menu
            print("Exit to menu")
            callback()
    
    turtle.onscreenclick(btnclick)
    turtle.listen()
    # Keep the window open
    turtle.mainloop()


