import string
from odoo import models, fields, api, _


class Lead(models.Model):
    _inherit ='crm.lead'

    company_name = fields.Char()
    
    customer_category= fields.Many2one('customer.category',required=True)
    market_segment = fields.Many2one('market.segment',required=True)



    opportunity_type = fields.Char()
    language_id = fields.Many2one('res.lang')
    new_date= fields.Char()
    lead_expected_value = fields.Char()
    lead_readiness = fields.Char()
    quoted_same_project_before= fields.Boolean(default=True)
    contact_name= fields.Char()
    email = fields.Char()
    jop_postion = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    # priority = fields.Char()
    tag_ids = fields.Many2many('crm.tag', string='Tags')
    priority_icon = fields.Binary(attachment=True)