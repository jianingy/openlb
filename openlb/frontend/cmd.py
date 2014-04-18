#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from openlb.common import gettextutils
from openlb.frontend import wsgi as frontend_wsgi

from oslo.config import cfg
from werkzeug.serving import run_simple
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.debug import DebuggedApplication

import logging
import os
import sys

__project__ = 'openlb'

LOG = logging.getLogger(__name__)
CONF = cfg.CONF

server_opts = [
    cfg.StrOpt('bind',
               default='127.0.0.1',
               help='Bind address'),
    cfg.IntOpt('port',
               default=5000,
               help='Bind port'),
]

CONF = cfg.CONF
CONF.register_cli_opts(server_opts)
CONF.register_opts(server_opts)


def main():
    gettextutils.install(__project__)
    LOG.info(_('Server started'))
    CONF(sys.argv[1:], project=__project__)

    if CONF.debug:
        logging.basicConfig(level=logging.DEBUG)

    wsgi_app = frontend_wsgi.create_app()

    if CONF.debug:
        wsgi_app = DebuggedApplication(wsgi_app, evalex=True)

    app = SharedDataMiddleware(wsgi_app, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
        })

    run_simple(CONF.bind, CONF.port, app, use_reloader=CONF.debug)
