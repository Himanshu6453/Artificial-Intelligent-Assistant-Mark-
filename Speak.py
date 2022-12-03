import pyttsx3

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id )   # Ravi 1 , David - 2  , zira - 3 , hetal - 0
#print(voices[1])
engine.setProperty('rate', 170)


def Say(Text):
    print("  ")
    print(f" Mark_IV  : {Text}")
    engine.say(Text)
    engine.runAndWait()
    print("  ")

