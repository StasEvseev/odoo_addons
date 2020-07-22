# -*- coding: utf-8 -*-
from odoo import http


class MailInvoice(http.Controller):
    @http.route('/mail_invoice/mail_invoice/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/mail_invoice/mail_invoice/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('mail_invoice.listing', {
            'root': '/mail_invoice/mail_invoice',
            'objects': http.request.env['mail_invoice.mail_invoice'].search([]),
        })

    @http.route('/mail_invoice/mail_invoice/objects/<model("mail_invoice.mail_invoice"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('mail_invoice.object', {
            'object': obj
        })
