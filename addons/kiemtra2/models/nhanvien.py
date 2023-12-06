from odoo import models, fields

class NhanVien(models.Model):
    _name = 'nhanvien'

    name = fields.Char(string='Họ và tên', required=True)
    empid = fields.Integer(string='Mã nhân viên', required=True)
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], string='Giới tính')
    phone = fields.Char(string='Điện thoại')