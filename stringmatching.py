
import re                                 # for performing regex expressions
tokens = []                               # for string tokens
source_code = 'intresult= 100;'.split() # turning source code into list of words
inputregex ="542154||!!!!!!!!!8xht8TT99gr<=55154||ysgdd>=45547474&&ysgdd<45547474&&ysgdd>45547474"
# Loop through each source code word
def stringmatches(inputregex):
    inputregexlist=re.split(r'[|]{2}|&&',inputregex)
    #inputregex.split("||") if "||"in inputregex else inputregex.split("&&") if "&&" in inputregex else inputregex
    regexfortext=r'([!]*((((([a-z]([a-zA-Z0-9]*)))|[A-Z]([a-zA-Z0-9]*))[a-zA-Z0-9]))|[!]*[a-zA-Z0-9])'
    #([!]*((([a-z]([a-zA-Z0-9]*)|[A-Z]([a-zA-Z0-9]*))[a-zA-Z0-9]))|[a-z])'
    compregexfortext=re.compile(regexfortext)
    regexfornumbers=r'([!]*((-){0,1}[0-9]+))'
    # #
    regexforillegalnumbers=r'~([0-9]+(~[0-9]+))'
    #[0-9][0-9]+
    compregexforno=re.compile(regexfornumbers)
    regexfortextornumbers=r'({}|{})'.format(regexfortext,regexfornumbers)
    regexforcompop=r'(>|<|<=|>=|=|[|]{2}|[&]{2})'

    regexfororsands=r'([|]{2}|&&)'# x < 4 x>=4 
    regexforsinglecomparison=r'^{}{}{}$|^{}$'.format(regexfortextornumbers,regexforcompop,regexfortextornumbers,regexfortextornumbers)
    n=1
    regexrun=re.compile(regexforsinglecomparison)
    for onestr in inputregexlist:
        retextno = re.compile(regexfortextornumbers)
        if not(regexrun.match(onestr)):
            print(onestr+"not in comp")
            #print("No matches")
            return False
        elif (retextno.match(onestr)) and (len(inputregexlist)==1) and not(regexrun.match(onestr)):
            return False
        else:
            n+=1
                   #print("matches")
    return True
    #print(inputregexlist)
    #return 
    print(tokens) # Outputs the token array
#class backend():
 #   def __init__(self,inputstr):
 #       self.inputstr=inputstr
 #       self.tokens=[]
 #   def tokenize(self):
