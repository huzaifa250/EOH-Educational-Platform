# -*- coding: utf-8 -*-
from odoo import http


class ElearningController(http.Controller):
    @http.route('/slides/courses', auth='public', website=True)
    def get_courses(self, **kwargs):
        # get all the courses from the eLearning model
        courses = http.request.env['slide.channel'].sudo().search([])
        # Pass courses data to the template
        return http.request.render('slide_add.elearning_courses_template', {
            'my_courses': courses
        })
