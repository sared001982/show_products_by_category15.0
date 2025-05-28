# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from odoo.osv import expression
from datetime import date, datetime, timedelta
from operator import itemgetter
from odoo.tools import float_round
import pytz
import time

from odoo import osv, models, fields, api, tools, exceptions, _
from odoo.tools import format_datetime
from odoo.osv.expression import AND, OR
from odoo.tools.float_utils import float_is_zero
import base64
from odoo.exceptions import UserError
import xlwt
import pandas as pd
from calendar import monthrange

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_order_lines_by_category(self):
        result = {}
        for line in self.order_line:
            category = line.product_id.categ_id
            if category not in result:
                result[category] = []
            result[category].append(line)
        return sorted(result.items(), key=lambda x: x[0].name if x[0] else '')

