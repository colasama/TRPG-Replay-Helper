import re
def seperate_str(string):
	result = re.findall(r"[\w']+", string)
	final = []
	if(len(result)<=1):
		return string
	else:
		return result
input_psd = "kp隐瞒了什么，申请对kp心理学（不））"

def seperate_kp(ori):
	if(type(ori) == str):
		pass
	else:
		pass
print(seperate_str(input_psd), input_psd.split("kp"))