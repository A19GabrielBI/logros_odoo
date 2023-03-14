# -*- coding: utf-8 -*-

from odoo import models, fields, api


class logros_odoo(models.Model):
    _name = 'logros_odoo.logros_odoo'
    _description = 'logros_odoo.logros_odoo'

    nombre = fields.Char(string="Nombre", required=True)
    imagen = fields.Binary(string="Imagen")
    descripcion = fields.Text(string="Descripcion", required=True)
    categoria =  fields.Char(string="Categoria", required=True)

    def name_get(self):
        result = []
        for record in self:
            name = record.nombre + " (" + record.categoria + ")"
            result.append((record.id, name))
        return result

class empleado_logro(models.Model):
    _name='empleado.logro'
    _description='empleado.logro'

    nombre = fields.Many2one('logros_odoo.logros_odoo', string="Logro")
    fecha_evento = fields.Datetime(string="Fecha logro", default=fields.datetime.now(), required=True)
    name = fields.Many2one('hr.employee', string="Empleado")
    resultado = fields.Selection([("bronce", "Bronce"),("plata", "Plata"),("oro", "Oro")], required=True, string="Nivel")

    def name_get(self):
        result = []
        for record in self:
            name = record.nombre
            result.append((record.id, name))
        return result