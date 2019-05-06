


import ChumBucketSingleFeedAndTweetNoPhoto
import time
import datetime

for i in range(24):
    ChumBucketSingleFeedAndTweetNoPhoto.FeedAndTweet()

    now = str(datetime.datetime.now())
    message= "Hello Chum! Eat up! %s" % (now)

    print("Fed and Tweeted: %s %s %d" % (message, now, i+1))
    time.sleep(100)#####MAKE THIS 86400 for 24 HOURS, 3600 for 1 hour
