from pyvis.network import Network
from tokenizer import token
def isIDe(elem) :
    tokenli=token(elem)
    return tokenli[0][0]=="id"
def generateAST(list):
    # base cases
    if len(list) == 1 and isIDe(list[0]):
        return list
    # recursion
    if '||' in list:
        x = len(list) - list[::-1].index("||") - 1
        first = list[:x]
        second = list[x + 1:]
        firstReady = generateAST(first)
        secondReady = generateAST(second)
        return '||', firstReady, secondReady
    elif '&&' in list:
        x = len(list) - list[::-1].index("&&") - 1
        first = list[:x]
        second = list[x + 1:]
        firstReady = generateAST(first)
        secondReady = generateAST(second)
        return '&&', firstReady, secondReady
    elif '<' in list or '>' in list or '=' in list:
        for x in list[::-1]:
            if x == '<' or x == '>' or x == '=':
                index = len(list) - list[::-1].index(x) - 1
                first = list[:index]
                second = list[index + 1:]
                firstReady = generateAST(first)
                secondReady = generateAST(second)
                return x, firstReady, secondReady
    elif list[0] == '!':
        after = generateAST(list[1:])
        return '!', after


def drawAST(inputstring, filename):
   
    Tree = Network(height='650px', width='730px', directed=False)
    nodesli = []
    Tree = drawRecursive(0, -100, Tree, nodesli, inputstring)
    print(nodesli)
    for n in Tree.nodes:
        n.update({'physics': False})
    Tree.show(filename)


def drawRecursive(x_coor, y_coor, head, dictionary, node, parent=None):
    x = len(dictionary)
    head.add_node(n_id=x + 1, x=x_coor, y=y_coor, label=node[0])
    if len(node) == 1:
        print(node)     
        if parent is not None:
            head.add_edge(parent, x + 1)
        dictionary.append((node[0], x + 1))
        return head
    if parent is not None:
        head.add_edge(parent, x + 1)
    dictionary.append((node[0], x + 1))
    # adding the children
    if len(node) == 3:
        # left branch
        head = drawRecursive(x_coor - 100, y_coor + 100, head, dictionary, node[1], x + 1)
        # right branch
        head = drawRecursive(x_coor + 100, y_coor + 100, head, dictionary, node[2], x + 1)
        return head
    elif len(node) == 2:
        head = drawRecursive(x_coor, y_coor + 100, head, dictionary, node[1], x + 1)
        return head
def astdrawal(list):
    tokenlist=token(list)
    for i in range(len(tokenlist)):
        tokenlist[i]=tokenlist[i][1]
    x = generateAST(tokenlist)
    print(x)
    drawAST(x, '1.html')
