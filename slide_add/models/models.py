# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SlideAdd(models.Model):
    _inherit = 'slide.slide'
    _description = 'Course with required skills'

    is_soft = fields.Boolean(default=True, string='Soft skills complete')
    
    # Modified GPA field with a minimum value constraint
    gpa = fields.Float('GPA', digits=(4, 2), help="Enter the GPA (out of 4.00).")

    @api.constrains('gpa')
    def _check_gpa(self):
        # Check GPA must not be less than 2.5
        for record in self:
            if record.gpa < 2.50:
                raise ValidationError(_("GPA must be 2.50 or higher!"))
