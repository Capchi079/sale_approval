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
            if record.state == 'approval_one':  # Check if current state is 'draft'
                record.state = 'approval_two'  # Set the state to 'pre_ongoing'
            else:
                raise UserError("You can only move to 'Pre-Ongoing' from 'Draft' state.")

    @api.model
    def create(self, vals):
        """Override the create method to set default state to 'approval_one'."""
        vals['state'] = 'approval_one'  # Automatically set state to 'approval_one'
        return super(SaleOrderInherit, self).create(vals)

