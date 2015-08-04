#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.stormpath import StormpathManager

app = Flask(__name__)
app.config.from_object('wlmetricsweb.config')
stormpath_manager = StormpathManager(app)

from wlmetricsweb import views, filters, forms
