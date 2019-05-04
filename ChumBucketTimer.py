
import ChumBucketSingleFeedAndTweet
import time
import datetime

for i in range(24):
    ChumBucketSingleFeedAndTweet.FeedAndTweet()

    now = str(datetime.datetime.now())
    message= "Hello Chum! Eat up! %s" % (now)

    print("Fed and Tweeted: %s %s %d" % (message, now, i+1))
    time.sleep(86400)#####MAKE THIS 86400 for 24 HOURS, 3600 for 1 hour
