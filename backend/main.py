from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pytz
import tweepy
import requests
import json
from datetime import datetime,timezone
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from authentication_module import getTwitterAuthInfo

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def twitterAuth():

    api_key = getTwitterAuthInfo("api_key")
    api_secret = getTwitterAuthInfo("api_secret")
    access_token = getTwitterAuthInfo("access_token")
    access_token_secret = getTwitterAuthInfo("access_token_secret")

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


def getUserTimeLine():
    api = twitterAuth()
    TWEET_COUNT = 10
    SEARCH_WORD = "#天国大魔境 -filter:retweets"
    user_tweet = tweepy.Cursor(api.search_tweets,q=SEARCH_WORD,tweet_mode='extended',include_entities=True,result_type='recent',lang='ja').items(TWEET_COUNT)
    return user_tweet


def change_time_JST(u_time):
    utc_time = datetime(u_time.year, u_time.month,u_time.day, \
    u_time.hour,u_time.minute,u_time.second, tzinfo=timezone.utc)
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    str_time = jst_time.strftime("%Y/%m/%d %H:%M")
    return str_time




@app.get("/")
def getTweetData():

    result = []
    
    user_tweet = getUserTimeLine()

    for tweet in user_tweet:

        dataTable = {}
        dataTable["id"] = tweet.id_str
        dataTable["name"] = tweet.user.screen_name
        dataTable["text"] = tweet.full_text
        dataTable["created_at"] = change_time_JST(tweet.created_at)
        dataTable["profile_image_url"] = tweet.user.profile_image_url
        if "media" in tweet.entities:
            for media in tweet.entities['media']:
                dataTable["media_url"] = media['media_url_https']
        result.append(dataTable)
      
        
    return {"TweetData":result}
