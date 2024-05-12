import os
import turtle 

def display_controls(callback):
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
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    icons_dir = os.path.join(script_dir, "Icons")
    print(f"ICONS PATH {icons_dir}")
    help
    
    # Register PNG images as shapes
    win.register_shape(os.path.join(icons_dir, "LR.gif"))
    win.register_shape(os.path.join(icons_dir, "UD.gif"))

    # Draw LR image
    lr_turtle = turtle.Turtle()
    lr_turtle.speed(0)
    lr_turtle.penup()
    lr_turtle.shape(os.path.join(icons_dir, "LR.gif"))  
    lr_turtle.goto(-120, 60)  
    lr_turtle.stamp()  
    lr_turtle.hideturtle()

    # Draw UD image
    ud_turtle = turtle.Turtle()
    ud_turtle.speed(0)
    ud_turtle.penup()
    ud_turtle.shape(os.path.join(icons_dir, "UD.gif"))
    ud_turtle.goto(135, 60)  
    ud_turtle.stamp()  
    ud_turtle.hideturtle()
    
    # Write Texts
    def write_text(text,x,y,size,style):
        pen = turtle.Turtle()
        pen.penup()
        pen.goto(x, y)
        pen.color('white')  # Change color to white
        pen.write(text, font=("courier",size,style))
        pen.hideturtle()
        
    # Title
    title = "Controls"
    write_text(title,-75,220,25,"bold")
    
    # LR arrows
    lr_text = '''Change the turtle's 
     direction'''
    write_text(lr_text,-220,-60,14,"normal")
    
    # UD arrows
    ud_text = '''Increase or decrease
    turtle speed'''
    write_text(ud_text,25,-60,14,"normal")
    
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
    pen.penup()
    
    # Write button text
    pen.goto(0, -200)  
    pen.pendown()
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


'''
def placeholder_function() :
    print("Something")


display_controls(placeholder_function) 

'''