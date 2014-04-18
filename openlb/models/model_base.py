#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from openlb.extensions import db as flask_db
from openlb.common import db


class BASE(flask_db.Model, db.JSONSeriableMixin, db.TableNameMixin):

    __abstract__ = True
