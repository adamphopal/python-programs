import os

#go to nano .bash_profile to see all of your exports environment variables

en_one = os.environ.get('ONE')
en_c = os.environ.get('HOME')
email_send = os.environ.get('EMAIL_SEND')
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
translate_api = os.environ.get('TRANSLATE_API')
lyrics_key = os.environ.get('LYRICS_API')
geo_api = os.environ.get('GEOCODE_API')

print(email_send)
print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)
print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)
print(translate_api)
print(lyrics_key )
print(geo_api)

