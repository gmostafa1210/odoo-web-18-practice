# -*- encoding: utf-8 -*-
###################################################################
#
#       G. Mostafa
#       Copyright (C) 2024 (https://gmostafa1210.github.io/)
#
###################################################################

from odoo import http
from odoo.http import request


class WebCustom(http.Controller):
    @http.route('/res_partner_web', type='http', auth='public', website=True)
    def res_partner_web(self, **kw):
        return request.render('gm_web_custom.res_partner_website_form', {})
    
    @http.route('/my/res_partner_web', type='http', auth='public', website=True)
    def my_res_partner_web(self, **kw):
        return request.render('gm_web_custom.my_res_partner_web', {})