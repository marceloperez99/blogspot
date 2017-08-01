from google.appengine.ext import ndb



class UserModel(ndb.Model):
    desc = ndb.TextProperty()
    #profile_pic = ndb.BlobProperty()
    username = ndb.StringProperty()
    favblogs = ndb.KeyProperty(repeated = True)

# class SourcePageModel(ndb.Model):
#     url = n

class BlogModel(ndb.Model):
        title = ndb.StringProperty()
        url = ndb.StringProperty()
        descr = ndb.TextProperty()

class BlogaddModel(ndb.Model)
        title =
        url =
        decri =
        username = 
