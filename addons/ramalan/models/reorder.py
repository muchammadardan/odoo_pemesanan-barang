from odoo import api, fields, models 

class Reorder(models.Model):
    _name = 'reorder'
    _description = 'Model Reorder Barang'
    _check_company_auto = True
    _rec_name = 'no'
    _order = 'no asc'

    no = fields.Char(string='No', readonly=True)
    tanggal = fields.Date(string='Tanggal')

    barang_ids = fields.One2many(comodel_name='reorder.data', inverse_name='reorder_id', string='Barang')

    

    sub_total = fields.Integer(string='Total', compute='_compute_total')
    
    
    # validasi = fields.Selection(string='Status', selection=[('draft','Draft'),('order', 'Order'), ('cancel', 'Cancel'),], default='draft')
    
    # status = fields.Char(string='Status')
    
    validasi = fields.Selection(string='Status',selection=
    [('draft','Simpan'),
    ('order', 'Terima'), 
    ('cancel', 'Batal')]
    , default='draft')
    active = fields.Boolean(string='Active', default=True)



    _sql_constraints = [
        ('unique_code_company_id', 'unique(code,company_id)',
        ('This Code already exist!')),
    ]

    @api.model
    def create(self, values):
        # Add code here
        values['no']=self.env['ir.sequence'].next_by_code('reorder')
        return super(Reorder, self).create(values)

    def draft_progressbar(self):
        self.write({
            'validasi':'draft'
        })

    def order_progressbar(self):
        self.write({
            'validasi':'order'
        })

    def cancel_progressbar(self):
        self.write({
            'validasi':'cancel'
        })
    
    @api.depends('sub_total')
    def _compute_total(self):
        for rec in self:
            rec.sub_total = sum(rec.mapped('barang_ids.jumlah'))



    
