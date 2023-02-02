from odoo import api, fields, models 

class BarangMasuk(models.Model):
    _name = 'barang.masuk'
    _description = 'Model Barang Masuk '
    _check_company_auto = True
    _rec_name = 'no'
    _order = 'no asc'

 
    no = fields.Char(string='No', readonly=True )
    tanggal = fields.Date(string='Tanggal')

    barang_ids = fields.One2many(comodel_name='barangmasuk.data', inverse_name='barang_masuk_ids', string='Barang')

    total = fields.Integer(string='Total',compute='_compute_total')
    
    
    active = fields.Boolean(string='Active', default=True)


    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]

    @api.model
    def create(self, values):
        # Add code here
        values['no']=self.env['ir.sequence'].next_by_code('barang.masuk')
        return super(BarangMasuk, self).create(values)

    @api.depends('total')
    def _compute_total(self):
       for rec in self:
        rec.total = sum(rec.mapped('barang_ids.jumlah'))
       
