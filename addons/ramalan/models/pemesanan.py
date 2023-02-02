from odoo import api, fields, models 

class Pemesanan(models.Model):
    _name = 'pemesanan'
    _description = 'Model Pemesanan Data Barang'
    _check_company_auto = True
    _rec_name = 'barang_id'
    _order = 'barang_id asc'

    barang_id = fields.Many2one(comodel_name='barang', string='Barang')

    harga = fields.Integer(string='Harga')

    jumlah = fields.Integer(string='jumlah')

    total = fields.Integer(string='Total Harga', compute='_compute_total', store=True)
    
    transaksi_id = fields.Many2one(comodel_name='transaksi', string='Transaksi', ondelete='cascade')
    # fungsi cascade ketika transaksi dihapus makan pemesanan juga dihapus
    
    
    
    active = fields.Boolean(string='Active', default=True)


    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        self.harga = self.barang_id.harga_jual


    @api.depends('harga', 'jumlah')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.harga * rec.jumlah


    @api.model
    def create(self, values):
        # Add code here
        barangkeluar = super(Pemesanan, self).create(values)

        barang = self.env['barang'].search([('id','=',barangkeluar.barang_id.id)], limit=1)
    
        barang.jumlah = barang.jumlah - barangkeluar.jumlah

        return barangkeluar


    def write(self, values):
        # Add code here
        self.barang_id.jumlah = self.barang_id.jumlah + self.jumlah - values['jumlah']
        res = super(Pemesanan, self).write(values) 
        return res

        # fungsi res Mengembalikan recordset untuk id yang disediakan sebagai parameter di lingkungan saat ini
        # 
    
        
    
    # def unlink(self):
    #     # Add code here

    #     # raise ValueError(self.jumlah)   
    #     self.barang_id.jumlah = self.barang_id.jumlah + self.jumlah
        
    #     res = super(Pemesanan, self).unlink()
    #     return res

        

    
    
   