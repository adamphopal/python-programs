import requests
import json
from lyrics_api import *

# example call: base_url + lyrics_matcher + format_url + artist_search_parameter + artist_variable + track_search_parameter + track_variable + api_key
# example json print: print(json.dumps(api_call, sort_keys=True, indent=2))

while True:
    print()
    print("Welcome to the Musixmatch API explorer!")
    print()
    print("MENU OPTIONS")
    print("1 - Call one of the API methods with parameters and see JSON")
    print("2 - EXAMPLE: Search for the lyrics of a song")
    print("0 - Exit")
    print()
    choice = input("> ")
    print()

    if choice == "0":
        break

    # see the paramaters for an api method
    if choice == "1":
        print("API METHODS")
        for index, api_method in enumerate(api_methods, start = 0):
            print(str(index) + ": " + api_method)
        print()
        print("Your choice (0 - 15)")
        method_choice = input("> ")
        print()
        user_choice = api_methods[int(method_choice)]
        parameter_list = get_parameters(user_choice)

        print("PARAMATERS")
        for index, parameter in enumerate(parameter_list, start = 0):
            print(str(index) + ": " + parameter)
        print()

        # start building the api call
        api_call = base_url + user_choice + format_url

        while True:
            print("API call so far: " + api_call)
            print()
            print("Which parameter would you like to add a value for? (0-n) (type x to make the call)")
            parameter_choice = input("> ")
            print()

            # add the api key and make the call
            if parameter_choice == "x":
                api_call = api_call + api_key
                request = requests.get(api_call)
                data = request.json()
                print("Final API Call: " + api_call)
                print()
                print("JSON DATA")
                print(json.dumps(data, sort_keys=True, indent=2))
                break

            # add a parameter
            else:
                parameter_choice_string = parameter_list[int(parameter_choice)]
                value = input(parameter_choice_string)
                api_call = api_call + parameter_choice_string + value
                print()

    # example
    if choice == "2":
        print("Whats's the name of the artist?")
        artist_name = input("> ")
        print("What's the name of the track?")
        track_name = input("> ")
        print()
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']
        print("API Call: " + api_call)
        print()
        print(data['lyrics']['lyrics_body'])

    # check if the user wants to go again
    print()
    print("Again? (y/n)")
    again = input("> ")
    if again == "n":
        break



#Hacking through Google's Text to Speech API

API_ENDPOINT = "https://translate.google.com/translate_tts"

headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}

#text to save as mp3



text = input("Enter text to store:" )


params = {
    'ie': 'UTF-8',
    'q': text,
    'tl': 'hi',
    'client': 'gtx'
}

#en
#hi

r = requests.get(API_ENDPOINT, params = params, headers = headers)

print(r.status_code)

#name of file that will save voice of given input text
file_name = input("Enter file name to store audio translated from text, needs mp3 at end:" )
with open(file_name, 'wb') as f:
    f.write(r.content)


#lanuages that can be tanslated from text into voice mp3 file
'''
Supported languages:
LANG_MAP = {'swahili': 'sw', 'russian': 'ru', 'ukrainian': 'uk', 'macedonian': 'mk', 'kannada': 'kn', 'hebrew': 'iw', 'chinese simplified': 'zh-CN', 'latvian': 'lv', 'icelandic': 'is', 'hungarian': 'hu', 'czech': 'cs', 'turkish': 'tr', 'esperanto': 'eo', 'irish': 'ga', 'danish': 'da', 'german': 'de', 'bulgarian': 'bg', 'basque': 'eu', 'filipino': 'tl', 'maltese': 'mt', 'thai': 'th', 'haitian creole': 'ht', 'english': 'en', 'galician': 'gl', 'chinese traditional': 'zh-TW', 'yiddish': 'yi', 'polish': 'pl', 'vietnamese': 'vi', 'belarusian': 'be', 'portuguese': 'pt', 'welsh': 'cy', 'croatian': 'hr', 'korean': 'ko', 'bengali': 'bn', 'urdu': 'ur', 'slovak': 'sk', 'azerbaijani': 'az', 'georgian': 'ka', 'afrikaans': 'af', 'norwegian': 'no', 'telugu': 'te', 'lithuanian': 'lt', 'persian': 'fa', 'estonian': 'et', 'gujarati': 'gu', 'hindi': 'hi', 'albanian': 'sq', 'tamil': 'ta', 'indonesian': 'id', 'serbian': 'sr', 'swedish': 'sv', 'french': 'fr', 'malay': 'ms', 'spanish': 'es', 'dutch': 'nl', 'italian': 'it', 'finnish': 'fi', 'arabic': 'ar', 'slovenian': 'sl', 'latin': 'la', 'japanese': 'ja', 'catalan': 'ca', 'greek': 'el', 'romanian': 'ro'}
'''

