import pandas as pd
terminal_expr=['!','&&','||','<','>','=','id','$']
#exp=>E exp'=>N term=>T term'=>N  Factor=>F Factor'=>M COMPOP=>C OPERAND=>O Z=>endstate badl (epi) 
nonterminal_expr=['E','N','T','W','F','M','C','O']
DF = pd.DataFrame(index=["EXP", "EXP'", "TERM", "TERM'", "FACTOR", "FACTOR'", "COMPOP", "OPERAND"],columns=["!", "&&", "||", "<", "=",">", "id", "$"])
DF["!"]["EXP"] = 1
DF["id"]["EXP"] = 1
#######
DF["$"]["EXP'"] = 3
DF["||"]["EXP'"] = 2
#######
DF["!"]["TERM"] = 4
DF["id"]["TERM"] = 4
#######
DF["&&"]["TERM'"] = 5
DF["||"]["TERM'"] = 6
DF["$"]["TERM'"] = 6
#######
DF["!"]["FACTOR"] = 7
DF["id"]["FACTOR"] = 7
########
DF["&&"]["FACTOR'"] = 9
DF["||"]["FACTOR'"] = 9
DF["<"]["FACTOR'"] = 8
DF["="]["FACTOR'"] = 8
DF[">"]["FACTOR'"] = 8
DF["$"]["FACTOR'"] = 9
#######
DF["<"]["COMPOP"] = 12
DF["="]["COMPOP"] = 11
DF[">"]["COMPOP"] = 10
###############
DF["!"]["OPERAND"] = 13
DF["id"]["OPERAND"] = 14
print(DF)
print(DF["&&"]["OPERAND"])

def ruletranslation(num):
    arr=[0,"TERM EXP'","|| TERM EXP'","EPI","FACTOR TERM'","&& FACTOR TERM'","EPI","OPERAND FACTOR'","COMPOP OPERAND FACTOR'","EPI",">","=","<","! OPERAND","id"]
    return -1 if pd.isna(num) else arr[num]
for i in range (1,15):
    print(i,ruletranslation(i))
def parsingTable(row,col):
    return DF[col][row]

print(ruletranslation(DF["&&"]["OPERAND"]))


