import tweepy
import credentials

# Authenticate to Twitter
auth = tweepy.OAuthHandler(credentials.API_key, credentials.API_secret_key)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")
