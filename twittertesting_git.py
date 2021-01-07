import tweepy
import time

# Github version without personal keys, using placeholders
auth = tweepy.OAuthHandler("CONSUMER_KEY_HERE", "CONSUMER_SECRET_KEY_HERE")
auth.set_access_token("CONSUMER_KEY_HERE", "CONSUMER_SECRET_KEY_HERE")

api = tweepy.API(auth)

# public_tweets = api.home_timeline() #prints tweets on the timeline
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

def limit_handle(cursor): #this is just to compensate for twitter's built in rate limit
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(2)

# # Bot that will follow back all followers
# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     print(f"{follower.name} has been followed")


# # Bot that will like the first numberOfTweets tweets with keyword search_str
# search_str = 'HoloEn'
# numbersOfTweets = 5
#
# for tweet in limit_handle(tweepy.Cursor(api.search, search_str).items(numbersOfTweets)):
#     try:
#         tweet.favorite()
#         print(f"Liked the tweet {tweet}")
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

