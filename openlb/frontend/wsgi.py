#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from openlb.extensions import db

from flask import Flask
from oslo.config import cfg

application_opts = [
    cfg.BoolOpt('debug', default=False, help='Enable debug mode'),
]

CONF = cfg.CONF
CONF.register_cli_opts(application_opts)
CONF.register_opts(application_opts)

app = Flask(__name__)


def init_app():

    app.config['SQLALCHEMY_DATABASE_URI'] = CONF.database.connection
    db.init_app(app)

    from openlb.frontend.dashboard import dashboard
    app.register_blueprint(dashboard)


def wsgi_app():
    return app
