from processing_data import process
from datagen import dataGen
import tweepy
import keys

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_key_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

def tweet(api, message, image_path):
    api.update_status_with_media(message, image_path)

if __name__ == "__main__":

    api = api()
    message = dataGen.messages()
    image_path = 'table.png'

    with open('success.txt') as f:
        success_prompt = f.read()

    process = process()
    try:
        from processed import data
        data_df = dataGen(data).generateTable()
        tweet(api, message, image_path)
        print(success_prompt)
    except Exception as e:
        print(e)
    
    

    



