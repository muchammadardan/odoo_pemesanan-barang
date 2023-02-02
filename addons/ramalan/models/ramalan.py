from odoo import api, fields, models 

class Ramalan(models.TransientModel):
    _name = 'ramalan'
    _description = 'ramalan data barang'
    _check_company_auto = True
    _rec_name = 'barang_id'
    _order = 'barang_id asc'

    
    barang_id = fields.Many2one(comodel_name='barang', string='Barang')
    
    eoq = fields.Float(string='EOQ (Unit)', readonly=True)
    toc = fields.Float(string='TOC (Total Biaya Pesan Rupiah)',readonly=True)
    tcc = fields.Float(string='TCC  (Total Biaya Simpan Rupiah)',readonly=True)
    tc = fields.Float(string='TC (Total Biaya Persediaan Minimum Rupiah)')
    f = fields.Float(string='F (Frekuensi Pemesanan)')
    t = fields.Float(string='T (Jarak Siklus)')
    exp = fields.Float(string='EXP (Durasi Habis EOQ Hari)')
    ss = fields.Float(string='SS (Safety Stock Unit)')
    rop = fields.Float(string='ROP (Titik Pemesanan Kembali Unit)')
    
    
    
    
    
    
    
    





    active = fields.Boolean(string='Active', default=True)


    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]


    

    # abstrak model hanya view tidak disimpan di database
    # model model disimpan ke database
    # transient model model disimpen di data base sementara 