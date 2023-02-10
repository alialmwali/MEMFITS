import string
from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    # project_id = fields.Many2one('project.project')
    quotaion_ref = fields.Char(readonly=True)
    order_ref = fields.Char(readonly=True)
    expiration_close = fields.Date(required=True)
    department_name = fields.Char()

    _sql_constraints = [
        ('unique_quotaion_ref',
         'UNIQUE(quotaion_ref)',
         "The quotaion_ref of the Quotaion must be unique!"), ('unique_order_ref',
                                                               'UNIQUE(order_ref)',
                                                               "The order_ref of the Quotaion must be unique!")
    ]

    @api.model
    def create(self, vals):   
        sequence_code = 'quotaion'
        seq_order = 'order'
        vals['quotaion_ref'] = self.env['ir.sequence'].next_by_code(sequence_code)
        vals['order_ref'] = self.env['ir.sequence'].next_by_code(seq_order)
        return super(SaleOrder, self).create(vals)