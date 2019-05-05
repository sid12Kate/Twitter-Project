import webapp2
import jinja2
from google.appengine.api import users
from myuser import MyUser
from first_login import FirstLogin
from profile import Profile
from google.appengine.ext import ndb
from edit import Edit
from search import Search
from searchresult import SearchResult
from searchcontent import SearchContent
from tweet import Tweet
from edit_tweet import EditTweet
import os
from datetime import datetime
import logging
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        url = ''
        url_string = ''
        user = users.get_current_user()
        usernames = []
        print_tweet = []
        username_list = []


        if user:
           url = users.create_logout_url(self.request.uri)
           url_string = 'logout'
           myuser_key = ndb.Key('MyUser', user.user_id())
           myuser = myuser_key.get()
           if myuser == None:
               self.redirect('/first_login')
           myuser_list = MyUser().query().fetch()
           tweet = Tweet()
           tweet_list = tweet.query().fetch()

           for x in myuser_list:
               if x.username in myuser.following:
                    usernames.append(x.username)

           for x in usernames:
                for y in tweet_list:
                   if x == y.username:
                        print_tweet.append(y)


           for y in tweet_list:
               if y.username == myuser.username:
                   print_tweet.append(y)


           logging.info(print_tweet)
           logging.info(username_list)
        else:
           url = users.create_login_url(self.request.uri)
           url_string = 'login'




        template_values = {
        'url' : url,
        'url_string' : url_string,
        'user' : user,
        'print_tweet' : print_tweet,
        'username_list' : username_list
           }


        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        if action == 'Post':
            string = self.request.get('value')
            user = users.get_current_user()
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()
            myuser.tweet.append(string)
            myuser.put()
            tweet = Tweet()
            tweet_key = ndb.Key('Tweet', self.request.get('value') )
            tweet = tweet_key.get()
            if tweet == None:
                tweet = Tweet(id=self.request.get('value'))
                tweet.username = myuser.username
                tweet.tweet = self.request.get('value')
                tweet.tweettime = datetime.now()
                tweet.put()
            else:
                tweet.tweet = self.request.get('value')
                tweet.username = myuser.username
                tweet.tweettime = datetime.now()
                tweet.put()
            self.redirect('/')
        else:
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/first_login', FirstLogin),
    ('/edit', Edit),
    ('/profile', Profile),
    ('/search', Search),
    ('/searchresult', SearchResult),
    ('/searchcontent', SearchContent),
    ('/edit_tweet', EditTweet),
    ], debug=True)
