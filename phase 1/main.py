import node
import edge
import graph
import functions
import tokenizer
import stringmatching
import errorfinder
import backend
import States
add_library('controlP5')


mainGraph = graph.DiGraph()
acceptanceStates = []
listenForNewWeight = False
listenForInputString= False

def setup():


    global outputField
    font = createFont("arial",16)
    global cp5
    cp5 = ControlP5(this)
    smooth()
    

    size(1600, 900)

    (cp5.addToggle('Acceptance State')
        .setPosition(1300,40)
        .setSize(20,20)
        .setColorBackground(color(0, 0, 0))
        .setColorForeground(color(255,255,0))
        .setColorActive(color(0,255,0))
        .setFont(font)
    )

    (cp5.addToggle('ID/NUM')
        .setPosition(1300,150)
        .setSize(20,20)
        .setColorBackground(color(0, 0, 0))
        .setColorForeground(color(255,255,0))
        .setColorActive(color(0,255,0))
        .setFont(font)
    )
    (cp5.addToggle('Operator')
        .setPosition(1300,210)
        .setSize(20,20)
        .setColorBackground(color(0, 0, 0))
        .setColorForeground(color(255,255,0))
        .setColorActive(color(0,255,0))
        .setFont(font)
    )
    (cp5.addToggle('Other')
        .setPosition(1300,270)
        .setSize(20,20)
        .setColorBackground(color(0, 0, 0))
        .setColorForeground(color(255,255,0))
        .setColorActive(color(0,255,0))
        .setFont(font)
    )
    (cp5.addTextfield('Add Custom Weight')
        .setPosition(1300,330)
        .setSize(200,25)
        .setColorBackground(color(0, 0, 0))
        .setColorForeground(color(255,255,0))
        .setColorActive(color(0,255,0))
        .setFont(font)
    )
    (cp5.addTextfield('Input String')
        .setPosition(1300,390)
        .setSize(200,25)
        .setColorBackground(color(0, 0, 0))
        .setColorForeground(color(255,255,0))
        .setColorActive(color(0,255,0))
        .setFont(font)
        .setAutoClear(False)
    )
    outputField = (cp5.addTextarea("output")
        .setPosition(1300, 450)
        .setSize(200, 400)
        .setColorBackground(color(0, 0, 0))
        .setColorForeground(color(255,255,0))
        .setColorActive(color(0,255,0))
        .setFont(font)
        
    )
    textAlign(LEFT)



def draw():
    global acceptanceToggle
    global Id_NumToggle
    global operatorToggle
    global otherToggle
    global addWeightField
    global inputStringField
    global acceptanceStates
    acceptanceToggle = cp5.getController('Acceptance State')
    Id_NumToggle = cp5.getController('ID/NUM')
    operatorToggle = cp5.getController('Operator')
    otherToggle = cp5.getController('Other')
    addWeightField = cp5.getController('Add Custom Weight')
    inputStringField = cp5.getController('Input String')
    background(51)
    mainGraph.show()
    showStartEdge()
    fill(255)
    textSize(20)

    text("Special Weights", 1400, 140)   


    addWeightClicked()
    inputStringClicked()
    

        
    
    


def mousePressed():
    if mouseX < 1300:
        mainGraph.listenForClicks()
        updateAcceptanceToggle()
        updateSpecialWeights()
    acceptanceToggleClicked()
    specialWeightsClicked()
    
    

                
    
def mouseDragged():
    mainGraph.listenForDrags()

        
        
        
def mouseReleased():
    mainGraph.listenForRelease()


def keyPressed():

    if (keyCode == SHIFT):
        return
    
    if((key == ENTER or key == RETURN)):
        getNewWeight()
        getInputString()
        
    if ((key == DELETE or key == BACKSPACE) and not( listenForNewWeight or listenForInputString)):
        mainGraph.deleteNode()
        mainGraph.deleteEdge()
        
    elif((key == 'n' or key == 'N') and not(listenForNewWeight or listenForInputString)):
        mainGraph.addNode()
        
def showStartEdge():
    stroke(0)
    startNode = mainGraph.startNode
    endPointX = startNode.x - startNode.size/2
    startPointx = endPointX - 50
    line(startPointx, startNode.y, endPointX, startNode.y)
    flank1 = PVector(15*cos(150*PI/180), 15*sin(150*PI/180))
    flankPointX = flank1.x + endPointX
    flankPointY = flank1.y + startNode.y
    line(endPointX, startNode.y, flankPointX, flankPointY)
    flank1 = PVector(15*cos(-150*PI/180), 15*sin(-150*PI/180))
    flankPointX = flank1.x + endPointX
    flankPointY = flank1.y + startNode.y
    line(endPointX, startNode.y, flankPointX, flankPointY)
    
