from pydub import AudioSegment
import os


# AudioSegment.converter = "D:\\Program Files (x86)\\ffmpeg-4.1-win64-static\\bin\\ffmpeg.exe"

# wav 格式语音文件合成
def splice(voice_list, output_name):
    try:
        n=0
        #list_voice_dir_length = len(list_voice_dir)
        playlist = AudioSegment.empty()
        second_3_silence = AudioSegment.silent(duration=300)  #产生一个持续时间为300ms的无声AudioSegment对象
        for i in voice_list:
            sound = AudioSegment.from_file(voice_list[n],format="wav") #  wav
            playlist = playlist + sound + second_3_silence
            n+=1
            
        playlist.export(output_name,format="wav") #wav

        for i in voice_list:
            os.remove(i)
    except:
        print("wavespicing error in "+ output_name)

# 总的合成
def final_splice(voice_list, output_name):
    try:
        n=0
        #list_voice_dir_length = len(list_voice_dir)
        playlist = AudioSegment.empty()
        second_3_silence = AudioSegment.silent(duration=300)  #产生一个持续时间为300ms的无声AudioSegment对象
        for i in voice_list:
            sound = AudioSegment.from_file(voice_list[n],format="wav") #  wav
            playlist = playlist + sound + second_3_silence
            n+=1
            
        playlist.export(output_name,format="wav") #wav

    except:
        print("wavespicing error in "+ output_name)

def get_none(durat, output_name):
    playlist = AudioSegment.empty()
    playlist += AudioSegment.silent(duration=durat)
    playlist.export(output_name,format="wav")

get_none(300, "D:/a.wav")