import re
import csv
import copy

path = "./test_file/第一集.md"
dest = "./test_file/第一集.csv"
headers = ['name', 'content']
rows = []

# 然后我发现要手动把NPC的话分出来！！NOO！！！！

with open(path, "r", encoding="utf8") as f:
    line = f.readline()
    row = []
    while line:
        
        line = line.replace(" ","") # 清空log中不必要的空格
        name = re.search(r"<([^<>]*)>", line)
        line = re.sub(r"<([^<>]*)>", '', line, count=1) # 正则识别名字和对话
        
        if(name != None): # 清空name中的<>符号
            name = name.group(0).strip("<").strip(">")
        else:
            name = "none"

        line = line.replace("\n","") # 清空句尾\n

        row.append(name)
        row.append(line)
        rows.append(copy.deepcopy(row))
        row.clear()
        line = f.readline()

with open(dest, 'w', encoding="utf8", newline="") as de:
    w_csv = csv.writer(de)
    w_csv.writerow(headers)
    w_csv.writerows(rows)
    rows.clear()