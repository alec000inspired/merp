# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from . import models

from odoo import api, SUPERUSER_ID

def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})

    sql = '''
    CREATE TABLE product_product_stock_picking_rel (
    stock_picking_id INTEGER NOT NULL,
    product_product_id INTEGER NOT NULL,
    CONSTRAINT product_product_stock_picking_rel_pk PRIMARY KEY (stock_picking_id, product_product_id),
    CONSTRAINT product_product_stock_picking_rel_stock_picking_id_fkey FOREIGN KEY (stock_picking_id)
        REFERENCES stock_picking (id) MATCH SIMPLE
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT product_product_stock_picking_rel_product_product_id_fkey FOREIGN KEY (product_product_id)
        REFERENCES product_product (id) MATCH SIMPLE
        ON UPDATE CASCADE ON DELETE CASCADE
    )
    '''
    env.cr.execute(sql)
