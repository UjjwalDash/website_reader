#Import Libriries
from newspaper import Article
import warnings
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
warnings.filterwarnings('ignore')
url=input("Enter Url of the website:")
article=Article(url)
article.download()
article.parse()
article.nlp()
corpus=article.text
print(corpus)
speak(corpus)
