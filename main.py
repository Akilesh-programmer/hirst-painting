# # Importing a class called colorgram. It just identifies colors from an image and then gives it in the form of rgb values.
# import colorgram
# # Creating a object out of the class. Then giving the inputs it needs to identify the colors and give the rgb value.
# colors = colorgram.extract('image.jpg', 20)

# # Creating an empty list to hold the rgb value of colors.
# rgb_colors = []

# # Creating a for loop to go through the colors where we have all the rgb values. It is not formatte properly so that getting hold of the r g and b values of each colors stored with help of methods and then appending them to the newly formed empty list.
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b 
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# # Printing the color values.
# print(rgb_colors)

# # Copy pasting the output that we got from the above thing. Then putting the values in a online rgb maker. Then deleting the white ones. Then saving them into a list. Then commenting out all the before code because I got my colors.





color_list = [(236, 35, 108),(145, 28, 64), (239, 75, 35), (6, 148, 93),(231, 68, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]



# Importing the turtle module   
import turtle as t

# Importing the random function.
import random


# Creating a object named akilesh from the turtle class
akilesh = t.Turtle()

# Craeting a screen object to hold the image in the screen.
my_screen = t.Screen()

# Doing few things with my_screen so that rgb color gets printed.
my_screen.colormode(255)

# Hiding the turtle so that while painting it would be nice to see.
akilesh.ht()

# First getting my akilesh to a good position in the screen from which it will be good to create a 10 / 10 square.
akilesh.penup()
akilesh.speed("fastest")
akilesh.backward(300)
akilesh.left(90)
akilesh.forward(250)
akilesh.right(180)

# Creating a function to draw 10 dots in a column with 50 gap between them.
def draw_10_dots():
    for n in range(10):
        # Creating a random color for the dot.
        rgb = (random.choice(color_list))
        akilesh.color(rgb)
        akilesh.dot(20)
        akilesh.forward(50)

# Creating a function to get my turtle to a correct position from the bottom side to execute the above draw_10_dots function perfectly once again. So that it will be good in a for loop.
def correct_position_bottom():
    akilesh.backward(50)
    akilesh.left(90)
    akilesh.forward(50)
    akilesh.left(90)

# Creating a function to get my turtle to a correct position from the top side to execute the above draw_10_dots function perfectly once again. So that it will be good in a for loop.
def correct_position_top():
    akilesh.backward(50)
    akilesh.right(90)
    akilesh.forward(50)
    akilesh.right(90)

# Creating a variable assigned to 0.
num = 0

# Creating the for loop to create the 10 / 10 square.
for n in range(10):
    # Adding the num variable to track the number of times the code has looped through.
    num += 1
    draw_10_dots()
    # If the num is even then it means that the turtle is at the top side. So calling the top function.
    if num % 2 == 0:
        correct_position_top()
    # If the num is not an even number then it means that the turtle is at the bottom side. So calling the bottom function.
    else:
        correct_position_bottom()
    


# Using a method called exit on click to close the screen only after clicking on it.
my_screen.exitonclick()