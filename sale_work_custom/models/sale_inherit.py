from odoo import api, fields, models
from odoo.exceptions import UserError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', "Quotation"),
        ('approval_one', "Waiting For Approval"),
        ('approval_two', "Approve"),
        ('sent', "Quotation Sent"),
        ('sale', "Sales Order"),
        ('cancel', "Cancelled")], string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')

    def action_second_approval(self):
        for record in self:
            if record.state == 'approval_one':
                record.state = 'approval_two'
            else:
                raise UserError("You can only move to from 'Draft' state.")

    @api.model
    def create(self, vals):

        vals['state'] = 'approval_one'
        return super(SaleOrderInherit, self).create(vals)

    def action_custom_confirm(self):
        """ Custom Confirm Button - Moves from approval_two to sale """
        for record in self:
            if record.state == 'approval_two':
                record.state = 'sale'
            else:
                raise UserError("You Need Approval From The CEO.")


