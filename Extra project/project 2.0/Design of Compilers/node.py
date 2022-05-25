import functions

class Node:
    def __init__(self, x, y):
        self.id = None
        self.x = x
        self.y = y
        self.size = 30
        self.defaultColor = (255,255,255)
        self.currentColor = self.defaultColor
        self.h = None
    
    def show(self):
        stroke(0)
        fill(self.currentColor[0], self.currentColor[1], self.currentColor[2])
        ellipse(self.x, self.y, self.size, self.size)
        self.__showId()

    def clicked(self):
        distance = dist(self.x, self.y, mouseX, mouseY)
        if(int(distance) < self.size):
            if(mouseButton == LEFT):
                self.currentColor = (255, 0, 0)
            return True
        else:
            self.currentColor = self.defaultColor
            return False

    def __showId(self):
        if self.id is None:
            return
        fill(0)
        textAlign(CENTER)
        textSize(20)
        text(self.id, self.x, self.y+self.size/4)
