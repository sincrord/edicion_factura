from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_edicion_factura_user = fields.Boolean(
        compute='_compute_is_edicion_factura_user',
        store=False
    )

    def _compute_is_edicion_factura_user(self):
        group = self.env.ref('edicion_factura.group_edicion_factura')
        user = self.env.user
        for rec in self:
            rec.is_edicion_factura_user = group in user.groups_id