# models/purchase_order_line.py
from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_unit_editable = fields.Boolean(compute='_compute_price_unit_editable', store=True)

    @api.depends('product_id')
    def _compute_price_unit_editable(self):
        for line in self:
            line.price_unit_editable = line.product_id.type == 'service' or line.product_id.type == 'consu'
