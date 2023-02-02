from odoo import api, fields, models 

class BarangMasukData(models.Model):
    _name = 'barangmasuk.data'
    _description = 'Model Hitung Barang Masuk Data'
    _check_company_auto = True
    _rec_name = 'barang_id'
    _order = 'barang_id asc'


    barang_id = fields.Many2one(comodel_name='barang', string='Barang')
    jumlah = fields.Integer(string='Jumlah',store=True)
    
    barang_masuk_ids = fields.Many2one(comodel_name='barang.masuk', string='Barang')
    

    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]


    @api.model
    def create(self, values):
        # Add code here
        barangmasuk = super(BarangMasukData, self).create(values)


        barang = self.env['barang'].search([('id','=', barangmasuk.barang_id.id)], limit=1)

        barang.jumlah = barang.jumlah + barangmasuk.jumlah

        return barangmasuk



    # limit untuk mengambil data 1
    # barang masuk proses simpan data ke tabel barang masuk, hasil data disimpan di variabel barangmasuk
    # barang untuk mengambil record tabel barang dan bisa di tampilkan di tabel barang masuk