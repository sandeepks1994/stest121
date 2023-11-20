from odoo import http
from odoo.http import request
from odoo.tools import html_escape
import base64

class CustomCustomerPage(http.Controller):
    @http.route('/my_blog/blogs/page', auth='public', website=True)
    def my_blogs(self):
        blogs = request.env['my_blog.blog'].search([])
        return request.render('blog.blogs_page_template', {'blogs': blogs})
    

class EmployeeReg(http.Controller):
    @http.route('/my_website/welcome', type='http', auth='public', website=True)
    def MyWebsite_welcome(self):
        return request.render('blog.my_website_home_page_template')