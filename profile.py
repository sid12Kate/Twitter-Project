import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import MyUser
from tweet import Tweet
import logging
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class Profile(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()

        myuser.tweet = myuser.tweet[::-1]
        #logging.info(tweet_list)

        template_values = {
         'myuser' : myuser

        }
        template =JINJA_ENVIRONMENT.get_template('profile.html')
        self.response.write(template.render(template_values))


    def post(self):
        action = self.request.get('button')
        if action == 'Edit':
            value = self.request.get('tweet')
            self.redirect('/edit_tweet?value_1='+value)

        elif action == 'Delete':
            user = users.get_current_user()
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()
            value = self.request.get('tweet')
            tweet_key = ndb.Key('Tweet', value )
            key = tweet_key.get()
            key.key.delete()
            logging.info(key)
            logging.info(value)
            myuser.tweet.remove(value)
            myuser.put()
            self.redirect('/profile')
        elif action == 'Back':
            self.redirect('/')
