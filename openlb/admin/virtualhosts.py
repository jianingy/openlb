#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from openlb.extensions import db_admin
from openlb.models.virtualhosts import VirtualHost

from flask.ext.admin.contrib.sqla import ModelView


admin_view = ModelView(VirtualHost, db_admin.session)
