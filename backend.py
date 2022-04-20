import re
import tokenizer
import stringmatching
import errorfinder
x=input("Enter string : ")
tokenlist=tokenizer.token(x)
print(tokenlist)
retstring=errorfinder.sequence(tokenlist)
if(re.match('.*NUM=>ID.*',retstring)):
    print(False)
else:
    print(stringmatching.stringmatches(x))
