"""
Forms for the Job Application Tracker

This module contains the form definitions for the Job Application Tracker
using the Flask-WTF and WTForms libraries.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DateTimeField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Optional
from datetime import datetime

class ApplicationForm(FlaskForm):
    """
    Form for adding or editing a job application.

    Fields:
        date_applied (DateTimeField): The date the application was submitted.
        applicant_name (SelectField): The name of the applicant.
        industry (StringField): The industry of the job.
        company (StringField): The company the application was submitted to.
        location (StringField): The location of the job.
        job_description_link (StringField): The URL of the job description.
        resume_link (StringField): The URL of the applicant's resume.
        cover_letter_link (StringField): The URL of the applicant's cover letter.
        outcome (TextAreaField): The outcome of the application.
        prompt_details (TextAreaField): Additional details or prompts for the application.
        notes (TextAreaField): Notes related to the application.
        submit (SubmitField): The submit button for the form.
    """

    date_applied = DateField('Date Applied', validators=[DataRequired()])
    applicant_name = SelectField('Applicant Name', validators=[DataRequired()], choices=[])
    industry = StringField('Industry')
    company = StringField('Company', validators=[DataRequired()])
    location = StringField('Location')
    job_description_link = StringField('Job Description Link', validators=[Optional(), URL()])
    resume_link = StringField('Resume Link', validators=[Optional(), URL()])
    cover_letter_link = StringField('Cover Letter Link', validators=[Optional(), URL()])
    outcome = TextAreaField('Outcome')
    prompt_details = TextAreaField('Prompt Details')
    notes = TextAreaField('Notes')
    submit = SubmitField('Submit')
