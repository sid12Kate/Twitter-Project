import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import MyUser
from search import Search
import logging
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class SearchResult(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        my_user = MyUser()
        list = my_user.query().fetch()
        value = self.request.get('value_1')
        u_list = []
        for x in list:
            if x.username==value:
                u_list.append(x)
        tweets = u_list[0].tweet
        tweets = tweets[::-1]
        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        if value in myuser.following:
            button = 'Unfollow'
        else:
            button = 'Follow'

        template_values = {
         'u_list' : u_list,
         'tweets' : tweets,
         'value'  : value,
         'button' : button
        }

        template =JINJA_ENVIRONMENT.get_template('searchresult.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        value = self.request.get('value')

        if action == 'Follow':
            myuser.following.append(value)
            myuser.put()
            self.redirect('/searchresult?value_1='+value)

        elif action == 'Unfollow':
            myuser.following.remove(value)
            myuser.put()
            self.redirect('/searchresult?value_1='+value)

        elif action == 'Back':
            self.redirect('/')
