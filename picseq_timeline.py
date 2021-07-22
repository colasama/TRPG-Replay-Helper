import os

path = "./test_file/chara/"
chara = "夏慎"
png_list = {"夏慎00": 1.68}
emo = {0:"0-无表情", 1:"1-笑", 2:"2-开口", 3:"3-尴尬", 4:"4-生气", 5:"5-恐惧", 6:"6-沉思"}

# 从图片创建指定时长的带Alpha通道视频片段
def create_clip_from_pic(duration, chara, pic, output):
    full_path = path+chara+"/"+emo[int(pic)]+".png"
    print(full_path)
    total_frames = round(duration * 30)
    # ,fade=out:"+str(total_frames-3)+":3 也许不需要fadeout
    os.system(r"ffmpeg -f image2 -r 30 -loop 1 -i "+full_path+ \
              r" -vf fps=30,fade=in:0:4 -vcodec png "+"-t "+str(duration+0.3)+ \
              " "+output+".mov -y")
    return output+".mov"

# 合并clips，先手动了
def concat_clips(clips_list):
    for clip in clips_list:
        pass

print(emo[0])
