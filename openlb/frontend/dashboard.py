#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from flask import render_template
import flask

dashboard = flask.Blueprint('frontend', __name__)


@dashboard.route('/')
def index():
    return render_template('index.html')
