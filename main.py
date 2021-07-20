from lrc_calc import LrcCalc
import tts
import os  

wav_list = []

def get_filelist(path, list_name):  
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.splitext(file_path)[1]=='.wav':
            list_name.append(file_path)

def main():
    get_filelist('./test_file', wav_list)
    lrc = LrcCalc()

    for file in wav_list:
        print(lrc.get_wave_lrc_time(file))
    
if __name__ == '__main__':
    main()



    