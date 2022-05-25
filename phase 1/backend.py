import re
import tokenizer
import stringmatching
import errorfinder
#x=input("Enter string : ")
def matches(x):
    y=x.replace(" ", "")
    # print(y)
    tokenlist=tokenizer.token(y)
    # print(tokenlist)
    retstring=errorfinder.sequence(tokenlist)
    if(re.match('.*NUM=>ID.*',retstring)):
        return "refused"
    else:
        return "Accepted" if (stringmatching.stringmatches(y)==True)  else "Refused"
#print(matches(x))
