#!/usr/bin/env python

import re
import csv
import time

reader = csv.DictReader(open('csv_datos_ejemplo.csv'))

linea = '<?xml version="1.0" encoding="utf-8"?>\n'

linea = linea +'<openerp>\n'
linea = linea + '\t<data noupdate="1">\n'
l = 0

for r in reader:
    l=l+1

    linea = linea + '\t\t<record id="product_'+r["Clave"]+'" model="product.template">\n'
    
    linea = linea + '\t\t\t<field name="name">'+r["Nombre"]+'</field>\n'
    linea = linea + '\t\t\t<field name="categ_id" ref="product.product_category_1"/>\n'
    linea = linea + '\t\t\t<field name="type">product</field>\n'
    linea = linea + '\t\t\t<field name="list_price">'+r["Precio"]+'</field>\n'
    linea = linea + '\t\t\t<field name="standard_price">100.0</field>\n'
    linea = linea + '\t\t\t<field name="uom_id" ref="product.product_uom_unit"/>\n'
    linea = linea + '\t\t\t<field name="company_id" eval="[]"/>\n'
    linea = linea + '\t\t\t<field name="uom_po_id" ref="product.product_uom_unit"/>\n'
    linea = linea + '\t\t\t<field name="company_id" eval="[]"/>\n'

    linea = linea + '\t\t</record>\n'

    print 'linea '+str(l)+" - "+r["Nombre"]
    time.sleep(1)

linea = linea + '\t</data>\n'
linea = linea + '</openerp>'
ar2 = open("productos_ariel.xml",'w')
ar2.write(linea)
ar2.close()
linea = ''
