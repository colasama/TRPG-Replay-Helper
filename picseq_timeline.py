import os
from PIL import Image

path = "./test_file/chara/"
chara = "夏慎"
png_list = {"夏慎00": 1.68}

def create_clip_from_pic(duration, pic, output):
    full_path = path+chara+"/"+pic+".png"
    img = Image.open(full_path)
    width = img.width
    height = img.height

    # os.system(r"ffmpeg -r 30 -loop 1 -i " + full_path +" -pix_fmt yuv420p -vcodec \
    #             libx264 -b:v 600k -r:v 30 -preset medium -crf 30 -s "+str(width)+"x"+str(height)+ \
    #             " -vframes 250 -r 25 -t "+str(duration)+" "+output+".mp4")
    total_frames = round(duration * 30)
    os.system(r"ffmpeg -f image2 -r 30 -loop 1 -i "+full_path+ \
              r" -vf fps=30 -vf fade=in:0:6,fade=out:"+str(total_frames-6)+":6 -vcodec qtrle "+"-t "+str(duration)+ \
              " "+output+".mov -y")
create_clip_from_pic(3, "夏慎00", "./test_file/mov_tmp/b")