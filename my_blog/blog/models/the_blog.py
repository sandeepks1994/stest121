# -*- coding: utf-8 -*-

from odoo import models, fields, api , _


class Blog(models.Model):
    _name = 'my_blog.blog'
    _description = 'my_blog_blog'

    sequence = fields.Char(string='Sequence', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    name = fields.Char(string = 'Name',required=True)
    description = fields.Text(string = 'Description',required=True)
    author = fields.Char(string = 'Author',required=True)
    publish_date = fields.Date(string = 'Publish Date',required=True)
    image = fields.Binary(string="Image")


# <!-- ************************** sequence ************************** -->
    @api.model
    def create(self, vals):
        print("In create vals: ",vals)
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('my_blog.blog') or _('New')
        return super(Blog, self).create(vals)