from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tweepy
import requests
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from authentication_module import get_authentication_info

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

    api_key = get_authentication_info("api_key")
    api_secret = get_authentication_info("api_secret")
    access_token = get_authentication_info("access_token")
    access_token_secret = get_authentication_info("access_token_secret")

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


def getUserTimeLine():

    api = twitterAuth()
    user_tweet = api.user_timeline(screen_name="",include_rts=False)

    return user_tweet


@app.get("/")
def getTweetData():

    result = []
    user_tweet = getUserTimeLine()

    for tweet in user_tweet:
        result.append(tweet.text)

    return {"TweetData":result}