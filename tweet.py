from google.appengine.ext import ndb

class Tweet(ndb.Model):
    username = ndb.StringProperty()
    tweet = ndb.StringProperty()
    tweettime = ndb.DateTimeProperty()
