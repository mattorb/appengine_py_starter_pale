#!/usr/bin/env python
# encoding: utf-8

from google.appengine.ext import db

class BaseModel(db.Model):                           
    stamp = db.DateTimeProperty(auto_now_add=True)  # keep this to make data syncing easier

class User(BaseModel):
    name = db.StringProperty()
    friendCount = db.IntegerProperty(default=2)
    subscribed = db.BooleanProperty(default=True) 
    pictureData = db.BlobProperty()
