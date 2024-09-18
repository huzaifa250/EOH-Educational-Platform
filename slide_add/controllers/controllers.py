# -*- coding: utf-8 -*-
from odoo import http


class ElearningController(http.Controller):
    @http.route('/slides/courses', auth='public', website=True)
    def get_courses(self, **kwargs):
        # get all the courses from the eLearning model
        courses = http.request.env['slide.channel'].sudo().search([])
        # Check if no courses are found
        if not courses:
            # Render a template for no courses or pass a message to the existing template
            return http.request.render('slide_add.elearning_courses_template', {
                'my_courses': [],
                'error_message': 'No courses available at the moment.'
            })

        # if courses are found pass courses data to the template
        return http.request.render('slide_add.elearning_courses_template', {
            'my_courses': courses,
            'error_message': False  # No error, so no message
        })

