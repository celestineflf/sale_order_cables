from odoo import fields, models, api, _

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    partner_id = fields.Many2one(
        'res.partner', string="Customer", index=True, copy=True, store=True, domain=lambda self: 
    )