from twython import Twython
import datetime
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

now = str(datetime.datetime.now())
message= "Tweet coming to you from the Terminal and vi editor!! %s" % now

twitter.update_status(status=message)

print("Tweeted: %s %s" % (message, now))

