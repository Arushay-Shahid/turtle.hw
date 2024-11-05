import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Hexagon Drawing")

# Set up the turtle
board = turtle.Turtle()
board.shape("turtle")
board.color("blue")
board.pensize(2)

# Set the side length of the hexagon
side_length = 100

# Draw the hexagon
for i in range(6):
    board.forward(side_length)  # Move forward by the side length
    board.right(60)             # Turn 60 degrees to the right to form a hexagon

# Hide the turtle and keep the window open
board.hideturtle()
turtle.done()
