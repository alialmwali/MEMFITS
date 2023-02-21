from odoo import api, fields, models, _
from odoo.tools import float_repr
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError
import base64
from datetime import datetime, date
import pytz

class AccountMove(models.Model):
    _inherit = 'account.move'

    qr_code_str = fields.Char(string='Zatka QR Code', compute='_compute_qr_code_str')
    confirm_date = fields.Datetime(default=lambda self: fields.Datetime.now())

    def convert_withtimezone(self, date):
        """
        Convert to Time-Zone with compare to UTC
        """
        tz_name = 'Asia/Riyadh' or self.env.context.get('tz') or self.env.user.tz
        contex_tz = pytz.timezone(tz_name)
        date_time_local = pytz.utc.localize(date).astimezone(contex_tz)
        return date_time_local.strftime(DEFAULT_SERVER_DATETIME_FORMAT)

    @api.depends('amount_total', 'amount_untaxed', 'confirm_date', 'company_id', 'company_id.vat')
    def _compute_qr_code_str(self):
        """ Generate the qr code for Saudi e-invoicing. Specs are available at the following link at page 23
        https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20210528_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vShared.pdf
        """
        def get_qr_encoding(tag, field):
            company_name_byte_array = field.encode('UTF-8')
            company_name_tag_encoding = tag.to_bytes(length=1, byteorder='big')
            company_name_length_encoding = len(company_name_byte_array).to_bytes(length=1, byteorder='big')
            return company_name_tag_encoding + company_name_length_encoding + company_name_byte_array
        
        for record in self.with_context(lang='ar_001'):
            seller_name_enc = get_qr_encoding(1, record.company_id.display_name)
            company_vat_enc = get_qr_encoding(2, record.company_id.vat or '*')
            time_sa = fields.Datetime.context_timestamp(self.with_context(tz='Asia/Riyadh'), record.confirm_date or fields.Datetime.now())
            timestamp_enc = get_qr_encoding(3, time_sa.isoformat())
            invoice_total_enc = get_qr_encoding(4, str(record.amount_total))
            total_vat_enc = get_qr_encoding(5, str(record.currency_id.round(record.amount_total - record.amount_untaxed)))
            str_to_encode = seller_name_enc + company_vat_enc + timestamp_enc + invoice_total_enc + total_vat_enc
            record.qr_code_str = base64.b64encode(str_to_encode).decode('UTF-8')
