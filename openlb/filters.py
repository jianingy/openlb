#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from ago import human


def filter_timesince(dt, default="just now"):
    return human(dt, 1)


def init_app(app):
    for func in globals():
        if not func.startswith('filter_'):
            continue
        funcname = func[7:]
        app.jinja_env.filters[funcname] = func
