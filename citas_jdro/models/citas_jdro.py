# -*- coding: utf-8 -*- 
from odoo import api, fields, models 
from datetime import datetime 

class citas_jdro(models.Model): 
    _name = 'citas_jdro' 
    autor = fields.Char(string='autor', required=True) 
 
    cita = fields.Text(string='cita', required=True) 
 
    fecha_visualizacion = fields.Datetime(string='Fecha de visualizacion', required=True) 
 
    orden_visualizacion = fields.Integer(string='Orden de visualizacion', required=True) 
 
