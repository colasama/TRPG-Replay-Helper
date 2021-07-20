from ttskit import sdk_api
import csv
import re
import os
import wav_splicer
from lrc_calc import LrcCalc

pair = {"骰子姬":1, "KP":12, "文明青年阿辽":3, "夏慎":22, "艺术家摸鱼":30, "刘深":20, "孙舞":9, "孙沁":4, "刘晓晓":16, "Ulire": 22}
path = "./test_file/第一集1.csv"
dest_lrc_name = "第一集1"

work_dir = "D:/code/TRPG-Replay-Helper/final/"

def text_synthesize(text, people, output):
    wav = sdk_api.tts_sdk(text, audio=people, output=output)

def seperate_str(string):
    result = re.findall(r"[\w']+", string)
    if(len(result)<=1):
        return string
    else:
        return result 

def main():
    lrc = LrcCalc()
    content_lrc = open(work_dir+dest_lrc_name+"Content.lrc", "w", encoding="utf8")
    people_lrc = open(work_dir+dest_lrc_name+"People.lrc", "w", encoding="utf8")
    total_wav_list = []

    with open(path, 'r', encoding="utf8") as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
        for row in csv_reader:
            content = seperate_str(row[1])

            # 确定一下保存文件的名字，去掉了不适合作为名字的内容
            file_name = str(row[1])
            file_name = re.findall(r'[^\*"/:?\\|<>]', file_name, re.S)
            file_name = "".join(file_name)
            # 文件不存在时，开始合成
            if(os.path.exists(work_dir+file_name+".wav") == False):
                if(type(content) == list):
                    name_list = []
                    for index, part in enumerate(content):
                        wav_path = work_dir+file_name+str(index)+".wav"
                        name_list.append(wav_path)
                        text_synthesize(part, pair[row[0]], wav_path)
                    wav_splicer.splice(name_list, work_dir+file_name+".wav")
                else:
                    text_synthesize(content, pair[row[0]], work_dir+file_name+".wav")
            
            # 保存文件名，用于下一步的合并为大wav
            total_wav_list.append(work_dir+file_name+".wav")
            # 这里保存一下lrc
            total_lrc = lrc.get_wave_lrc_time(work_dir+file_name+".wav", row[0])
            content_lrc.write(total_lrc[0]+"\n")
            people_lrc.write(total_lrc[1]+"\n")
    # 合并大wav，关闭两个lrc
    wav_splicer.splice(total_wav_list, work_dir+dest_lrc_name+".wav")
    content_lrc.close()
    people_lrc.close()

if __name__ == '__main__':
    main()
