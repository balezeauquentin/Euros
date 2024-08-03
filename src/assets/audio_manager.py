import pyaudio
import speech_recognition as sr


record = sr.Recognizer()

# print("Available microphones:")
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f"{index}: {name}")

device_index = 2

with sr.Microphone(device_index=device_index) as source:
    print("Adjusting for ambient noise...")
    record.adjust_for_ambient_noise(source)
    print("Speak!")
    audio_data = record.listen(source)
    print("End!")
try:
    text = record.recognize_google(audio_data, language="fr-FR") # type: ignore
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
