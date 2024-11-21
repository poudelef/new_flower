import turtle
import math

def spiral(t, n, length, angle, factor):
    """Draw a spiral with n line segments."""
    for i in range(n):
        t.forward(length)
        t.left(angle)
        length *= factor

def sunflower_petal(t, size):
    """Draw a single sunflower petal."""
    t.color("yellow")
    t.begin_fill()
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)
    t.end_fill()

def sunflower(t, n, size):
    """Draw a sunflower with n petals."""
    for i in range(n):
        sunflower_petal(t, size)
        t.left(360 / n)
    
    # Draw the center of the sunflower
    # t.color("brown")
    t.begin_fill()
    t.circle(size / 3)
    t.end_fill()

def stem(t, length):
    """Draw the stem of the sunflower."""
    t.color("green")
    t.pensize(3)
    t.right(90)
    t.forward(length)
    t.left(90)

# Display a message with cool animation
def display_message():
    """Display the text message with animation."""
    message_turtle = turtle.Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.color("red")
    message_turtle.goto(0, -300)
    
    message = "Hello Cutie meri dhrumaniii. How are you?)"
    for i in range(1, len(message) + 1):
        message_turtle.clear()
        message_turtle.write(message[:i], align="center", font=("Arial", 24, "bold"))
        screen.update()

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1.0,height=1.0)
screen.bgcolor("light blue")
screen.title("Sunflower with Leaves")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the speed to the fastest
t.hideturtle()

# Draw the stem
stem(t, 200)

# Draw the sunflower
t.penup()
t.goto(0, 0)
t.pendown()
sunflower(t, 24, 100)

# Start the animation loop
def animate():
    """Rotate the sunflower and display the message after animation."""
    for _ in range(360):  # Rotate the sunflower 360 degrees
        t.left(1)
        screen.update()
    display_message()

# Start the animation
screen.tracer(0)  # Turn off automatic screen updates
animate()

turtle.done()
