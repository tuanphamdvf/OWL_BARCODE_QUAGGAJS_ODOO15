from odoo import fields, models


class View(models.Model):
    _inherit = "ir.ui.view"

    type = fields.Selection(
        selection_add=[("barcode_production_view", "barcode_production_view")]
    )
