# -*- encoding: utf-8 -*-
# Author=Nhomar Hernandez nhomar@vauxoo.com
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from osv import osv
from osv import fields
from tools.translate import _


class import_info(osv.osv):
    _name = "import.info"
    _description = "Information about customs"
    _order = 'name asc'
    _columns = {
        'name' : fields.char('Number of Operation',15, required=True, 
                help="Transaction Number of tramit Information"),
        'customs' : fields.char('Aduana',64, help="Customs House product came in to contry where"),
        'date':fields.date('Fecha', help="Date of Custom and Import Information (In Document)"),
        'lot_id' : fields.many2one('stock.production.lot','pedimento'),
        'rate': fields.float('Exchange Rate', required=True, digits=(16, 4), 
                help='Exchange rate informed on Custom House when the transaction was approved'),
        'company_id':fields.many2one('res.company', 'Company', required=True, 
                                    help="Company related to this document."),
        'invoice_ids':fields.many2many('account.invoice', 'account_invoice_rel', 
                                        'import_id', 'invoice_id',
                                        'Invoices Related'),
    }


import_info()

