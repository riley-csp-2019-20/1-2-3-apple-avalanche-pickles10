#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -150
apple_letter_x_offset = -12
apple_letter_y_offset = -30

screen_width = 300
screen_height = 300
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("tree.gif")
apple = trtl.Turtle()
apple.speed(3)
apple.pu()
wn.tracer(False)

def reset_apple(active_apple):
  
  list_length = len(alphabet
)
  if (list_length != 0):
    index = rand.randint(0, list_length)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    active_apple.st()
    draw_apple(active_apple, alphabet
.pop(index))

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  draw_letter(letter, active_apple)
  wn.update()

def falling_apple():
  wn.tracer(True)
  apple.clear()
  apple.goto(apple.xcor(), ground_height)
  apple.ht()
  wn.tracer(False)
  reset_apple(apple)

# This function takes care of font and color.
def draw_letter(letter, active_apple):
  active_apple.color("red")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 30, "bold"))
  active_apple.setpos(remember_position)

# This call to the onkeypress function sets draw_letter as the function
# that will be called when the "a" key is pressed.

reset_apple(apple)
wn.onkeypress(falling_apple,"a")
#wn.onkeypress(falling_apple, str(key_bind))

wn.listen()
wn.mainloop()