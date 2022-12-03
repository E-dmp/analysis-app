from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tweepy
import requests
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
    
    # user_tweet = api.user_timeline(screen_name="yes_deknobou",include_rts=False,q=SEARCH_KEYWORD)
    # user_tweet = tweepy.Cursor(api.search_tweets, q='#天国大魔境' id="yes_deknobou")
    user_tweet = tweepy.Cursor(api.user_timeline,screen_name="",include_rts=False).items(TWEET_COUNT)
    # user_tweet = tweepy.Cursor(api.user_timeline, screen_name="rt1230909", q=SEARCH_KEYWORD).items(TWEET_COUNT)

    return user_tweet


@app.get("/")
def getTweetData():

    result = []
    user_tweet = getUserTimeLine()

    for tweet in user_tweet:
        if not "RT @" in tweet.text[0:4] and "#プログラミング" in tweet.text: 
            result.append(tweet.text)

    return {"TweetData":result}