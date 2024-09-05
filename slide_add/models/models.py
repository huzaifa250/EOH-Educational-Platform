# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SlideAdd(models.Model):
    _inherit = 'slide.slide'
    _description = 'slide_add.slide_add'

    is_soft = fields.Boolean(default=True, string='Soft skills complete')
    gpa = fields.Char('GPA')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
