from ttskit import sdk_api

def text_synthesize(text, i):
    path = str(i) + ".wav"
    wav = sdk_api.tts_sdk(text, audio=i, output=path)
    
def main():

    text_synthesize("欸 请问您是" ,2)
    

if __name__ == '__main__':
    main()
