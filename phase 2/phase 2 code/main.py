import backend
import processing_py
import keyboard
import vector
import AST
# import Ui_textInput
from PyQt5 import*

app = processing_py.App(1600, 900)
root = None
# parseTree = backend.restree
# try:
#     root = parseTree.listofnodes[0]
# except:
#     pass

prevInput = ''

def readFile():
    global root
    global prevInput
    file = open("input.txt", 'r')
    input = file.readline()
    # print(input)
    if input != prevInput:
        
        try:
            state,restree,asttree = backend.checkinput(input)
            root = restree.listofnodes[0]
            AST.astdrawal(input)
        except:
            root = None
        prevInput = input

def setup():
    import subprocess
    subprocess.Popen(["python" , "Ui_textInput.py"])
    file = open("input.txt", 'w')
    file.write('')
    pass

def draw():
    app.background(0)
    generateTree(root, app.width/2, 30)
    readFile()


def generateTree(root : backend.node, x, y):
    fringe = []
    length = 250
    angle = 120
    children = expandNode(root, x, y, length=length, angle = angle)
    fringe.extend(children)
    while fringe:
        node = fringe.pop(0)
        
        children = expandNode(node, node.x, node.y, length = node.radius, angle=node.angle)
        
        fringe.extend(children)
    
        

def expandNode(node: backend.node, x, y, length, angle):
    if node is None:
        return [] 
    anglesSum = angle
    textSize = 12
    app.fill(255)
    app.stroke(255)
    app.textSize(textSize)
    app.textAlign(processing_py.CENTER)
    vec = vector.obj(rho = length, phi = radian(90 + (anglesSum/2)) )
    vec = vec.to_xy()

    
    app.text(node.name, x, y)
    children = node.adjacentlist
    if children:
        if len(children) == 1:
            app.fill(255,0,0)
            vec = vector.obj(rho = length/2, phi = radian(90))
            step = 0
        elif len(children) == 2:
            step = radian(anglesSum)
        else:
            step =  radian(anglesSum / (len(children)-1))
            
        for child in children:
            child.name = child.name.replace("'", "^")
            app.line(x, y, x + vec.x , y+ vec.y - textSize)
            child.x = x + vec.x
            child.y = y + vec.y
            child.radius = length*0.80
            child.angle = angle*0.80
            app.text(child.name, child.x, child.y)
            vec = vec.rotateZ(-step)
            
    return children
  
    
def radian(angle):
    return angle*(processing_py.PI/180)
    
    



if __name__ == "__main__":
    setup()
    while(not app.isDead._flag):
        draw()
        app.redraw()
        

    exit()
