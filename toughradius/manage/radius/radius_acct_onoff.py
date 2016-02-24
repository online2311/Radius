#!/usr/bin/env python
# coding=utf-8

from toughradius.manage.radius.radius_basic import  RadiusBasic
from radiuslib.storage import Storage
from toughradius.manage import models
from radiuslib import  utils, dispatch, logger
from toughradius.manage.settings import *

class RadiusAcctOnoff(RadiusBasic):

    def __init__(self, dbengine=None,cache=None,aes=None,request=None):
        RadiusBasic.__init__(self, dbengine,cache,aes, request)

    def acctounting(self):
        self.unlock_online(self.request.nas_addr,None)
        logger.info('bas accounting onoff success')
