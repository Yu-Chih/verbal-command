import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    # print(sr.Microphone.list_microphone_names())
    print("Adjusting for background noise. One second")
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError as e:
        print("failed; {0}" .format(e))
        