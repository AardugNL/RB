# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           # 
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    type_show = fields.Selection([
        ('brand', 'Brand'),
        ('whitelabel', 'White Label'),
    ], store=True, string='Type', default='brand')
    box = fields.Float()

    @api.onchange('product_uom_qty')
    def _compute_boxes(self):
        if self.product_id:
            for line in self:
                if line.product_id.box_square_meter > 0.0:
                    line.box = line.product_uom_qty / line.product_id.box_square_meter

    @api.onchange('box')
    def _compute_quantity(self):
        if self.product_id:
            for line in self:
                line.product_uom_qty = line.box * line.product_id.box_square_meter

    @api.onchange('type_show')
    def product_type_change(self):
        if not self.type_show or not self.product_id:
            self.price_unit = 0.0
            return
        if self.type_show == 'whitelabel':
            self.name = self.product_id.white_label_description
            self.price_unit = self.product_id.white_label_sale_price
        else:
            self.name = self.get_sale_order_line_multiline_description_sale(self.product_id)
            self.price_unit = self.product_id.list_price
