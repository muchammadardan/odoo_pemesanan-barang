from odoo import api, fields, models

class Transaksi(models.Model):
    _name = 'transaksi'
    _description = 'Model Transaksi Barang'
    _check_company_auto = True
    _rec_name = 'tanggal'
    _order = 'nota asc'

    nota = fields.Char(string='Nota', readonly=True)
    tanggal = fields.Date(string='Tanggal')

    pelanggan_id = fields.Many2one(comodel_name='pelanggan', string='Pelanggan')

    pemesanan_ids = fields.One2many(comodel_name='pemesanan', inverse_name='transaksi_id', string='Penjualan' , ondelete='cascade')
    
    total_brg = fields.Integer(string='Total Barang',compute='_compute_total_brg', store=True)
    

    sub_total = fields.Integer(string='Sub Total Harga',compute='_compute_sub_total', store=True)
    
    

    


    active = fields.Boolean(string='Active', default=True)



    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]



    @api.depends('pemesanan_ids')
    def _compute_sub_total(self):
        
        for rec in (self) :

            total_barang=0
            for barang in rec.pemesanan_ids:

                total_barang= total_barang + barang.total

            rec.sub_total= total_barang

    def _compute_total_brg(self):

        for rec in (self) :
            rec.total_brg = sum(rec.mapped('pemesanan_ids.jumlah'))

    
    @api.model
    def create(self, values):
        # Add code here
        values['nota']=self.env['ir.sequence'].next_by_code('transaksi')

        return super(Transaksi, self).create(values)


    def unlink(self):
        # Add code here

        # raise ValueError(self.jumlah)

        res = super(Transaksi, self).unlink()

        for rec in self :   
            rec.pemesanan_ids.barang_id.jumlah = rec.pemesanan_ids.barang_id.jumlah + rec.pemesanan_ids.jumlah
        
        
        
        
        # self.pemesanan_ids.jumlah = self.pemesanan_ids.jumlah + self.jumlah
        
        # res = super(Transaksi, self).unlink()
    

        # for rec in self :
        #     rec.pemesanan_ids.jumlah = res
