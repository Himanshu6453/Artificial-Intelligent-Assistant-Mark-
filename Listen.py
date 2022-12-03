import speech_recognition as sr     #pip install speechrecognition

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mark_IV Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Mark_IV Recognizing..")
            query = r.recognize_google(audio , language="en-in")
            print(f"You said : {query}")

        except :
            return ""
        query = str(query)
        return query.lower()

