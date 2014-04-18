#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianing.yang@qunar.com>
#


class BaseError(Exception):

    message = _("An unknown exception occurred.")
    errcode = -1

    def __init__(self, **kwargs):
        try:
            super(BaseError, self).__init__(self.message % kwargs)
            self.msg = self.message % kwargs
        except Exception:
            # kwargs doesn't match a variable in the message
            # log the issue and the kwargs
            LOG.exception('Exception in string format operation')
            for name, value in kwargs.iteritems():
                LOG.error("%s: %s" % (name, value))
            message = self.message
    super(QException, self).__init__(message)


    def __unicode__(self):
        return unicode(self.msg)
