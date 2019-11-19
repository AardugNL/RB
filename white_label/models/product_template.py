# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           # 
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields, api

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	white_label_description = fields.Text(
        'White Label Description')
	white_label_sale_price = fields.Float(
        'White Label Sales Price')
	box_quantity = fields.Integer()
	box_square_meter = fields.Float()

	@api.model
	def create(self, values):
		record = super(ProductTemplate, self).create(values)
		if not record.white_label_description and record.white_label_sale_price == 0.00:
			record.white_label_description = record.description_sale 
			record.white_label_sale_price = record.list_price
		return record