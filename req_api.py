#Python Requests Beginner Tutorial - GET Requests With Translate API
#Python Requests library to you by talking about how to perform GET requests to a language translation API
#Yandex Translate API: https://tech.yandex.com/translate/
#https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages
import requests


API_KEY = os.environ.get('TRANSLATE_API')
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

words = input("Enter text to store:" )
#translate the quran into english, just copy from a website, then translate
params = dict(key=API_KEY, text=words, lang='en-ar') #translates text from arabic to englist
r = requests.get(url, params=params)
json = r.json()
print(json['text'][0])

#print(r.text)
