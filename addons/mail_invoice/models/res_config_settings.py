from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mail_invoice_imap_server = fields.Char()
    mail_invoice_imap_user = fields.Char()
    mail_invoice_imap_pass = fields.Char()

    # @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            mail_invoice_imap_server = self.env['ir.config_parameter'].sudo().get_param('mail_invoice.mail_invoice_imap_server'),
            mail_invoice_imap_user = self.env['ir.config_parameter'].sudo().get_param('mail_invoice.mail_invoice_imap_user'),
            mail_invoice_imap_pass = self.env['ir.config_parameter'].sudo().get_param('mail_invoice.mail_invoice_imap_pass'),
        )
        return res

    # @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()

        param.set_param('mail_invoice.mail_invoice_imap_server', self.mail_invoice_imap_server)
        param.set_param('mail_invoice.mail_invoice_imap_user', self.mail_invoice_imap_user)
        param.set_param('mail_invoice.mail_invoice_imap_pass', self.mail_invoice_imap_pass)
