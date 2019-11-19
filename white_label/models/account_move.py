# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           # 
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    type_show = fields.Selection([
        ('brand', 'Brand'),
        ('whitelabel', 'White Label'),
    ], string='Type')
    decription = fields.Char()

    @api.model_create_multi
    def create(self, values):
        records = super(AccountMoveLine, self).create(values)
        for record in records:
            saleLine = record.sale_line_ids
            if saleLine:
                record.type_show = saleLine[0].type_show
            else:
                record.type_show = 'brand'
        return records