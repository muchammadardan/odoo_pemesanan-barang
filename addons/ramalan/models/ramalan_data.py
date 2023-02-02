from odoo import api, fields, models
import math 

class RamalanData(models.TransientModel):
    _name = 'ramalan.data'
    _description = 'Deskripsi'
    _check_company_auto = True
    _rec_name = 'tanggal_mulai'
    _order = 'tanggal_mulai asc'


    tanggal_mulai = fields.Date(string='Tanggal Mulai')
    tanggal_selesai = fields.Date(string='Tanggal Selesai')
    
    active = fields.Boolean(string='Active', default=True)

    def tampilkan(self):
        products = {}
        trans = self.env['pemesanan'].search(
            [
                ('transaksi_id.tanggal', '>=', self.tanggal_mulai),
                ('transaksi_id.tanggal', '<=', self.tanggal_selesai)
            ])

        for tran in trans:
            if tran.barang_id.id in products:
                products[tran.barang_id.id]['R']+= tran.jumlah
            else:
                products[tran.barang_id.id] = {
                    'id': tran.barang_id.id,
                    'nama':tran.barang_id.nama,
                    'R':tran.jumlah,
                    'S':tran.barang_id.harga_beli,
                    'C':tran.barang_id.c,
                    'H':tran.barang_id.h,
                    'WD':tran.barang_id.wd,
                    'L':tran.barang_id.l,
                    'UD':tran.barang_id.ud,
                }
        productsArr=[]        
        for x in products:
            productsArr.append(products[x])

        for product in productsArr:
            # Jumlah Pemesanan Ekonomis EOQ
            product['EOQ'] = round(math.sqrt((2 * product['R'] * product['S']) / (product['H'] * product['C'])))

            # product['TOC'] Biaya Pemesanan Tahunan
            product['TOC'] = round((product['R'] / product['EOQ']) * product['S'])

            # hitung produk ['TCC'] Biaya Simpan Tahunan
            product['TCC'] = round((product['EOQ'] / 2) * (product['H'] * product['C']))

            # TC Biaya Tahunan Minimum
            product['TC'] = round(product['TOC'] + product['TCC'])

            # F* Frekuensi Pemesanan Optimum Per Tahun
            product['F'] = round(product['R'] / product['EOQ'], 2)

            # T Jarak Siklus Optimum
            product['T'] = round(product['EOQ'] / product['R'], 2)

            # EXP Durasi Habis EOQ
            product['EXP'] = round(product['WD'] / product['F'])

            # SS Safety Stock
            product['SS'] = round(product['UD'] * product['R'] / product['WD'])

            # ROP Titik Pemesanan Kembali
            product['ROP'] = round((product['L'] * product['R'] / product['WD']) + product['SS'])


        ramalan_ids = []
        for product in productsArr:
            res = self.env['ramalan'].create({
                'barang_id': product['id'],
                'eoq': product['EOQ'],
                'toc': product['TOC'],
                'tcc': product['TCC'],
                'tc': product['TC'],
                'f': product['F'],
                't': product['T'],
                'exp': product['EXP'],
                'ss': product['SS'],
                'rop': product['ROP']
            })
            ramalan_ids.append(res.id)

        return {
            "name": "Laporan Ramalan",
            "type": "ir.actions.act_window",
            "res_model": "ramalan",
            "views": [[False, "tree"], [False, "form"], [False, "graph"], [False,"pivot"]], 
            "domain": [["id", "in", ramalan_ids]],
        }


    # @api.model
    # def create(self, values):
        # Add code here

        
        # raise ValueError(productsArr)

        


# self memanggil model kosong

# values memanggil dictionari

# self.env['transaksi'].search([['tanggal' , '>=', values['tanggal_mulai']  ]])  

# fungsi self.env itu pindah pencarian di model lain dengan output dict

# [] lambang ini menandakan list
# {} lambang ini menandakan dictionerui key nilai


# ['field', 'operator', 'condition']