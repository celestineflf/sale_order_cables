from odoo import fields, models, api, _

class ProductProduct(models.Model):
    _inherit = 'product.product'

    cable_product = fields.Boolean(string="Is Cable Product?", index=True, copy=True, store=True)
    is_standard_cable = fields.Boolean(string="Is standard Cable?", index=True, copy=True, store=True)
    cable_make = fields.Boolean(string="Cable Make Product", index=True, copy=True, store=True)
    is_cable_eye = fields.Boolean(string='Is Cable Eye?', index=True, copy=True, store=True)
    is_strip = fields.Boolean(string='Is Strip Product?', index=True, copy=True, store=True)
    cable_color = fields.Selection([
        ('red', 'Red'),
        ('black', 'Black'),
        ], index=True, copy=True, store=True
    )
    cable_thick = fields.Selection([
        ('2,5', '2,5mm'),
        ('6', '6mm'),
        ('10', '10mm'),
        ('16', '16mm'),
        ('25', '25mm'),
        ('35', '35mm'),
        ('50', '50mm'),
        ('70', '70mm'),
        ('95', '95mm'),
        ('120', '120mm'),
        ], index=True, copy=True, store=True
    )
    eye_type = fields.Selection([
        ('m6', 'M6'),
        ('m8', 'M8'),
        ('m10', 'M10'),
        ('m12', 'M12'),
        ], index=True, copy=True, store=True
    )
    
    