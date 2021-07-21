import re
input_psd = "你说啥子?"
test_str = re.search(r"`~!@#$%^&*()_\-+=<>?:{}|,.\/;'\[\]·~！@#￥%……&*（）——\-+={}|《》？：“”【】、；‘'，。、",input_psd)
if test_str == None:
	print("没有没有真没有特殊字符")
else:
	print("该文本包含特殊字符")