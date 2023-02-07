from hashlib import algorithms_available
import string
from odoo import models, fields, api, _

class Project(models.Model):
    _inherit = 'project.project'

    billable  = fields.Boolean(
    default=True
    )
    time_sheet  = fields.Boolean( default=True)
    planning = fields.Boolean( default=True)
    create_task = fields.Char(string="Create task by sending an email to")