from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    practitioner_id = fields.Many2one(
        'res.partner',
        string='Practitioner',
        domain=[('specialty_ids', '!=', False)],
        help="The practitioner responsible for this sale order."
    )