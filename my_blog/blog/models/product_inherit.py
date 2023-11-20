from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'

    hide_price = fields.Boolean(string="Hide Price")
