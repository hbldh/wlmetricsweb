#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`views.py`
==================

.. module:: views.py
   :platform: Unix, Windows
   :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>

Created on 2014-09-09, 15:08

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from flask import render_template, jsonify, request, redirect, send_file
from flask.ext.stormpath import login_required, user, groups_required

from wlmetricsweb import app, forms, config, stormpath_manager, mongodb

@app.route('/', methods=['GET', ])
def index():
    if user.is_authenticated():
        return render_template('index.html', title='{0} {1}'.format(user.given_name, user.surname))
    else:
        return render_template('landing.html', title='Home')
