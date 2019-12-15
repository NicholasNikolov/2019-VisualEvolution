xcor = 300
ycor = 300
xvel = 1
yvel = 2

def setup():
    size(600,600)
    
def draw():
    global xcor, ycor, xvel, yvel
    background(0)
    xcor += xvel
    ycor += yvel
    
    if xcor > width-10 or xcor < 10:
        xvel = -xvel
    if ycor > height-10 or ycor <10:
        yvel = -yvel
    
    ellipse(xcor,ycor,20,20)
