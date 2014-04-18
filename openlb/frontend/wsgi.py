#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from openlb.extensions import admin, db, db_admin

from flask import Flask
from oslo.config import cfg

application_opts = [
    cfg.BoolOpt('debug', default=False, help='Enable debug mode'),
]

CONF = cfg.CONF
CONF.register_cli_opts(application_opts)
CONF.register_opts(application_opts)


def init_app(app):
    app.debug = CONF.debug

    app.config['SQLALCHEMY_DATABASE_URI'] = CONF.database.connection
    db.init_app(app)
    db_admin.init_app(app)

    from openlb.frontend.dashboard import dashboard
    app.register_blueprint(dashboard)

    from flask.ext.assets import Environment
    Environment(app)
    app.config['ASSETS_DEBUG'] = CONF.debug

    from openlb.admin import virtualhosts
    admin.init_app(app)
    admin.add_view(virtualhosts.admin_view)


def create_app():
    app = Flask(__name__)
    init_app(app)
    return app
