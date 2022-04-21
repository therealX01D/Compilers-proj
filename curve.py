import functions

class Curve():
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.mainLine = functions.vector(node1 = self.node1, node2= self.node2)
        self.defaultColor = (0, 0, 0)
        self.currentColor = self.defaultColor
        self.points = []
        self.density = 10
        self.endX = None
        self.endY = None
        self.startX = None
        self.startY = None
        
    def __initPoints(self):
        self.points = []
        if(self.node1 == self.node2):
            pointer = PVector(0, -70)
            pointer.rotate(PI/6)
            for i in range(3):
                pointer.rotate(-i* (PI/12))
                finalX = self.node1.x + pointer.x
                finalY = self.node1.y + pointer.y
                self.points.append(PVector(finalX, finalY))
                 
        else:
            self.mainLine = functions.vector(node1 = self.node1, node2 = self.node2)
            mainLineMag = self.mainLine.mag()
            for i in range(1,self.density):
                x = (i* mainLineMag)/self.density 
                v = self.mainLine.copy()   
                v.setMag(x)
                normal = v.copy()
                normal.rotate(PI/2)
                mag = self.__curveture(x)
                normal.setMag(mag)
                finalX = self.node1.x + v.x + normal.x
                finalY = self.node1.y + v.y + normal.y
                self.points.append(PVector(finalX, finalY))
        
       
    def __curveture(self, x):
        return x*(x-self.mainLine.mag())/(2*self.mainLine.mag()+1)
    
    def show(self):
        self.__initPoints()
        points = self.points
        stroke(self.currentColor[0], self.currentColor[1], self.currentColor[2])
        for i in range(len(points)-1):
            currentPoint = points[i]
            nextPoint = points[i+1]
            line(currentPoint.x, currentPoint.y, nextPoint.x, nextPoint.y)

        self.__showArrow()
        self.__adjustStartEdge()
        firstPoint = points[0]
        lastPoint = points[-1]
        line(self.startX, self.startY, firstPoint.x, firstPoint.y)
        line(self.endX, self.endY, lastPoint.x, lastPoint.y)
    
    def __showArrow(self):
        lastPoint = self.points[-1]
        lastLineV = functions.vector(x1 = lastPoint.x, y1 = lastPoint.y, x2 = self.node2.x, y2=self.node2.y)
        mag = lastLineV.mag()
        lastLineV.setMag(mag - self.node2.size/2)
        self.endX = lastPoint.x + lastLineV.x
        self.endY = lastPoint.y + lastLineV.y
        invLastLineV = functions.vector(x2 = lastPoint.x, y2 = lastPoint.y, x1 = self.endX, y1=self.endY)
        invLastLineV.setMag(15)
        flank1 = invLastLineV.copy()
        flank2 = invLastLineV.copy()
        flank1.rotate(PI/6)
        flank2.rotate(-PI/6)
        flank1.add(PVector(self.endX, self.endY))
        flank2.add(PVector(self.endX, self.endY))
        line(self.endX, self.endY, flank1.x, flank1.y)
        line(self.endX, self.endY, flank2.x, flank2.y)
        
    def showWeight(self, weights):
        textSize(24)
        textAlign(CENTER)
        if not weights:
            return
        copy  = weights[:]
        string = ", ".join(map(str, copy))
        arrayLen = len(self.points)
        fill(255)
        if(arrayLen%2 == 0):
            middleP = self.points[(arrayLen+1)/2]
            text(string, middleP.x, middleP.y)
        else:
            middleP1 = self.points[arrayLen/2]
            middleP2 = self.points[(arrayLen/2)+1]
            x = (middleP1.x + middleP2.x)/2
            y = (middleP1.y + middleP2.y)/2
            text(string, x, y)
        
    def clicked(self):
        firstPoint = self.points[0]
        lastPoint = self.points[-1]
        if(functions.isLineClicked(self.node1.x, self.node1.y, firstPoint.x, firstPoint.y)):
            self.currentColor = (0, 51, 128)
            return True
        if(functions.isLineClicked(lastPoint.x, lastPoint.y, self.endX, self.endY)):
            self.currentColor = (0, 51, 128)
            return True
        for i in range (len(self.points)-1):
            currentPoint = self.points[i]
            nextPoint = self.points[i+1]
            if(functions.isLineClicked(currentPoint.x, currentPoint.y, nextPoint.x, nextPoint.y)):
                self.currentColor = (0, 51, 128)
                return True
        self.currentColor = self.defaultColor
        return False
    
    def __adjustStartEdge(self):
        firstPoint = self.points[0]
        firstLineVec = functions.vector(x1 = firstPoint.x, y1 = firstPoint.y, x2 = self.node1.x, y2 = self.node1.y)
        mag = firstLineVec.mag()
        firstLineVec.setMag(mag - self.node1.size/2)
        self.startX = firstPoint.x + firstLineVec.x
        self.startY = firstPoint.y + firstLineVec.y