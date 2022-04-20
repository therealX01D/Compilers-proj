
import node
import edge




class DiGraph:
    """
    A class that descripes a Graph using a HashTable (dictionary in Python).
    The tabel is called "map". the table entry is a node and the output is a set of edges.
    this way all the data is available and can be derived.
    Example:
    suppose there is a node "n" that is already recognised by the graph.
    we can get the children of n using: map[n]
    this will return all the edges where node n is node1 inside the edge,
    now we can find the cost between a node and its child by getting the weight of the found edge.
    """

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.map = {}
        self.startNode = node.Node(50, 50)
        self.addNode(self.startNode)
        #variables to make the graph interactive
        self.selectedNode = None
        self.selectedEdge = None
        self.__tempNode = None
        self.__tempEdge = None
        self.__locked = False # draging nodes lock
        self.__drawingMode = False #drawing mode lock
        
        

    def addNode(self, newNode = None):
        """_summary_: 
        adds a node to the corner of the screen for later manipulation
        the node is added to array "self.nodes" so it can be recognized and 
        differentiated from other nodes outside the graph.
                      
        Args:
            node (_Node_, optional): you can provide a given node instead. Defaults to None.
        """        
        if newNode is None:
            newNode = node.Node(50, 50)
            
        self.map[newNode] = list()
        self.nodes.append(newNode)
        newNode.id = self.nodes.index(newNode)+1

        
    def __addEdge(self ,newEdge):
        """_summary_:
        adds an edge only if the end nodes of that edge are recognized 
        by the graph

        Args:
            edge (_Edge_): _description_
        """        
        if((newEdge.node1 in self.nodes) and (newEdge.node2 in self.nodes)):
            startNodeEdges = self.map[newEdge.node1]
            startNodeEdges.append(newEdge)
            self.edges.append(newEdge)
    
    def connect(self, node1, node2, weight = list()):
        """_summary_
        creates an edge between two nodes with an option to specify the weight

        Args:
            node1 (Node): _description_
            node2 (Node): _description_
            weight (Object, optional): _description_. Defaults to 0.
        """
        connectingEdge = edge.Edge(node1, node2)
        connectingEdge.weights = weight
        self.__addEdge(connectingEdge)
    
    def deleteNode(self):
        if self.selectedNode is None or self.selectedNode == self.startNode:
            return
        self.nodes.remove(self.selectedNode)
        deletedEdges = self.map.pop(self.selectedNode)
        for deletedEdge in deletedEdges:
                self.edges.remove(deletedEdge)
        groups = self.map.values()
        for group in groups:
            for iedge in group:
                if iedge.node2 == self.selectedNode:
                    group.remove(iedge)
                    self.edges.remove(iedge)
        self.selectedNode = None
        self.__updateNodesId()
                    
    def deleteEdge(self):
        if self.selectedEdge is None:
            return
        try:
            self.edges.remove(self.selectedEdge)
            startNode = self.selectedEdge.node1
            group = self.map[startNode]
            group.remove(self.selectedEdge)
            self.selectedEdge = None
        except:
            pass

    def isConnected(self, node1, node2):
        """_summary_
        check to see if two given nodes are connected

        Args:
            node1 (Node)
            node2 (Node)

        Returns:
            Boolean: True if found, otherwise false.
        """        
        nodeEdges = self.map[node1]
        for edge in nodeEdges:
            if(node2 == edge.node2):
                return True
        return False
    
    def adj(self, node):
        """_summary_
        returns a list of edges
        each edge include the end node, the cost to reach that node (weight)
        and the edge itself for further operations like coloring.
        this means we can deduce anything from the list of edges

        Args:
            node (Node): _description_

        Returns:
            List: list of Edges
        """        
        return self.map[node]
        
    def show(self):
        # draws the graph
        strokeWeight(1)
        for inode in self.nodes:
            inode.show()
            
        strokeWeight(3)
        for iedge in self.edges:
            iedge.show()
    
        if self.__tempEdge is not None:
            self.__tempEdge.show()
            
    def __updateNodesId(self):
        for inode in self.nodes:
            inode.id = self.nodes.index(inode)+1
        
#functions to make the graph interactive--------------------
    def __scanNodes(self):
        nodeFound = False
        for inode in self.nodes:
            if(inode.clicked()):
                self.selectedNode = inode
                nodeFound = True
                if(mouseButton == LEFT):
                    self.__locked = True
                else:
                    self.__drawingMode = True
                    self.__tempNode = node.Node(mouseX, mouseY)
                    self.__tempNode.size = 0
                    self.__tempEdge = edge.Edge(self.selectedNode, self.__tempNode)
        
        if not nodeFound:
            self.selectedNode = None
    
    def __scanEdges(self):
        found = False
        for iedge in self.edges:
            if(mouseButton == LEFT and iedge.clicked()):
                self.selectedEdge = iedge
                found = True
                break
                
        if not found :
            self.selectedEdge = None
        
    def listenForClicks(self):
        self.__scanNodes()
        self.__scanEdges()
        
    def listenForDrags(self):
        if(self.__locked):
            self.selectedNode.x = mouseX
            self.selectedNode.y = mouseY
        elif(self.__drawingMode):
            self.__tempNode = node.Node(mouseX, mouseY)
            self.__tempNode.size = 0
            self.__tempEdge.node2 = self.__tempNode
    
    def listenForRelease(self):
        
        if(self.__drawingMode):
            nodeFound = False
            for inode in self.nodes:
                if(inode.clicked()):
                    self.connect(self.selectedNode, inode)
                    nodeFound = True
                    
            if(not nodeFound):
                self.__tempEdge = None

        self.__locked = False
        self.__drawingMode = False
        self.__tempNode = None
        self.__tempEdge = None