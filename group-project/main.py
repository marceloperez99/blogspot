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


#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/hero_page.html")
        self.response.write(template.render())
        #


#class ProfileHandler(webapp2.RequestHandler):
        # def get(self):
        # .put
        # .remove



#class AboutHandler(webapp2.RequestHandler):


# class ProfileHandler(webapp2.RequestHandler):
#         def get(self):
#
# class ProfileModel(ndb.Model):
#
# class UserModel(ndb.Model):
#     # desc = ndb.TextProperty()
#     # profile_pic = ndb.BlobProperty()
#     username = ndb.KeyProperty(repeated = True)
#
# # class SourcePageModel(ndb.Model):
# #     url = n
#
# class BlogModel(ndb.Model):
#         title = ndb.StringProperty()
#         url = ndb.LinkProperty()
#
#
#
# class SourceHandler(webapp2.RequestHandler):


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/prof', ProfileHandler),
    # ('/about', AboutHandler),
    # ('/source', SourceHandler),
], debug=True)
