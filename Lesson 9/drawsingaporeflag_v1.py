import turtle

# singapore national flag Proportion:	3:2
flag_width = 450
flag_height = 300
radius = 55
star_length = 20

# move the pen to a position so we can draw the flag at the centre of the screen
turtle.penup()
turtle.setpos(-flag_width/2, 0)
turtle.pendown()

# draw a red rectangle filled with red color
turtle.color("red")
turtle.begin_fill()
for i in range(2):
    turtle.forward(flag_width)
    turtle.left(90)
    turtle.forward(flag_height/2)
    turtle.left(90)
turtle.end_fill()   # final direction: point right


# move the pen to the bottom-left corner
turtle.penup()
turtle.right(90)    # direction: point down
turtle.forward(flag_height/2)
turtle.pendown()
turtle.left(90)     # direction: point right

# draw a black border for the flag
turtle.color("black")
for i in range(2):
    turtle.forward(flag_width)
    turtle.left(90)
    turtle.forward(flag_height)
    turtle.left(90) # final direction: point right   




