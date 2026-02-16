import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("#f0f0f0")
cat = turtle.Turtle()
cat.speed(3)
cat.width(3)

def draw_circle(color, radius, x, y):
    cat.penup()
    cat.fillcolor(color)
    cat.goto(x, y)
    cat.pendown()
    cat.begin_fill()
    cat.circle(radius)
    cat.end_fill()

def draw_ear(x, y, tilt):
    cat.penup()
    cat.goto(x, y)
    cat.setheading(tilt)
    cat.pendown()
    cat.fillcolor("#ffb7c5") # Pink inner ear
    cat.begin_fill()
    for _ in range(3):
        cat.forward(60)
        cat.left(120)
    cat.end_fill()

# --- Draw the Body/Face ---
draw_circle("#333333", 100, 0, -100) # Head

# --- Draw the Ears ---
draw_ear(-70, 70, 110)  # Left ear
draw_ear(20, 85, 70)    # Right ear

# --- Draw the Eyes ---
draw_circle("white", 15, -35, 20) # Left eye
draw_circle("black", 7, -35, 30)
draw_circle("white", 15, 35, 20)  # Right eye
draw_circle("black", 7, 35, 30)

# --- Draw the Nose ---
draw_circle("#ffb7c5", 8, 0, 0)

# --- Draw the Whiskers ---
cat.penup()
cat.color("#333333")
# Left whiskers
cat.goto(-20, 0)
cat.setheading(170)
cat.pendown()
cat.forward(60)
cat.penup()
cat.goto(-20, -10)
cat.setheading(190)
cat.pendown()
cat.forward(60)

# Right whiskers
cat.penup()
cat.goto(20, 0)
cat.setheading(10)
cat.pendown()
cat.forward(60)
cat.penup()
cat.goto(20, -10)
cat.setheading(-10)
cat.pendown()
cat.forward(60)

# Hide turtle and finish
cat.hideturtle()



def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)
turtle. done()