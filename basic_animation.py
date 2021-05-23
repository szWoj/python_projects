# https://www.youtube.com/watch?v=mIQR6GUxZZI&ab_channel=TokyoEdTech
import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")


wn.register_shape("alien1.gif")
wn.register_shape("bomb.gif")

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self) #it initializes this turtule object
        self.penup()
        self.shape("alien1.gif")
        self.color("green")
        self.frame = 0
        self.frames = ["alien1.gif", "bomb.gif"]

    def animate(self): # there must be an argument here because we are inside the class
        self.frame += 1
        if self.frame >= len(self.frames): # it doesnt go beyond player.frames list
            self.frame = 0
        self.shape(self.frames[self.frame])

        wn.ontimer(self.animate, 500)

##player = turtle.Turtle()
# only 5 built in shapes: circle triangle square, arrow, turtle

##player.shape("alien1.gif")
##player.color("green")
##player.frame = 0
##player.frames = ["alien1.gif", "bomb.gif"]

player = Player() # when it runs, this "self" inside the class is replaced by "player"
player.animate()


player2 = Player()
player2.goto(-100, 0)
player2.animate()

player3 = Player()
player3.goto(100, 0)
player3.animate()
##def player_animate():
##    player.frame += 1
##    if player.frame >= len(player.frames): # it doesnt go beyond player.frames list
##        player.frame = 0
##    player.shape(player.frames[player.frame])
###3.    if player.frame == 0:
###3.        player.shape("alien1.gif")
###3.        player.frame = 1
###3.    elif player.frame ==1:
###3.        player.shape("bomb.gif")
###3.        player.frame = 0
##2.    if player.shape() == "alien1.gif":
##2.        player.shape("bomb.gif")
##2.    elif player.shape() == "bomb.gif":
##2.        player.shape("alien1.gif")
#1.    player.shape("square")
#1.    time.sleep(0.5)
#1.    player.shape("circle")
#1.    time.sleep(0.5)
        #Set timer, 500 miliseconds, hald a second
##    wn.ontimer(player_animate, 500) # no parentasis when using function as an argument

##player_animate()
#player.animate()

while True:
    wn.update()
##    print("Main loop")
    






wn.mainloop()
