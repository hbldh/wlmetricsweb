#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.stormpath import StormpathManager
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('wlmetricsweb.config')
stormpath_manager = StormpathManager(app)
mongodb = PyMongo(app)

from wlmetricsweb import views, filters, forms
