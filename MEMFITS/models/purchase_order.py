import string
from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    receipt_date= fields.Date() 
    delivery_partner_id = fields.Many2one('res.partner') 

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    delivery_partner_id = fields.Many2one('res.partner')
    company_id = fields.Many2one('res.company',readonly=False)

class AnalyticTag(models.Model):
    _name='analytic.tag'

    name = fields.Char()

class HrExpense(models.Model):
    _inherit='hr.expense'

    analytic_tag_id= fields.Many2one(
        'analytic.tag',
        )
    analytic_account_id= fields.Many2one(
        'account.analytic.account',
        )