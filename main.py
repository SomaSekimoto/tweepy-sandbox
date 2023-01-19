import os
import tweepy
import pytz
import datetime
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
jptz = pytz.timezone('Asia/Tokyo')

def fetch_replied_users(tweet_id):
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # API v2.0使う時は↓
    # api = tweepy.Client(
    #     consumer_key=consumer_key,
    #     consumer_secret=consumer_secret,
    #     access_token=access_token,
    #     access_token_secret=access_token_secret,
    #     bearer_token=bearer_token
    # )

    mentions = api.mentions_timeline(since_id=tweet_id)
    # replies = tweepy.Cursor(api.mentions_timeline,  since_id=tweet_id).items(20)
    
    mn_users = []
    
    for mn in mentions:
        print('reply')
        print(mn)
        mn_users.append("@" + mn.user.screen_name)
    print(mn_users)

    # print("len(mentions)")
    # print(len(list(mentions)))



if __name__ == "__main__":
    # Authするときに使うアクセストークンを発行したユーザーのツイートじゃないとリプライが取得できなかった。
    tweet_id = 1577575472120336384
    fetch_replied_users(tweet_id)