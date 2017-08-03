#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import urllib
import urllib2
import json
from models import BlogModel
from models import UserModel
from google.appengine.api import users


#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def get_or_create_user_model(user):
    userquery = UserModel.query(UserModel.username == user.email())
    userresults = userquery.fetch()

    if len(userresults) > 0 : #if the user model exits this function will retunr it back to us
        return userresults[0]
    else:
        #If the user model does not exist in our datatstor it should create one in the data store and return it back to us
        newuser = UserModel(username= user.email())
        newuser.put()
        return newuser

class MainHandler(webapp2.RequestHandler):
        def get(self):
            template = jinja_environment.get_template("templates/hero_page.html")
            self.response.write(template.render())

class ProfileHandler(webapp2.RequestHandler):
        def get(self):
            template = jinja_environment.get_template("templates/UserProfile.html")
            user = users.get_current_user()
            render_data = {}
            if user:
                render_data["Name"] = user
                blogquery = BlogModel.query()
                blogresults = blogquery.fetch()
                render_data["blogs"] = blogresults
            else:
                render_data["Name"] = "Please Sign In"
            #user_Model = userresults[0]
            self.response.write(template.render(render_data))

class BlogzHandler(webapp2.RequestHandler):
        def get(self):
            template = jinja_environment.get_template("templates/blogz.html")
            allblogs = BlogModel.query().fetch()
            render_data = {}
            render_data["allblogs"] = allblogs
            self.response.write(template.render(render_data))

class BlogaddHandler(webapp2.RequestHandler):
        def get(self):
            template = jinja_environment.get_template("templates/addblog.html")
            addblogs = BlogModel.query().fetch()
            render_data = {}
            render_data["addblogs"] = addblogs
            self.response.write(template.render(render_data))

        def post(self):
            self.added_blog = BlogModel(self.request.get('post'))
            self.added_blog.put()

class ContactHandler(webapp2.RequestHandler):
        def get(self):
            template = jinja_environment.get_template("templates/contact_form.html")
            render_data = {}
            self.response.write(template.render(render_data))

# class BlogshowHandler(webapp2.RequestHandler):
#         def get(self):
#             template = jinja_environment.get_template("templates/blogshow.html")
#             render_data = {}
#             self.response.write(template.render(render_data))

# class UsersHandler(webapp2.RequestHandler):
#         def get(self):
#             template = jinja_environment.get_template("templates/userapi.html")
#             user = users.get_current_user()
#         if user:
#             greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
#                 (users.nickname(), users.create_logout_url('/')))
#         else:
#             greeting = ('<a href="%s">Sign in or register</a>.' %
#                 users.create_login_url('/'))
#
#         self.response.write('<html><body>%s</body></html>' % greeting)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:

            get_or_create_user_model(user)
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/prof'))
        self.response.write('<html><body>%s</body></html>' % greeting)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blogz', BlogzHandler),
    ('/add', BlogaddHandler),
    ('/prof', ProfileHandler),
    ('/contact', ContactHandler),
    # ('/blogshow',BlogshowHandler),
    ('/login', LoginHandler),

], debug=True)
