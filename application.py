from flask import Flask
import tweet
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import constants

application = Flask(__name__)


@application.route("/")
def index():
    return "Follow @daily_dianxia on Twitter!"


def job():
    tweet.imageTweet()


scheduler = BackgroundScheduler()
# scheduler.add_job(func=job)
scheduler.add_job(func=job, trigger="interval", seconds=constants.sixHours)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=5000, debug=True)
