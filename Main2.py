import tweepy

TWITTER_CLIENT = 
TWITTER_SECRET = 
TWITTER_ACCESS = 
TWITTER_ACCESS_SECRET = 

auth = tweepy.OAuthHandler(TWITTER_CLIENT, TWITTER_SECRET)

auth.set_access_token(TWITTER_ACCESS, TWITTER_ACCESS_SECRET)

api = tweepy.API(auth)

api.update_status("Hello, world!!!!")
