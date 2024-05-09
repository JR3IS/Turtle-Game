import turtle

def create_menu(button_functions):
    win = turtle.Screen()
    win.title("TURTLE")
    win.bgcolor('darkblue')
    win.setup(width=1.0, height=1.0)
    win.tracer(3)

    pen = turtle.Turtle()
    pen.speed(0)

    # Draw border
    def drawBorder():
        mypen = turtle.Turtle()
        mypen.penup()
        mypen.setpos(-290, -290)
        mypen.color('white')  # Change color to white
        mypen.hideturtle()
        mypen.pendown()
        mypen.pensize(3)
        for side in range(4):
            mypen.forward(600)
            mypen.left(90)
        mypen.hideturtle()

    drawBorder()

    def draw_title():
        title_pen = turtle.Turtle()
        title_pen.penup()
        title_pen.color('white')
        title_pen.goto(0, 200)  # Adjusted position
        title_pen.write("TURTLE", align="center", font=("Courier", 40, "bold"))
        title_pen.hideturtle()

        # Draw green turtles on each side of the title
        draw_green_turtle(-150, 230)
        draw_green_turtle(150, 230)

    def draw_green_turtle(x, y):
        turtle_pen = turtle.Turtle()
        turtle_pen.shapesize(1.5)
        turtle_pen.penup()
        turtle_pen.color('green')
        turtle_pen.shape('turtle')
        turtle_pen.goto(x, y)
        turtle_pen.setheading(turtle_pen.towards(0, 200))
        turtle_pen.showturtle()

    draw_title()

    # Menu Options
    OPTIONS = ["Start Game", "Controls", "High Score", "Quit Game"]
    OPTION_Y_COORDINATES = [110, 20, -70, -160]
    OPTION_HEIGHT = 70

    def write_text(text, y):
        pen.penup()
        pen.goto(-110, y - 15)  # Adjusted position
        pen.color('white')  # Change color to white
        pen.write(text, font=("courier", 20, "normal"))

    def draw_button(y):
        pen.penup()
        pen.goto(-145, y + OPTION_HEIGHT / 2)
        pen.pendown()
        pen.color('white')
        pen.setheading(0)
        pen.forward(300)
        pen.right(90)
        pen.forward(OPTION_HEIGHT)
        pen.right(90)
        pen.forward(300)
        pen.right(90)
        pen.forward(OPTION_HEIGHT)
        pen.right(90)
        pen.hideturtle()

    for text, y in zip(OPTIONS, OPTION_Y_COORDINATES):
        draw_button(y)
        write_text(text, y)

    # Making options clickable
    def btnclick(x, y):
        for index, option_y in enumerate(OPTION_Y_COORDINATES):
            if option_y - OPTION_HEIGHT / 2 < y < option_y + OPTION_HEIGHT / 2 and -150 < x < 150:
                button_functions[index]()
                turtle.clearscreen()
                return
        print("Click One Of The Options!")
        print(x, y)

    turtle.onscreenclick(btnclick)
    turtle.listen()

    turtle.done()
