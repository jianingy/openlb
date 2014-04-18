#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from openlb.common import db

from openlb.models.model_base import BASE

import sqlalchemy as sa


class VirtualHost(BASE, db.HasIdMixin, db.TimestampMixin):

    __tablename__ = 'tb_virtualhosts'

    server_name = sa.Column(sa.String(60), nullable=False, unique=True)
    listen = sa.Column(sa.String(60), nullable=False, unique=True)
