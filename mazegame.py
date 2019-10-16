import math
import turtle
# Creates the screen


wn = turtle.Screen()
wn.bgcolor("indigo")
wn.title("Anastasia's Doolhof")
wn.setup(700, 700)

images = ["kistje.gif", "standing-up-man-.gif"]
for image in images:
    turtle.register_shape(image)


# Defines the pen as turtle class
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("purple")
        self.penup()
        self.speed(0)


# Defines the player as turtle class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("standing-up-man-.gif")
        self.color("indigo")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        self.goto(self.xcor(), self.ycor())
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        self.goto(self.xcor(), self.ycor())
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        self.goto(self.xcor(), self.ycor())
        # Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        self.goto(self.xcor(), self.ycor())
        # Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("kistje.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Add treasures list
treasures = []

# Create class instances
pen = Pen()
player = Player()


# Set speed
speed = 10


# Create wall coordinate list
walls = []

# Set keyboard bindings
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")


# Create level list with lvl 0 empty so you start at lvl 1
levels = [""]


# Define first lvl
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXXT XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX  GXXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                 T  X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"]


# Add maze to mazes list
levels.append(level_1)


# Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            # Don't switch the order of y and x
            character = level[y][x]
            # Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check if it is a P (player)
            if character == "P":
                player.goto(screen_x, screen_y)

            # Check if it is a T (treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))



# keyboard functions
def turnleft():
    player.left()


def turnright():
    player.right()


def moveforward():
    player.forward()


def movebackwards():
    player.backward()



# Set up the lvl
setup_maze(levels[1])


# Main Game Loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    wn.update()

