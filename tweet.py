import tweepy
import logging
import random
import credentials
import os
import constants
import pickle

consumer_key = credentials.API_key
consumer_secret_key = credentials.API_secret_key
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For adding logs in application
infoLogger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
infoLogger.setLevel(logging.INFO)


def textOnlyTweet(content):
    try:
        api.update_status(content + str(random.randint(0, 100)))
        infoLogger.info("Status update: text tweet")
    except:
        infoLogger.info("Error: update_status() failed")


def makeCaption():
    hashtags = random.sample(constants.hashtags, 2)
    caption = ""
    for h in hashtags:
        caption = caption + "#" + h + " "
    return caption


def imageTweet():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, "images")
    files = os.listdir(path)
    # fileName = random.choice(files)

    try:
        # no recent repeat mechanism
        with open(constants.queueFileName, "rb") as f:
            q = pickle.load(f)

        while 1:
            randImgName = random.choice(files)
            if randImgName in q:
                infoLogger.info("Image already in queue; retrying...")
            else:
                if len(q) >= constants.queueSize:
                    popped = q.pop(0)
                    q.append(randImgName)
                break

        with open(constants.queueFileName, "wb") as f:
            pickle.dump(q, f)

        imageName = "images/" + randImgName
        content = makeCaption()

        api.update_status_with_media(content, imageName)
        infoLogger.info("Media status update: image tweet")

    except:
        infoLogger.info("Error: update_status_with_media() failed")


if __name__ == "__main__":
    imageTweet()
