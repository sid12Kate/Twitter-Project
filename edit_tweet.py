import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import MyUser
from profile import Profile
from tweet import Tweet
import logging
import datetime
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class EditTweet(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        x = self.request.get('value_1')
        template_values = {
         'myuser' : myuser,
         'x' : x
        }
        template =JINJA_ENVIRONMENT.get_template('edit_tweet.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        if action == 'Submit':
            user = users.get_current_user()
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()
            x = self.request.get('value')
            y = self.request.get('tweet')
            if x in myuser.tweet:
                myuser.tweet.remove(x)
            myuser.tweet.append(y)
            myuser.put()
            tweet_key = ndb.Key('Tweet', x )
            tweet = tweet_key.get()
            tweet.key.delete()
            tweet = Tweet(id=y)
            tweet.username = myuser.username
            tweet.tweet = y
            tweet.tweettime = datetime.datetime.now()
            tweet.put()
            self.redirect('/profile')
        elif action == 'Back':
            self.redirect('/')
