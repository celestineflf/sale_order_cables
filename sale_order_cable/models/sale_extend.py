from odoo import fields, models, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    
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
    cable_eye_1 = fields.Many2one(
        'product.product', index=True, copy=True, store=True, domain=lambda self:"['|',('is_strip', '=', True),('cable_thick', '=', cable_thick),('is_cable_eye', '=', True)]"
    )
    cable_eye_2 = fields.Many2one(
        'product.product', index=True, copy=True, store=True, domain=lambda self:"['|',('is_strip', '=', True),('cable_thick', '=', cable_thick),('is_cable_eye', '=', True)]"
    )    
    cable_ex = fields.Many2one(
        'product.product', index=True, copy=True, store=True
    )
    cable_make = fields.Many2one(
        'product.product', string="Cable Make Product", index=True, copy=True, store=True
    )
    cable_product = fields.Many2one(
        'product.product', string="Cable Product", index=True, copy=True, store=True
    )
    cable_len = fields.Float(
        string="Cable Length in Meters", index=True, copy=True, store=True
    )


    
    @api.onchange('cable_ex')
    def onchange_cable_products(self):
        self.cable_make = self.env['product.product'].search([('cable_make', '=', True)])
        self.cable_product = self.env['product.product'].search([('cable_product', '=', True)])
         

    @api.onchange('cable_color', 'cable_thick')
    def onchange_cable_ex(self):
        product = self.env['product.product']
        if self.cable_color != False and self.cable_thick != False:
            self.cable_ex = product. search([('cable_color', '=', self.cable_color), ('cable_thick', '=', self.cable_thick), ('is_standard_cable', '=', True)])


    def action_cable_line(self):
        self.ensure_one()
        vals={}
        cable = self.cable_product
        cable_ex = self.cable_ex
        service = self.cable_make
        eye_1 = self.cable_eye_1
        eye_2 = self.cable_eye_2
        qty = self.cable_len
        line = self.env['sale.order.line']
        if self.cable_product != False:
            vals = {
                'sequence': 200,
                'product_id': cable.id,
                'product_uom': 1,
                'product_uom_qty': 1,
                'price_unit': ((cable_ex.list_price * qty) + service.list_price + eye_1.list_price + eye_2.list_price),
                'purchase_price': ((cable_ex.standard_price * qty) + service.standard_price + eye_1.standard_price + eye_2.standard_price),
                'name': cable.name,
                'order_id': self.id,
                'tax_id': cable.taxes_id,
                
            }
        add = line.sudo().create(vals)
        return add

    def action_make_mrp(self):
        cable_ex = self.cable_ex
        cable = self.cable_product
        eye_1 = self.cable_eye_1
        eye_2 = self.cable_eye_2
        qty = self.cable_len
        mrp = self.env['mrp.production']
        line = self.env['stock.move']
        line_cable = line.create({
            'product_id': cable_ex.id,
            'name': cable_ex.name,
            'product_uom': 1,
            'product_uom_qty': qty,
            'location_id': cable_ex.property_stock_inventory.id,
            'location_dest_id': cable_ex.property_stock_production.id,
        })
        line_eye_1 = line.create({
            'product_id': eye_1.id,
            'name': eye_1.name,
            'product_uom': 1,
            'product_uom_qty': 1,
            'location_id': eye_1.property_stock_inventory.id,
            'location_dest_id': eye_1.property_stock_production.id,
        })
        line_eye_2 = line.create({
            'product_id': eye_2.id,
            'name': eye_2.name,
            'product_uom': 1,
            'product_uom_qty': 1,
            'location_id': eye_2.property_stock_inventory.id,
            'location_dest_id': eye_2.property_stock_production.id,
        })
        vals = {
            'product_id': cable.id,
            'product_qty': 1,
            'product_uom_id': 1,
            'move_raw_ids': line_cable + line_eye_1 + line_eye_2,
        }

        return mrp.create(vals)
        



    