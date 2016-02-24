#!/usr/bin/env python
#coding=utf-8
import time
import traceback
from radiuslib.btforms import dataform
from radiuslib.btforms import rules
from radiuslib import utils, apiutils, dispatch
from radiuslib import db_cache as cache
from radiuslib.permit import permit
from toughradius.manage.api.apibase import ApiHandler
from toughradius.manage import models
from toughradius.manage.events.settings import ACCOUNT_DELETE_EVENT
from toughradius.manage.settings import * 
from hashlib import md5

""" 客户删除，删除客户资料及相关数据
"""

@permit.route(r"/api/customer/delete")
class CustomerDeleteHandler(ApiHandler):
    """ @param: 
        customer_name: str,
    """

    def get(self):
        self.post()

    def post(self):
        try:
            request = self.parse_form_request()
            customer_name = request.get('customer_name')

            if not customer_name:
                raise Exception("customer_name is empty")

            customer = self.db.query(models.TrCustomer).filter_by(customer_name=customer_name).first()
            if not customer:
                raise Exception("customer is not exists")

            for account in self.db.query(models.TrAccount).filter_by(customer_id=customer.customer_id):
                self.db.query(models.TrAcceptLog).filter_by(account_number=account.account_number).delete()
                self.db.query(models.TrAccountAttr).filter_by(account_number=account.account_number).delete()
                self.db.query(models.TrBilling).filter_by(account_number=account.account_number).delete()
                self.db.query(models.TrTicket).filter_by(account_number=account.account_number).delete()
                self.db.query(models.TrOnline).filter_by(account_number=account.account_number).delete()
                self.db.query(models.TrAccount).filter_by(account_number=account.account_number).delete()
                self.db.query(models.TrCustomerOrder).filter_by(account_number=account.account_number).delete()
                self.add_oplog(u'API删除用户账号%s' % (account.account_number))
                dispatch.pub(ACCOUNT_DELETE_EVENT, account.account_number, async=True)
                dispatch.pub(cache.CACHE_DELETE_EVENT,account_cache_key(account.account_number), async=True)

            self.db.query(models.TrCustomer).filter_by(customer_name=customer_name).delete()
            self.add_oplog(u'API删除用户资料 %s' % (customer_name))    
            self.db.commit()
            return self.render_result(code=0, msg='success')
        except Exception as err:
            self.render_result(code=1, msg=utils.safeunicode(err.message))
            import traceback
            traceback.print_exc()
            return















