from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectMultipleField, widgets, HiddenField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#from wtforms import validators
from cdk.models import User
from cdk.models import User
from cdk import db
from wtforms_validators import AlphaNumeric
from flask import render_template, url_for, flash, redirect, request
import random
import inspect

 
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class Register(FlaskForm):
    role = SelectField('Role', choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])    
    phone = StringField('Phone No.', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    ms = SelectField('Married Status', choices=[('Married', 'Married'), ('Not Married', 'Not Married')], validators=[DataRequired()])
    submit = SubmitField('Register')

class Predict(FlaskForm):

    Age = StringField('Age', validators=[DataRequired()])
    BloodPressure = StringField('BloodPressure', validators=[DataRequired()])
    SpecificGravity = StringField('Specific Gravity', validators=[DataRequired()])
    Albumin = StringField('Albumin', validators=[DataRequired()])
    Sugar = StringField('Sugar', validators=[DataRequired()])
    RBC = SelectField('RBC', choices=[('normal', 'normal'), ('abnormal', 'abnormal')], validators=[DataRequired()])
    Pus_Cell = SelectField('Pus Cell', choices=[('normal', 'normal'), ('abnormal', 'abnormal')], validators=[DataRequired()])
    Pus_Cell_Clump = SelectField('Pus Cell Clump', choices=[('present', 'present'), ('notpresent', 'notpresent')], validators=[DataRequired()])
    Bacteria = SelectField('Bacteria', choices=[('present', 'present'), ('notpresent', 'notpresent')], validators=[DataRequired()])
    Blood_Glucose_Random = StringField('Blood Glucose Random', validators=[DataRequired()])
    Blood_Urea = StringField('Blood Urea', validators=[DataRequired()])
    Serum_Creatinine = StringField('Serum Creatinine', validators=[DataRequired()])
    Sodium = StringField('Sodium', validators=[DataRequired()])
    Potassium = StringField('Potassium', validators=[DataRequired()])
    Hemoglobin = StringField('Hemoglobin', validators=[DataRequired()])
    Packed_Cell_Volume = StringField('Packed Cell Volume', validators=[DataRequired()])
    WBC_Count = StringField('WBC Count', validators=[DataRequired()])
    RBC_Count = StringField('RBC Count', validators=[DataRequired()])
    HyperTension = SelectField('HyperTension', choices=[('yes', 'yes'), ('no', 'no')], validators=[DataRequired()])
    Diabetes_Mellitus = SelectField('Diabetes Mellitus', choices=[('yes', 'yes'), ('no', 'no')], validators=[DataRequired()])
    Cor_Art_Dis = SelectField('Cor Art Dis', choices=[('yes', 'yes'), ('no', 'no')], validators=[DataRequired()])
    Appetite = SelectField('Appetite', choices=[('good', 'good'), ('poor', 'poor')], validators=[DataRequired()])
    Pedal_Edema = SelectField('Pedal Edema', choices=[('yes', 'yes'), ('no', 'no')], validators=[DataRequired()])
    Anemia = SelectField('Anemia', choices=[('yes', 'yes'), ('no', 'no')], validators=[DataRequired()])
    submit = SubmitField('Predict')

