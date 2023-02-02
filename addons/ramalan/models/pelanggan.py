from odoo import api, fields, models 

class Pelanggan(models.Model):
    _name = 'pelanggan'
    _description = 'Model Pelanggan'
    _check_company_auto = True
    _rec_name = 'nama'
    _order = 'nama asc'

    nama = fields.Char(string='Nama', required=True)
    alamat = fields.Char(string='Alamat')
    telepon = fields.Char(string='Telepon')
    
    

    active = fields.Boolean(string='Active', default=True)

   
    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]

    