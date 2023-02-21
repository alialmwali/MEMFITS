# -*- coding: utf-8 -*-
from hashlib import algorithms_available
import string
from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    contact_ref = fields.Char(string="Contact ID",readonly=True)
    customer_category= fields.Many2one('customer.category',required=True)
    market_segment = fields.Many2one('market.segment',required=True)
    region_id = fields.Many2one('res.region',required=True)
    currency_id = fields.Many2one('res.currency',string="Supplier Currency")
    carrier_id = fields.Many2one('delivery.carrier', string="Delivery Method", ondelete='cascade')
    lang_id = fields.Many2one('res.lang')
    vat_number = fields.Char()
    cr_number= fields.Char()
    vat_certificate= fields.Binary(attachment=True)
    cr_copy= fields.Binary(attachment=True)
    registration_number = fields.Char()
    name_in_arabic = fields.Char(required=True)
    address_arabic = fields.Char(required=True)
    city_arabic = fields.Char(required=True)
    country_arabic = fields.Char(required=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')
  
class CustomerCategory(models.Model):
    _name = 'customer.category'

    name = fields.Char()
class MarketSegment(models.Model):
    _name = 'market.segment'

    name = fields.Char()

class Region(models.Model):
    _name = 'res.region'

    name= fields.Char()
class Rescompany(models.Model):
    _inherit = 'res.company'
    
    coc_client = fields.Char(string='COC Client')
    bank_name = fields.Char()
    swiftbic_code = fields.Char(string="SWIFT/BIC Code")
    iban = fields.Char()
    