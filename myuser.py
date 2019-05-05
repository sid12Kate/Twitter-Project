from google.appengine.ext import ndb

class MyUser(ndb.Model):
    email_address = ndb.StringProperty()
    username = ndb.StringProperty()
    fullname = ndb.StringProperty()
    bio = ndb.StringProperty()
    tweet = ndb.StringProperty(repeated=True)
    following = ndb.StringProperty(repeated=True)
    followers = ndb.StringProperty(repeated=True)
