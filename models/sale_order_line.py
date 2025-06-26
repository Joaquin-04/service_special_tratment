# models/sale_order_line.py
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_unit_editable = fields.Boolean(compute='_compute_price_unit_editable', store=True)

    @api.depends('product_id')
    def _compute_price_unit_editable(self):
        for line in self:
            line.price_unit_editable = line.product_id.type == 'service'
