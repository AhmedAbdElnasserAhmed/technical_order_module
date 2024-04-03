from odoo import models, fields

class TechnicalOrder(models.Model):
    _name = 'technical.order'
    _description = 'Technical Order'

    name = fields.Char(string='Request Name', required=True)
    requested_by = fields.Many2one('res.users', string='Requested By', default=lambda self: self.env.user)
    customer = fields.Many2one('res.partner', string='Customer', domain="[('is_tech_offer', '=', True)]", required=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    end_date = fields.Date(string='End Date')
    rejection_reason = fields.Text(string='Rejection Reason', readonly=True, states={'reject': [('readonly', False)]})
    order_lines = fields.One2many('technical.order.line', 'order_id', string='Order Lines')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To be Approved'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', readonly=True, copy=False)

    def submit_for_approval(self):
        self.status = 'to_approve'

    def cancel_order(self):
        self.status = 'cancelled'

    def approve_order(self):
        self.status = 'approved'

    def reject_order(self):
        self.ensure_one()
        # You can implement a wizard to enter rejection reason here
        self.status = 'rejected'

    def _compute_total_price(self):
        for order in self:
            order.total_price = sum(order.order_lines.mapped('total'))



class TechnicalOrderLine(models.Model):
    _name = 'technical.order.line'
    _description = 'Technical Order Line'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    description = fields.Char(string='Description', related='product_id.name')
    quantity = fields.Float(string='Quantity', default=1)
    price = fields.Float(string='Price', related='product_id.lst_price', readonly=True)
    total = fields.Float(string='Total', compute='_compute_total')

    order_id = fields.Many2one('technical.order', string='Order')

    def _compute_total(self):
        for line in self:
            line.total = line.quantity * line.price
