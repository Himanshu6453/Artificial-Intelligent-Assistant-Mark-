import datetime
from Speak import Say

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def NonInputExecution(query):
    query = str(query)
    if 'time' in query:
        Time()
    elif 'date' in query:
        Date()
    elif 'sleep' in query:
        sleep()

def InputExecution(tag,query):
    if "wikipedia" in tag:
      try:
        name = str(query)
        name = name.replace("who", "").replace("about","").replace("is","").replace("what","").replace("tell","").replace("me","")
        #print(f"Query Searched on Wikipedia : {name}")
        import wikipedia
        result = wikipedia.summary(name,sentences = 2)
        Say(result)
      except:
          Say(f"No Records Found about {name}")

    if "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "").replace("find", "")
        import pywhatkit
        pywhatkit.search(query)