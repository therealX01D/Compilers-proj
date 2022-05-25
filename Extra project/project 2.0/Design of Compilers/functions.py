import math
import node

    
def direction(node1 = None, node2 = None,x1= None, y1= None, x2= None, y2= None):
    v = vector(node1 = node1 , node2 = node2, x1 = x1, y1 = y1, x2 = x2, y2 = y2)
    v.normalize()
    return v

def vector(node1 = None, node2 = None, x1 = None, y1 = None, x2 = None, y2 = None):
    if not(node1 is None or node2 is None):
        x1 = node1.x
        y1 = node1.y
        x2 = node2.x
        y2 = node2.y
        diffX = x2 - x1
        diffY = y2 - y1
        v = PVector(diffX, diffY)
        return v
    elif not(x1 is None or y1 is None or x2 is None or y2 is None):
        diffX = x2 - x1
        diffY = y2 - y1
        v = PVector(diffX, diffY)
        return v
    else:
        return None
    
def isLineClicked(x1, y1, x2, y2):
        edgeDirection  = direction(x1 = x1, y1 = y1, x2 = x2, y2 = y2)
        currentDirection = direction(x1 = x1, y1 = y1, x2 = mouseX, y2 = mouseY)
        edgeLength = dist(x1, y1, x2, y2)
        currentLength = dist(x1, y1, mouseX, mouseY)
        space = int(edgeDirection.dot(currentDirection)*1000)
        if(space >= 980 and currentLength< edgeLength+5):
            return True
        return False
    
def arrayToString(arr):
    if not arr:
        return ''
    finalString = ''
    for element in arr:
        finalString += str(element)
        finalString += '\n'
    
    return finalString

def createPath(x1, y1 , x2, y2, density = 10):
    path = []
    lineVector = vector(x1 = x1, y1 = y1, x2 = x2, y2 = y2)

    mag = lineVector.mag()
    path.append(PVector(x1, y1))
    for i in range(0, density+1):
        x = (i* mag)/density
        v = lineVector.copy()
        v.setMag(x)
        finalX = v.x + x1
        finalY = v.y + y1
        path.append(PVector(finalX, finalY))
    path.append(PVector(x2, y2))
    
    return path