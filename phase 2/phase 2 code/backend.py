from unicodedata import name
from numpy import NaN, true_divide
import itertools
import ParsingT
import tokenizer
import pandas as pd
class node:
    name=""
    adjacentlist=[]
    attr=[]
    def __init__(self,name):
        self.name=name
        self.adjacentlist=[]
        self.attr=[]
        self.x = 0
        self.y = 0
        self.radius = 0
        self.angle = 0
    def add2adjacentlist(self,node):
        self.adjacentlist.append(node)
    def updateattr(self,attr):
        self.attr.append(attr)

class tree:
    listofnodes=[]
    root=0
    def __init__(self,listofnodes):
        self.listofnodes=listofnodes
    def getnode(self,str):
        return self.listofnodes[str]
    def getedgelist(self):
        edgelist=[]
        for i in range(len(self.listofnodes)):
            for j in range(len(self.listofnodes[i].adjacentlist)):
                edgelist.append((self.listofnodes[i].name,(self.listofnodes[i].adjacentlist)[j]))
        return edgelist


def checkinput(inputstring):
    intokenlist=tokenizer.token(inputstring)
    intokenlist.append("$")
    intokenlist.reverse()  
    currstate="EXP"
    nextstate=None
    currstatenode=node(currstate)
    decforprevnodes={"EXP":currstatenode,"EXP'":NaN,"TERM":NaN, "TERM'":NaN,"FACTOR":NaN,"FACTOR'":NaN,"COMPOP":NaN,"OPERAND":NaN,"id":NaN}
    occurancesofprevnodes={"EXP":999999,"EXP'":0,"TERM":0, "TERM'":0,"FACTOR":0,"FACTOR'":0,"COMPOP":0,"OPERAND":0,"id":0,"<":0,"||":0,">":0,"!":0,"&&":0,"=":0}
    listforptree=[]
    listforast=[]
    currast="$"
    level=1
    statelist=["$","EXP"]
    while True:

        if len(statelist)==1 and len(intokenlist)==1 and statelist[0]=="$" and intokenlist[0]=="$" :
            print("--------------------------------------------------")
            for i in range(len(listforptree)):
                 print(f"{listforptree[i].name} => {listforptree[i].adjacentlist}")
            print("--------------------------------------------------")
            retree=tree(listforptree)
            return "accepted",retree,listforast
        tupeoftokenizer=intokenlist[-1]
        typeofstart=tupeoftokenizer[0]
        currstate=statelist.pop()
        currstatenode=node(currstate) if  occurancesofprevnodes[currstate]<0 else decforprevnodes[currstate]
        if currstate==typeofstart:
            if(currstate=="id"):
                level=4
                currstatenode.add2adjacentlist(node(tupeoftokenizer[1]))
                #currstatenode.attr.append(tupeoftokenizer[1])
                listforptree.append(currstatenode)
            elif currstate=="<" or currstate==">" or currstate=="=" :
                level=3
            elif currstate=="&&":
                level=2
            elif currstate=="||":
                level=1 
            currstatenode.attr.append(tupeoftokenizer[1])
            listforast.append({currstate:level})
            intokenlist.pop()
            print(intokenlist)
            print(statelist)
            continue
        #print(typeofstart)
        nextstate=ParsingT.ruletranslation(ParsingT.parsingTable(currstate,typeofstart))
        if nextstate=="EPI":
             currstatenode.add2adjacentlist(node("EPI"))
             listforptree.append(currstatenode)
             print(statelist)
             continue
        if nextstate==-1:
             print(currstate)
             return "refused",tree([]),tree([])
        templist=nextstate.split(" ")
        templist.reverse()
        for i in range(len(templist)):
            statelist.append(templist[i])
        level+=1
        templist.reverse()
        for i in range(len(templist)):
            decforprevnodes[templist[i]]=node(templist[i])
            occurancesofprevnodes[templist[i]]+=1
            if(not templist[i] == "EPI"):
                currstatenode.attr.append(decforprevnodes[templist[i]].attr)    
            currstatenode.add2adjacentlist(decforprevnodes[templist[i]])
        occurancesofprevnodes[currstate]-=1
        templist.reverse()
        listforptree.append(currstatenode)
        print(statelist)
        print(intokenlist)
 

state,restree,asttree = checkinput("x2<y1")
root=restree.listofnodes[0]
print(root.attr)

for i in range(len(restree.listofnodes)):
    print(f"tree root ")
    for j in range(len(restree.listofnodes[i].adjacentlist)):
        print(f"{str(i)}=>{restree.listofnodes[i]}:{restree.listofnodes[i].name}=>{restree.listofnodes[i].adjacentlist[j].name}:{restree.listofnodes[i].adjacentlist[j]}")
print(asttree)
