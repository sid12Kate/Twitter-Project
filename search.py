import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from myuser import MyUser
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class Search(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        myuser = MyUser()
        uname = myuser.query().fetch()
        action = self.request.get('button')
        if action == 'Search':
            name = self.request.get('value')
            for x in uname:
                if x.username == name:
                    self.redirect('/searchresult?value_1='+name)


        template_values = {
         'myuser' : myuser,
         'uname' : uname,
        }
        template =JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        if action == 'Back':
            self.redirect('/')
