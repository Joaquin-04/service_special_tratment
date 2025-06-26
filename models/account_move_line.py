# models/account_move_line.py
from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_unit_editable = fields.Boolean(compute='_compute_price_unit_editable', store=True)

    @api.depends('product_id')
    def _compute_price_unit_editable(self):
        for line in self:
            line.price_unit_editable = line.product_id.type == 'service'
