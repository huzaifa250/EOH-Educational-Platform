# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
from odoo.exceptions import ValidationError
from odoo import _

_logger = logging.getLogger(__name__)


class ElearningController(http.Controller):
    @http.route('/courses', auth='public', website=True)
    def list_courses(self, **kwargs):
        # get all the courses from the eLearning model
        courses = request.env['slide.channel'].sudo().search([])
        # Check if no courses are found
        if not courses:
            # Render a template for no courses or pass a message to the existing template
            return request.render('slide_add.elearning_courses_template', {
                'my_courses': [],
                'error_message': 'No courses available at the moment.'
            })

        # if courses are found pass courses data to the template
        return request.render('slide_add.elearning_courses_template', {
            'my_courses': courses,
            'error_message': False  # No error, so no message
        })

    # Route for the course creation form page
    @http.route('/new/course', type='http', auth='public', website=True, csrf=True)
    def create_course_form(self, **kwargs):
        return request.render("slide_add.elearning_create_submit_course_temp")

    # Route to handle form submission for creating a new course
    @http.route('/submit/course', auth='public', website=True, csrf=True)
    def submit_course(self, **kwargs):
        # allow users to create course
        name = kwargs.get('course_name')
        description = kwargs.get('description')  # optional
        # responsible_user = kwargs.get('user_id')
        # Log the received data
        _logger.info(
            f"Received data: course_name={name}, description={description}")
        # Check if the course name is provided
        # course = request.env['slide.channel'].sudo().search([()])
        # if course_name:
        #     raise ValidationError(_("Course Not Available !!"))
        course = request.env['slide.channel'].sudo().create(
            {'name': name,
             'description': description or '',
             })
        # print("Name is *************** ", name)
        _logger.info(f"Course created: {course}")
        # _logger.error(f"Error creating course:")
        # Redirect or render a success page after creation
        return request.redirect('/courses')