def updateAcceptanceToggle():
    if mainGraph.selectedNode is None or mainGraph.selectedNode not in acceptanceStates:
        acceptanceToggle.setValue(False)
    elif mainGraph.selectedNode in acceptanceStates:
        acceptanceToggle.setValue(True)

def acceptanceToggleClicked():
    if mainGraph.selectedNode is None:
        return
    if acceptanceToggle.isMousePressed():
        if acceptanceToggle.getValue():
            acceptanceStates.append(mainGraph.selectedNode)
            mainGraph.selectedNode.defaultColor = (0,0,255)
            mainGraph.selectedNode.currentColor = (0,0,255)
        else:
            acceptanceStates.remove(mainGraph.selectedNode)
            mainGraph.selectedNode.defaultColor = (255,255,255)
            mainGraph.selectedNode.currentColor = (255,0,0)
    
def specialWeightsClicked():
    if mainGraph.selectedEdge is None:
        return
    if(Id_NumToggle.isMousePressed() or operatorToggle.isMousePressed() or otherToggle.isMousePressed()):
        weights = []
        if Id_NumToggle.getValue():
            weights.append("ID/NUM")
        if operatorToggle.getValue():
            weights.append("OPERATOR")
        if otherToggle.getValue():
            weights.append("OTHER")
        
        mainGraph.selectedEdge.weights = weights[:]
        
def updateSpecialWeights():
    if mainGraph.selectedEdge is None:
        Id_NumToggle.setValue(False)
        operatorToggle.setValue(False)
        otherToggle.setValue(False)
    else:
        edgeWeights = mainGraph.selectedEdge.weights
        if not edgeWeights :
            Id_NumToggle.setValue(False)
            operatorToggle.setValue(False)
            otherToggle.setValue(False)
            return
        if "ID/NUM" in edgeWeights:
            Id_NumToggle.setValue(True)
        if "OPERATOR" in edgeWeights:
            operatorToggle.setValue(True)
        if "OTHER" in edgeWeights:
            otherToggle.setValue(True)

def addWeightClicked():
    global listenForNewWeight
    if addWeightField.isFocus():
        listenForNewWeight = True
    else:
        listenForNewWeight = False

def getNewWeight():
    if not listenForNewWeight:
        return
    if(mainGraph.selectedEdge is None):
        addWeightField.setText('')
    else:
        newWeight = addWeightField.getText()
        oldWeights = mainGraph.selectedEdge.weights[:]
        oldWeights.append(newWeight)
        mainGraph.selectedEdge.weights = oldWeights
        addWeightField.setText('')

def inputStringClicked():
    global listenForInputString
    if (inputStringField.isFocus()):
        listenForInputString = True

    else:

        listenForInputString = False

def getInputString():
    if not listenForInputString:
        return
    inputString = inputStringField.getText()
    tokens = tokenizer.token(inputString)
    tokensString = functions.arrayToString(tokens) 
    outputField.setText(tokensString)   
    isAccepted = backend.matches(inputString)
    outputField.append(isAccepted+'\n')
    tokenSeq = errorfinder.sequence(tokens)
    outputField.append(tokenSeq + '\n')
    stateSeq = States.state(inputString)
    outputField.append(str(stateSeq))
    getEdges(stateSeq)

def getEdges(stateSequence):
    if not stateSequence:
        return
    edges = []
    for i in range(len(stateSequence)-1):
        firstNodeIndex = stateSequence[i] - 1
        secondNodeIndex = stateSequence[i+1] -1
        if(secondNodeIndex < 0):
            break
        try:
            firstNode = mainGraph.nodes[firstNodeIndex]
            secondNode = mainGraph.nodes[secondNodeIndex]
            connectingEdge = mainGraph.isConnected(firstNode, secondNode)
            if connectingEdge is None:
                break
            edges.append(connectingEdge)
        except:
            pass
         
    colorPath(edges)
        
def colorPath(edges, r=0, g=255, b=0):
    if not edges:
        return
    color = (r, g, b)
    for iedge in edges:
        iedge.node1.currentColor = color
        iedge.setColor(color)
        
    lastEdge = edges[-1]
    lastEdge.node2.currentColor = (235, 146, 52)