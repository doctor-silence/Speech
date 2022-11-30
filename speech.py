import speech_recognition as sr


mic = sr.Microphone(device_index=2)
#list_mic = sr.Microphone.list_microphone_names()
#for i in range(0, len(list_mic)):
#    print(i, list_mic[i])

# obtain audio from the microphone
r = sr.Recognizer()
with mic as source:
    print('Говорите число А!')
    audio = r.listen(source)

try:
    a = r.recognize_google(audio, language='ru-RU')
    print("Google Speech Recognition thinks you said " + a)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


with mic as source:
    print('Говорите число B!')
    audio = r.listen(source)

try:
    b = r.recognize_google(audio, language='ru-RU')
    print("Google Speech Recognition thinks you said " + b)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print('A+B=', (int(a)+int(b)))