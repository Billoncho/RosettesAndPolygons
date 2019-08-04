# RosettesAndPolygons.py
# Billy Ridgeway
# A spiral alternating between polygons and rosettes.

import turtle       # Imports turtle graphics.
t = turtle.Pen()    # Creates a new turtle called t.
t.speed(0)          # Sets the speed of the pen to fast.

# Ask the user for the number of sides or circles, default to 4.
sides = int(turtle.numinput("Number of sides",
                             "How many sides in your spiral?", 4))

# Our outter spiral loop for polygons and rosettes, from size 5 to 75.
for m in range(5,75):           # Sets range in the variable 'm'.
    t.left(360/sides + 5)       # Moves the pen left by 360 divided by the number of sides entered by the user plus 5.
    t.width(m//25 + 1)          # Sets the pen's width to the variable 'm' divided by 25s quotient plus 1.
    t.penup()                   # Lifts the pen to prevent writing while moving to the next position.
    t.forward(m*4)              # Moves the pen forward by the variable 'm' times 4.
    t.pendown()                 # Puts the pen down and ready to draw.

    # Draw a little rosette at each EVEN corner of the spiral.
    if (m % 2 == 0):            # Divides 'm' by 2 and if there is no remainder runs this loop.
        for n in range(sides):  # Sets the variable 'n' to the number of sides entered by the user.
            t.circle(m/3)       # Draws a circle the size of the variable 'm' divided by 3.
            t.right(360/sides)  # Moves the pen right by 360 degrees divided by the number of sides entered by the user.

    # OR, draw a little polygon at each ODD corner of the spiral.
    else:                       # If there was a remainder, then the number was an ODD number and a polygon will be drawn.
        for n in range(sides):  # Sets the variable 'n' to the number of sides entered by the user.
            t.forward(m)        # Moves the pen forward by the number contained in the variable 'm'.
            t.right(360/sides)  # Moves the pen right by 360 degrees divided by the number of sides entered by the user.
    
