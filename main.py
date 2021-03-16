    # pip install gTTS
    from gtts import gTTS
    import os
    
    #Istalgan tekt kiritishingiz mumkin
    text = 'Hello world!'
    
    #Modulni ishlatish
    tts = gTTS(text=text, lang='en', slow='False')
    
    #yozilgan ovozni faylga saqlash
    tts.save('DeCoder.mp3')
    
    #dastur ishlab turgan holatda faylni ochish
    os.system("DeCoder.mp3")