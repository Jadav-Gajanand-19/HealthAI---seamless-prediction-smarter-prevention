# app.py
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import pickle
import numpy as np
from models import db, User, HealthProfile

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Load ML models
diabetes_model = pickle.load(open('ML Models\diabetes_model.pkl', 'rb'))
heart_model = pickle.load(open('ML Models\heart_disease_model.pkl','rb'))
diseases_model = pickle.load(open('ML Models\diseases_model.pkl','rb'))

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    if User.query.filter_by(username=username).first():
        flash('Username already exists')
        return redirect(url_for('home'))
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect(url_for('profile_setup'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return redirect(url_for('dashboard'))
    flash('Invalid credentials')
    return redirect(url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/profile-setup', methods=['GET', 'POST'])
@login_required
def profile_setup():
    if request.method == 'POST':
        profile = HealthProfile(
            full_name=request.form.get('fullName'),
            age=int(request.form.get('age')),
            sex=request.form.get('sex'),
            height=float(request.form.get('height')),
            weight=float(request.form.get('weight')),
            user_id=current_user.id
        )
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('profile-setup.html')

@app.route('/predict_selection')
@login_required
def predict_selection():
    return render_template('prediction.html', user=current_user)

@app.route('/diabetes | Home')
@login_required
def diabetes_home():
    return render_template('diabetes.html')

@app.route('/diabetes | Prediction', methods=['GET', 'POST'])
@login_required
def diabetes_prediction():
    if request.method == 'POST':
        try:
            features = [float(x) for x in request.form.values()]
            final_input = [np.array(features)]
            risk_score = diabetes_model.predict(final_input)[0]
            risk_percent = int(risk_score * 100)
            result = "⚠️ Diabetic – Take precautions and consult your doctor." if risk_percent >= 50 else "✅ Not Diabetic – Stay healthy!"
            session['diabetes_result'] = result
            session['diabetes_risk'] = risk_percent
            return redirect(url_for('diabetes_result'))
        except Exception as e:
            session['diabetes_result'] = f"Error: {str(e)}"
            session['diabetes_risk'] = 0
            return redirect(url_for('diabetes_result'))

    return render_template('diabetes_prediction.html')

@app.route("/diabetes_result")
@login_required
def diabetes_result():
    result = session.get('diabetes_result')
    risk = session.get('diabetes_risk')
    if result is None or risk is None:
        return redirect(url_for('diabetes_home'))
    return render_template('diabetes_result.html', result=result, risk=risk)

@app.route("/heart | Home")
@login_required
def heart_home():
    return render_template('heart.html')

@app.route("/heart_prediction", methods=['GET', 'POST'])
@login_required
def heart_prediction():
    if request.method == 'POST':
        try:
            features = [float(x) for x in request.form.values()]
            final_input = [np.array(features)]
            risk_score = heart_model.predict_proba(final_input)[0][1]
            risk_percent = int(risk_score * 100)
            result = "⚠️ High Risk – You may be prone to heart disease." if risk_percent >= 50 else "✅ Low Risk – Unlikely to have heart disease."
            session['heart_result'] = result
            session['heart_risk'] = risk_percent
            return redirect(url_for('heart_result'))
        except Exception as e:
            session['heart_result'] = f"Error: {str(e)}"
            session['heart_risk'] = 0
            return redirect(url_for('heart_result'))

    return render_template('heart_prediction.html')

@app.route("/heart_result")
@login_required
def heart_result():
    result = session.get('heart_result')
    risk = session.get('heart_risk')
    if result is None or risk is None:
        return redirect(url_for('heart_prediction'))
    return render_template('heart_result.html', result=result, risk=risk)

@app.route("/multi_disease | Home")
@login_required
def multi_disease():
    return render_template("multi_disease.html")

@app.route("/multi_disease_form")
@login_required
def multi_disease_form():
    return render_template("multi_disease_prediction.html")

@app.route("/multi_disease_prediction", methods=["GET", "POST"])
@login_required
def multi_disease_prediction():
    if request.method == "GET":
        return redirect(url_for("multi_disease_form"))
    try:
        input_features = [float(x) for x in request.form.values()]
        final_input = np.array([input_features])
        prediction = diseases_model.predict(final_input)[0]
        label = {
            0: "Predicted Disease : Anemia",
            1: "Predicted Disease : Diabetes",
            2: "You are Fit and Healthy",
            3: "Predicted Disease : Thalasse",
            4: "Predicted Disease : Thromboc"
        }.get(prediction, f"Result: {prediction}")
        session['multi_disease_result'] = label
        return redirect(url_for("multi_disease_result"))
    except Exception as e:
        session['multi_disease_result'] = f"Error: {str(e)}"
        return redirect(url_for("multi_disease_result"))

@app.route("/multi_disease_result")
@login_required
def multi_disease_result():
    result = session.get("multi_disease_result")
    if result is None:
        return redirect(url_for("multi_disease_form"))
    return render_template("multi_disease_result.html", result=result)

@app.route('/Healthy habits')
@login_required
def healthy_habits():
    return render_template('healthy_habits.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
