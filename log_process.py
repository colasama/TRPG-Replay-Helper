import re

def seperate_str(string):
    result = re.findall(r"[\w']+", string)
    if(len(result)<=1):
        return string
    else:
        return result 

print(type(seperate_str("assfdghfdgfdg")) == str)