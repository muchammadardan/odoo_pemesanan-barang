from odoo import api, fields, models 

class Barang(models.Model):
    _name = 'barang'
    _description = 'Model Barang'
    _check_company_auto = True
    _rec_name = 'nama'
    _order = 'nama asc'

    nama = fields.Char(string='Nama', required=True)
    kode = fields.Char(string='Kode')
    harga_jual = fields.Float(string='Harga Jual')
    harga_beli = fields.Float(string='Harga Beli')
    jumlah = fields.Integer(string='Jumlah' )
    satuan = fields.Selection(string='Satuan', selection=[('pcs', 'PCS')], default='pcs', required=True)
    
    
    gambar = fields.Binary(string='Gambar')
    
    c = fields.Float(string='Biaya Simpan Tahunan')
    # biaya simpan tahunan

    h = fields.Float(string='Biaya Simpan Tahun dalam rupiah')

    wd = fields.Float(string='Hari Kerja')

    l = fields.Float(string='Waktu Tunggu Pengiriman')

    ud = fields.Float(string='Selisih Tanggal Date Dengan Penerimaan Barang')


    
    
    
    
    


    active = fields.Boolean(string='Active', default=True)



    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]

    


    

    