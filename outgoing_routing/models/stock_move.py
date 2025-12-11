# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"
    _description = "Stock Move"

    ventor_picked = fields.Boolean('Ventor Picked')
