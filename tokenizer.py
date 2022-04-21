#x="!xhttgr<=55154||!ysGdd>=45547474&&||ysgdd<45547474&&ysgdd>dgsgsda"
def token(x):
    tokens = []
    x+="_"
    xsize=len(x)
    i=0
    while(i<xsize):
        if (x[i]>='a' and x[i]<='z') or (x[i]>='A' and x[i]<='Z'):
            t=""
            while(i<xsize):
                if (x[i]>='a' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')or(x[i]>=str(0) and x[i]<=str(9)) or (x[i]>=str(0) and x[i]<=str(9)):
                    t+=x[i]
                    i+=1
                else:
                    tokens.append(['ID',t])
                    break
        elif (x[i]>=str(0) and x[i]<=str(9)):
            t=""
            while(i<xsize):
                if (x[i]>=str(0) and x[i]<=str(9)):
                    t+=str(x[i])
                    i+=1
                else:
                    tokens.append(['NUM',t])
                    break
        elif (x[i]== '&' and x[i+1]=='&') :
                tokens.append(['and','&&'])
                i+=2
        elif (x[i]== '|' and x[i+1]=='|') :
                tokens.append(['or','||'])
                i+=2
        elif (x[i]== '!') :
                tokens.append(['not','!'])
                i+=1
        elif (x[i]== '=') :
                tokens.append(['equal','='])
                i+=1
        elif (x[i]== '<') :
            if (x[i+1]=='='):
                i+=2
                tokens.append(['smallerorequal','<='])
            else:
                i+=1
                tokens.append(['smaller','<'])
        elif (x[i]== '>') :
            if (x[i+1]=='='):
                tokens.append(['biggerorequal','>='])
                i+=2
            else:
                i+=1
                tokens.append(['bigger','>'])
        else:
            i+=1
    #print(str(i))
    tokenlistupd=[]
    # for i in tokens:
    #     print(i)
    return tokens
    #return tokens
    #print(tokens)