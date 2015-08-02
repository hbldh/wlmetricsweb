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

from wlmetricsweb import app, forms, config


@app.route('/', methods=['GET', ])
def index():
    return render_template('index.html',
                           title='Home')
