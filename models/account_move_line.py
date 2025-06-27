# models/account_move_line.py
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_unit_editable = fields.Boolean(compute='_compute_price_unit_editable', store=True)

    
    @api.depends('product_id')
    def _compute_price_unit_editable(self):
        for line in self:
            move_type = line.move_id.move_type
            product_type = line.product_id.type
            _logger.info(f"[FACTURA] Producto: {line.product_id.display_name} ({product_type}), Move: {move_type}")

            # Editable si es servicio o si es nota de crédito/débito
            line.price_unit_editable = (
                product_type == 'service'
                or product_type == 'consu'
                or move_type in ['out_refund', 'in_refund']  # agregá más si tenés tipos especiales
            )

            """
            _logger.info(f"Producto: {line.product_id.display_name}, tipo: {line.product_id.type}")
            line.price_unit_editable = line.product_id.type == 'service' or line.product_id.type == 'consu'
            """
