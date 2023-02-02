from odoo import api, fields, models

class Laporan(models.Model):
    _name = 'laporan'
    _description = 'laporan barang'
    _check_company_auto = True
    _rec_name = 'barang_id'
    _order = 'barang_id asc'


    barang_id = fields.Many2one(comodel_name='barang', string='Nama')
    
    active = fields.Boolean(string='Active', default=True)


    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]

