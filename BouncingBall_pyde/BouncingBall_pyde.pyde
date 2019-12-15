ballList = []

def setup():
    size(600,600)
    for i in range(550):
        ballList.append(Ball(random(width),random(height)))
    smooth()
    
def draw():
    background(0)
    for ball in ballList:
        ball.update()
    


class Ball:
    def __init__(self,x,y):
        self.xcor = x
        self.ycor = y
        self.xvel = random(-2,2)
        self.yvel = random(-2,2)
        self.col = color(random(255),random(255),random(255))
        self.size = random(5,60)

    def update(self):
        self.xcor += self.xvel
        self.ycor += self.yvel
        
        if self.xcor > width - 10 or self.xcor < 10:
            self.xvel = -self.xvel
        if self.ycor > height - 10 or self.ycor < 10:
            self.yvel = -self.yvel
        fill(self.col)
        ellipse(self.xcor,self.ycor,self.size,self.size)
