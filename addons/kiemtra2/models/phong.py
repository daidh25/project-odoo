from odoo import models, fields

class Phong(models.Model):
    _name = 'phong'

    name = fields.Char(string='Tên phòng', required=True)
    depid = fields.Integer(string='Mã phòng', required=True)