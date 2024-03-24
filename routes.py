from flask import render_template, url_for, flash, redirect, request
from cdk import app, db, bcrypt
from cdk.forms import LoginForm, Register, Predict
from cdk.models import User
from base64 import b64encode, b64decode
from flask_login import login_user, current_user, logout_user#, login_required
import secrets
import os
from functools import wraps
from werkzeug.utils import secure_filename
from flask import Markup
import datetime

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):

            if not current_user.is_authenticated:
               return app.login_manager.unauthorized()
            urole = current_user.role
            if ( (urole != role) and (role != "ANY")):
                return app.login_manager.unauthorized()      
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

@app.route("/")
@app.route("/home")
def home():
    return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
#try:
    db.create_all()
    db.session.commit()
    #Run this for first time setup - to create the admin account
    '''
    try: #if admin is not created it will create | if already created it will throw the errors  
        user_info = User(
                        first_name = 'admin',
                        last_name = 'admin',
                        email = 'admin@admin.com',
                        password = bcrypt.generate_password_hash('admin'),
                        phone = 'admin',
                        address = 'admin',
                        ms = 'currently in happy searching...',
                        role = 'Admin',
                    )
        db.session.add(user_info)
        db.session.commit()
    except:
        pass
    '''
    print("Setting")

    #except Exception as e:
        #print(e)
        #user = User.query.filter_by(email='admin@admin.com').first()
        #print('user', user)
        #print("DD is Set")

    if current_user.is_authenticated:
        print("current_user", current_user, type(current_user), current_user.email)
        if current_user.role == 'Admin':
            return redirect(url_for('atomadmin'))
        elif current_user.role == 'Doctor':
            return redirect(url_for('doctor'))
        else:
            return redirect(url_for('patient'))

    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        user = User.query.filter_by(email=form.email.data).first()
        print('user', user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            print("Login Success", user)
            next_page = request.args.get('next')
            if current_user.role == 'Admin':
                return redirect(next_page) if next_page else redirect(url_for('atomadmin'))
            elif current_user.role == 'Doctor':
                return redirect(next_page) if next_page else redirect(url_for('doctor'))
            else:
                return redirect(next_page) if next_page else redirect(url_for('patient'))
            #return redirect(url_for('user_operation'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/atomadmin", methods=['GET', 'POST'])
@login_required(role="Admin")
def atomadmin():
    form = Register()
    if form.validate_on_submit():
        print(form.role.data, type(form.role.data))
        print(bcrypt.generate_password_hash(form.password.data))
        user_info = User(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                email = form.email.data,
                password = bcrypt.generate_password_hash(form.password.data),
                phone = form.phone.data,
                address = form.address.data,
                ms = form.ms.data,
                role = form.role.data,
            )
        print('u_i', user_info)
        db.session.add(user_info)
        db.session.commit()
        flash('Account is Registered', 'success')
        return redirect(url_for('atomadmin'))

    home_links = [
                Markup('''<a class="nav-item nav-link" href="/logout">Logout</a>'''),                    
    ]
    return render_template('admin.html', form=form, home_links=home_links)

@app.route("/doctor", methods=['GET', 'POST'])
@login_required(role="Doctor")
def doctor():
    form = Predict()
    if form.validate_on_submit():

        output, filename = pre(form.Age.data,
            form.BloopPressure.data,
            form.SpecificGravity.data,
            form.Albumin.data,
            form.Sugar.data,
            form.RBC.data,
            form.Pus_Cell.data,
            form.Pus_Cell_Clump.data,
            form.Bacteria.data,
            form.Blood_Glucose_Random.data,
            form.Blood_Urea.data,
            form.Serum_Creatinine.data,
            form.Sodium.data,
            form.Potassium.data,
            form.Hemoglobin.data,
            form.Packed_Cell_Volume.data,
            form.WBC_Count.data,
            form.RBC_Count.data,
            form.HyperTension.data,
            form.Diabetes_Mellitus.data,
            form.Cor_Art_Dis.data,
            form.Appetite.data,
            form.Pedal_Edema.data,
            form.Anemia.data
            )

        home_links = [
                    Markup('''<a class="nav-item nav-link" href="/logout">Logout</a>'''),                    
        ]
        return render_template('predict.html', form=form, home_links=home_links, output=output, filename=filename)

    home_links = [
                Markup('''<a class="nav-item nav-link" href="/logout">Logout</a>'''),                    
    ]
    return render_template('predict.html', form=form, home_links=home_links, )

@app.route("/patient", methods=['GET', 'POST'])
@login_required(role="Patient")
def patient(): 
    form = Predict()
    if form.validate_on_submit():
        output, filename = pre(form.Age.data,
            form.BloodPressure.data,
            form.SpecificGravity.data,
            form.Albumin.data,
            form.Sugar.data,
            form.RBC.data,
            form.Pus_Cell.data,
            form.Pus_Cell_Clump.data,
            form.Bacteria.data,
            form.Blood_Glucose_Random.data,
            form.Blood_Urea.data,
            form.Serum_Creatinine.data,
            form.Sodium.data,
            form.Potassium.data,
            form.Hemoglobin.data,
            form.Packed_Cell_Volume.data,
            form.WBC_Count.data,
            form.RBC_Count.data,
            form.HyperTension.data,
            form.Diabetes_Mellitus.data,
            form.Cor_Art_Dis.data,
            form.Appetite.data,
            form.Pedal_Edema.data,
            form.Anemia.data
            )
        home_links = [
                    Markup('''<a class="nav-item nav-link" href="/logout">Logout</a>'''),
        ]
        return render_template('predict.html', form=form, home_links=home_links, output=output, filename=filename)
 
    home_links = [
                Markup('''<a class="nav-item nav-link" href="/logout">Logout</a>'''),
    ]

    return render_template('predict.html', form=form, home_links=home_links)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


def pre(age, BloodPressure, Sugar, SpecificGravity, Albumin, Bacteria, RBC, Pus_Cell, Pus_Cell_Clump, Blood_Glucose_Random
    , Blood_Urea, Serum_Creatinine, Sodium, Potassium, Hemoglobin, Packed_Cell_Volume, WBC_Count, RBC_Count, HyperTension
    , Diabetes_Mellitus, Cor_Art_Dis, Appetite, Pedal_Edema, Anemia):
    
    if(RBC=="normal"):
        RBC = 1
    else:
        RBC = 0

    if(Pus_Cell=="normal"):
        Pus_Cell = 1
    else:
        Pus_Cell = 0

    if(Pus_Cell_Clump=="present"):
        Pus_Cell_Clump = 1
    else:
        Pus_Cell_Clump = 0

    if(Bacteria=="present"):
        Bacteria = 1
    else:
        Bacteria = 0

    if(HyperTension=="yes"):
        HyperTension = 1
    else:
        HyperTension = 0

    if(Diabetes_Mellitus=="yes"):
        Diabetes_Mellitus = 1
    else:
        Diabetes_Mellitus = 0

    if(Cor_Art_Dis=="yes"):
        Cor_Art_Dis = 1
    else:
        Cor_Art_Dis = 0

    if(Appetite=="good"):
        Appetite = 0
    else:
        Appetite = 1

    if(Pedal_Edema=="yes"):
        Pedal_Edema = 1
    else:
        Pedal_Edema = 0

    if(Anemia=="yes"):
        Anemia = 1
    else:
        Anemia = 0

    age = float(age)
    BloodPressure = float(BloodPressure)
    SpecificGravity = float(SpecificGravity)
    Albumin = float(Albumin)
    Sugar = float(Sugar)
    Blood_Glucose_Random = float(Blood_Glucose_Random)
    Blood_Urea = float(Blood_Urea)
    Serum_Creatinine = float(Serum_Creatinine)
    Sodium = float(Sodium)
    Potassium = float(Potassium)
    Hemoglobin = float(Hemoglobin)
    Packed_Cell_Volume = float(Packed_Cell_Volume)
    WBC_Count = float(WBC_Count)
    RBC_Count = float(RBC_Count)

    import pandas as pd
    from collections import Counter
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import GridSearchCV
    import numpy as np
    from matplotlib import pyplot as plt
    import joblib
    from sklearn.model_selection import StratifiedKFold
    from sklearn.naive_bayes import MultinomialNB
    import pickle
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import SGDClassifier
    from sklearn import metrics
    import sklearn.neighbors._base

    print('osssss', os.listdir())
    lr = joblib.load("cdk/static/models/lr1.0.joblib")
    svm = joblib.load("cdk/static/models/svm1.0.joblib")
    #rf = joblib.load("cdk/static/models/rf1.0.joblib")
    #knn = joblib.load("cdk/static/models/knn1.0.joblib")
    sgd = joblib.load("cdk/static/models/sgd1.0.joblib")
    with open ("cdk/static/models/scaler.pkl", "rb") as f:
      scaler = pickle.load(f)

    t = [age, BloodPressure, SpecificGravity, Albumin, RBC, Pus_Cell, Pus_Cell_Clump, Bacteria, Blood_Glucose_Random
    , Blood_Urea, Serum_Creatinine, Sodium, Potassium, Hemoglobin, Packed_Cell_Volume, WBC_Count, RBC_Count, HyperTension
    , Diabetes_Mellitus, Cor_Art_Dis, Appetite, Pedal_Edema, Anemia]

    scaled_X = scaler.transform([t])

    lr_val = lr.predict_proba(scaled_X)
    #svm_val = svm.predict_proba(scaled_X)
    #rf_val = rf.predict_proba(scaled_X)
    #knn_val = knn.predict_proba(scaled_X)
    sgd_val = sgd.predict_proba(scaled_X)

    #output = (lr_val+svm_val+rf_val+knn_val+sgd_val)/5
    output = (lr_val+sgd_val)/2
    output = output[0]

    #plt.figure(figsize = (3, 3))
    lab = ['cdk', 'not cdk']
    y_pos = np.arange(len(lab))
    plt.barh(y_pos,output)
    plt.yticks(y_pos,lab)
    plt.title('Chronic kidney disease Prediction')
    plt.ylabel('Labels')
    plt.xlabel('Percentage')
    a = datetime.datetime.now()
    filename = str(a.hour)+"_"+str(a.minute)+".png"
    plt.savefig("cdk/static/images/output_"+filename)

    output = np.argmax(output)
    if(output==0):
        output = "cdk"
    else:
        output = "notcdk"
    return(output, "/static/images/output_"+filename)