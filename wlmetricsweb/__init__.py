#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.config.from_object('wlmetricsweb.config')

from wlmetricsweb import views, filters, forms
