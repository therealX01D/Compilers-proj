def sequence(tokenlist):
    tokenclass=[]
    for token in tokenlist:
        tokenclass.append(token[0])
    
    stri="=>".join(tokenclass)
    # print(stri)
    return stri