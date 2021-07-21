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
print("聘请" in "周老师聘请这样一个健忘到把事件写在笔记本上的人是有毛病吗")