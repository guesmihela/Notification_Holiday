import logging
from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError, Warning
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)

class HrHolidays(models.Model):
    _name = "email.notif"
    _inherit = ['hr.holidays']

    def add_follower_id(self, res_id, partner_id, model):
       followers_obj = self.env['mail.followers']
       follower_id = False
       reg = {
        'res_id': res_id,
        'res_model': model,
        'partner_id': partner_id, }
       try:
        follower_id = followers_obj.create(reg)
       except:
        _logger.info(u'AddFollower: follower already exists')
       return follower_id
