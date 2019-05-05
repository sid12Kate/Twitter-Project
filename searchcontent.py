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

class SearchContent(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        myuser = MyUser()
        uname = myuser.query().fetch()
        action = self.request.get('button')
        contentlist = []
        if action == 'Search':
            content = self.request.get('value')
            #content = content.split()
            for x in uname:
                for y in x.tweet:
                    if content in y:
                            contentlist.append(y)




        template_values = {
         'myuser' : myuser,
         'uname' : uname,
         'contentlist' : contentlist
        }
        template =JINJA_ENVIRONMENT.get_template('searchcontent.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        if action == 'Back':
            self.redirect('/')
