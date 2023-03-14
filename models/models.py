# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re

class logros_odoo(models.Model):
    _name = 'logros_odoo.logros_odoo'
    _description = 'logros_odoo.logros_odoo'

    nombre = fields.Char(string="Nombre", required=True)
    imagen = fields.Binary(string="Icono")
    descripcion = fields.Text(string="Descripcion", required=True)
    categoria =  fields.Char(string="Categoria", required=True)

    _sql_constraints = [
        ('nombre_categoria_unicos', 'unique(nombre, categoria)', 'Este logro ya está definido con la misma categoria.')
    ]

    def name_get(self):
        result = []
        for record in self:
            name = record.nombre + " (" + record.categoria + ")"
            result.append((record.id, name))
        return result

class empleado_logro(models.Model):
    _name='empleado.logro'
    _description='empleado.logro'

    nombre = fields.Many2one('logros_odoo.logros_odoo', string="Logro", required=True)
    fecha_evento = fields.Datetime(string="Fecha logro", default=fields.datetime.now(), required=True)
    name = fields.Many2one('hr.employee', string="Empleado", required=True)
    informacion_extra = fields.Char(string="Información")

    imagen_logro = fields.Binary(string="Icono", compute='_compute_imagen_logro')
    @api.depends('nombre')
    def _compute_imagen_logro(self):
        for record in self:
            if record.nombre and record.nombre.imagen:
                record.imagen_logro = record.nombre.imagen
            else:
                record.imagen_logro = False

    def name_get(self):
        result = []
        for record in self:
            name = record.nombre
            result.append((record.id, name))
        return result

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
	
    logros_history = fields.One2many('empleado.logro', 'name', string="Historial")
