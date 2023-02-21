from odoo import api, fields, models, _
from odoo.tools import float_repr
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError
import base64
from datetime import datetime, date
import pytz

class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_sa_qr_code_str = fields.Char(string='Zatka QR Code', compute='_compute_qr_code_str',store=True)
