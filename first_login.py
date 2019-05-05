import webapp2
import jinja2
from google.appengine.api import users
from myuser import MyUser
import os

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class FirstLogin(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        myuser = MyUser()

        template_values = {
         'myuser' : myuser
        }
        template =JINJA_ENVIRONMENT.get_template('first_login.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        if action == 'Submit':
            user = users.get_current_user()
            myuser = MyUser(id=user.user_id())
            myuser.email_address = user.email()
            myuser.username = self.request.get('value_1')
            myuser.fullname = self.request.get('value_2')
            myuser.bio = self.request.get('value_3')
            myuser.put()
            self.redirect('/')
        else:
            self.redirect('/')
