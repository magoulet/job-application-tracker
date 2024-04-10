"""
Job Application Tracker

This module contains the Flask application for the Job Application Tracker.
It handles the routing, database connections, and form processing.
"""

import os
from copy import deepcopy
from datetime import datetime
import yaml

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL
from bson.objectid import ObjectId
from pymongo import MongoClient

from forms import ApplicationForm


# Load applicant names from YAML file
applicant_names_data = yaml.load(open("config/applicant_names.yml"), Loader=yaml.FullLoader)
APPLICANT_NAMES = applicant_names_data['applicant_names'] 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
bootstrap = Bootstrap(app)

# MongoDB connection
mongo_uri = os.environ.get('MONGO_URI')
client = MongoClient(mongo_uri)
db = client.job_applications

db = client.job_applications

@app.route('/', methods=('GET', 'POST'))
def index():
    applications = list(db.applications.find({}, {'_id': 0}))
    return render_template('index.html', applications=applications)

@app.route('/add', methods=['GET', 'POST'])
def add_application():
    form = ApplicationForm()
    form.applicant_name.choices = [(name, name) for name in APPLICANT_NAMES]
    form.applicant_name.delete_one = APPLICANT_NAMES[0]
    if form.validate_on_submit():
        application = {
            'application_id': str(ObjectId()),
            # 'date_applied': form.date_applied.data,
            'date_applied': datetime.combine(form.date_applied.data, datetime.min.time()),
            'applicant_name': form.applicant_name.data,
            'industry': form.industry.data,
            'company': form.company.data,
            'location': form.location.data,
            'job_description_link': form.job_description_link.data,
            'resume_link': form.resume_link.data,
            'cover_letter_link': form.cover_letter_link.data,
            'outcome': form.outcome.data,
            'prompt_details': form.prompt_details.data,
            'notes': form.notes.data
        }
        db.applications.insert_one(application)
        return redirect(url_for('index'))
    return render_template('add_application.html', form=form)

@app.route('/edit/<application_id>', methods=['GET', 'POST'])
def edit_application(application_id):
    application = db.applications.find_one({'application_id': application_id})
    form = ApplicationForm(data=application)
    form.applicant_name.choices = [(name, name) for name in APPLICANT_NAMES]
    if form.validate_on_submit():
        updated_application = {
            'date_applied': datetime.combine(form.date_applied.data, datetime.min.time()),
            'applicant_name': form.applicant_name.data,
            'industry': form.industry.data,
            'company': form.company.data,
            'location': form.location.data,
            'job_description_link': form.job_description_link.data,
            'resume_link': form.resume_link.data,
            'cover_letter_link': form.cover_letter_link.data,
            'outcome': form.outcome.data,
            'prompt_details': form.prompt_details.data,
            'notes': form.notes.data
        }
        db.applications.update_one({'application_id': application_id}, {'$set': updated_application})
        return redirect(url_for('index'))
    return render_template('edit_application.html', form=form, application=application)

@app.route('/copy/<application_id>', methods=['GET'])
def copy_application(application_id):
    original_application = db.applications.find_one({'application_id': application_id})
    if original_application:
        new_application = deepcopy(original_application)
        new_application['application_id'] = str(ObjectId())
        new_application.pop('_id')
        db.applications.insert_one(new_application)
    return redirect(url_for('index'))

@app.route('/delete/<application_id>', methods=['GET'])
def delete_application(application_id):
    db.applications.delete_one({'application_id': application_id})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)