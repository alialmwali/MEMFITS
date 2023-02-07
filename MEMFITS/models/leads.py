import string
from odoo import models, fields, api, _

class CrmLead(models.Model):
    _inherit ='crm.lead'

    probability = fields.Char()
    company_name = fields.Char()
     # address fields
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    country_code = fields.Char(related='country_id.code', string="Country Code")
    
    website = fields.Char()
    opportunity_name = fields.Char()
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
    sales_person_id = fields.Many2one('res.user')
    sales_team_id= fields.Many2one('crm.team')
    priority = fields.Char()
    tags = fields.Many2one('crm.tag')
    priority = fields.Binary(attachment=True)