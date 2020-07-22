# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Mail(models.Model):
    _name = 'mail_invoice.mail'
    _description = 'mail_invoice.mail'

    title = fields.Char()
    date = fields.Datetime()
    from_field = fields.Char()
    to = fields.Char()
    is_handling = fields.Boolean()
    # invoice = fields.E2E()
    files = fields.Char()
    text = fields.Char()
    provider_id = fields.Many2one(
        'res.partner', string='Related Provider', ondelete='cascade', index=True)


class Invoice(models.Model):
    _name = 'mail_invoice.invoice'
    _description = 'mail_invoice.invoice'

    number = fields.Char()
    date = fields.Date()
    provider_id = fields.Many2one(
        'res.partner', string='Related Provider', ondelete='cascade', index=True)
    sum_without_nds = fields.Monetary(currency_field='currency_id')
    sum_with_nds = fields.Monetary(currency_field='currency_id')
    sum_nds = fields.Monetary(currency_field='currency_id')
    weight = fields.Float()
    responsible = fields.Char()
    star = fields.Boolean()

    currency_id = fields.Many2one( 
        'res.currency', string='Currency') 


class InvoiceItem(models.Model):
    _name = 'mail_invoice.invoice_item'
    _description = 'mail_invoice.invoice_item'

    name = fields.Char()
    count_order = fields.Integer()
    count_postorder = fields.Integer()
    count = fields.Integer()
    price_without_nds = fields.Monetary(currency_field='currency_id')
    price_with_nds = fields.Monetary(currency_field='currency_id')
    sum_without_nds = fields.Monetary(currency_field='currency_id')
    sum_nds = fields.Monetary(currency_field='currency_id')
    sum_with_nds = fields.Monetary(currency_field='currency_id')
    rate_nds = fields.Monetary(currency_field='currency_id')
    sum_with_nds = fields.Monetary(currency_field='currency_id')
    thematic = fields.Char()
    count_whole_pack = fields.Integer()
    placer = fields.Integer()
    invoice_id = fields.Many2one(
        'mail_invoice.invoice', string='Invoice', ondelete='cascade', index=True)

    full_name = fields.Char()
    number_global = fields.Char()
    number_local = fields.Char()
    good = fields.Many2one(
        'product.product', string='Product', ondelete='cascade', index=True)

    fact_count = fields.Integer()
    price_gross = fields.Monetary(currency_field='currency_id')
    price_retail = fields.Monetary(currency_field='currency_id')

    currency_id = fields.Many2one( 
        'res.currency', string='Currency') 


class mail_invoice(models.Model):
    _name = 'mail_invoice.mail_invoice'
    _description = 'mail_invoice.mail_invoice'

    name = fields.Char()
    value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    @api.model
    def call_email(self):
        res = self.env['mail_invoice.mail_invoice'].create({'name': 'name'})
        return self.env['mail_invoice.mail_invoice'].search_count([])
