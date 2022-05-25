import node
import functions
import curve
class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.weights = []
        self.curve = curve.Curve(self.node1, self.node2)
        self.id = 0
        
        
    def show(self):
        self.curve.node2 = self.node2
        self.curve.show()
        self.curve.showWeight(self.weights)
    
    def addWeight(self,weight):
        self.weights.append(weight)
    
    def clicked(self):
        return self.curve.clicked()
    
    def setColor(self, color):
        self.curve.currentColor = color
    

    

        
