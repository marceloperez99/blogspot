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


#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/hero_page.html")
        self.response.write(template.render())

class ProfileHandler(webapp2.RequestHandler):
            def get(self):
                template = jinja_environment.get_template("templates/profile.html")
                self.response.write(template.render())

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

class ContactHandler(webapp2.RequestHandler):
        def get(self):
            template = jinja_environment.get_template("templates/contact_form.html")
            render_data = {}
            self.response.write(template.render(render_data))

class BlogshowHandler(webapp2.RequestHandler):
        def get(self):
            template = jinja_environment.get_template("templates/blogshow.html")
            render_data = {}
            self.response.write(template.render(render_data))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blogz', BlogzHandler),
    ('/add', BlogaddHandler),
    ('/prof', ProfileHandler),
    ('/contact', ContactHandler),
], debug=True)
