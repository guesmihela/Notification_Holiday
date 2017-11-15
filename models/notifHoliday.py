import logging
from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError, Warning
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)

class HrHolidays(models.Model):
    
    _inherit = 'hr.holidays'

    def _needaction_domain_get(self):
        return [('state', 'in', ['confirm', 'validate', 'validate1'])]
