import graph
class PathFinder:
    def __init__(self, diGraph, inputString):
        self.diGraph = diGraph
        self.startNode = diGraph.startNode
        self.inputString = inputString
        self.currentNode = self.startNode
        self.currentIndex = 0
        self.edges = None
        self.currentChar = None
        self.loadingString = ''
        self.matchingMessage = ''
    def traverse(self):
        if self.currentIndex >= len(self.inputString):
            if self.currentNode in self.diGraph.acceptanceStates:
                self.matchingMessage = "The String is Accepted!"
            else:
                self.matchingMessage = "The String is not Accepted!"
            return
        self.currentChar = self.inputString[self.currentIndex]
        if self.currentChar == ' ':
            self.currentIndex += 1
            self.loadingString += self.currentChar
            if self.currentIndex < len(self.inputString):
                self.currentChar = self.inputString[self.currentIndex]

        if self.__lookForChar():
            return
        if self.__lookForLetter():
            return
        if self.__lookForDigit():
            return
        if self.__lookForOther():
            return
        self.currentNode.currentColor = (255, 255, 0)
        self.matchingMessage = 'Stuck at Node ' + str(self.currentNode.id)
                
    def __lookForChar(self):
        self.edges = self.diGraph.adj(self.currentNode)
        for edge in self.edges:
            if self.currentChar in edge.weights:
                edge.traverse()
                self.currentNode = edge.node2
                self.currentIndex += 1
                self.loadingString += self.currentChar
                return True
        return False
    
    def __lookForLetter(self):
        self.edges = self.diGraph.adj(self.currentNode)
        for edge in self.edges:
            if self.currentChar.isalpha() and "LETTER" in edge.weights:
                edge.traverse()
                self.currentNode = edge.node2
                self.currentIndex += 1
                self.loadingString += self.currentChar
                return True
        return False
    
    def __lookForDigit(self):
        self.edges = self.diGraph.adj(self.currentNode)
        for edge in self.edges:
            if self.currentChar.isdigit() and "DIGIT" in edge.weights:
                edge.traverse()
                self.currentNode = edge.node2
                self.currentIndex += 1
                self.loadingString += self.currentChar
                return True
        return False
    
    def __lookForOther(self):
        self.edges = self.diGraph.adj(self.currentNode)
        for edge in self.edges:
            if  "OTHER" in edge.weights:
                edge.traverse()
                self.currentNode = edge.node2
                self.currentIndex += 1
                self.loadingString += self.currentChar
                return True
        return False
    
    def show(self):
        textSize(36)
        textAlign(LEFT)
        fill(255)
        text(self.inputString, 100, 850)
        fill(0,255,0)
        text(self.loadingString, 100, 850)
        
        textSize(26)
        fill(255)
        text(self.matchingMessage, 100, 880)
        