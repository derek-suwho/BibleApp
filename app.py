from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///faithapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, User, Prayer, Devotional, Community, UserProfile, Church
db.init_app(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('dashboard.html')
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return render_template('register.html')
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    recent_prayers = Prayer.query.filter_by(user_id=current_user.id).order_by(Prayer.created_at.desc()).limit(5).all()
    today_devotional = Devotional.query.filter_by(date=datetime.now().date()).first()
    return render_template('dashboard.html', prayers=recent_prayers, devotional=today_devotional)

@app.route('/prayers')
@login_required
def prayers():
    user_prayers = Prayer.query.filter_by(user_id=current_user.id).order_by(Prayer.created_at.desc()).all()
    return render_template('prayers.html', prayers=user_prayers)

@app.route('/add_prayer', methods=['POST'])
@login_required
def add_prayer():
    title = request.form['title']
    content = request.form['content']
    prayer_type = request.form.get('prayer_type', 'personal')
    
    prayer = Prayer(
        title=title,
        content=content,
        prayer_type=prayer_type,
        user_id=current_user.id
    )
    db.session.add(prayer)
    db.session.commit()
    
    flash('Prayer added successfully')
    return redirect(url_for('prayers'))

@app.route('/devotional')
@login_required
def devotional():
    today_devotional = Devotional.query.filter_by(date=datetime.now().date()).first()
    if not today_devotional:
        # Fallback to most recent devotional
        today_devotional = Devotional.query.order_by(Devotional.date.desc()).first()
    return render_template('devotional.html', devotional=today_devotional)

@app.route('/mark_prayer_answered/<int:prayer_id>', methods=['POST'])
@login_required
def mark_prayer_answered(prayer_id):
    prayer = Prayer.query.get_or_404(prayer_id)
    if prayer.user_id != current_user.id:
        flash('Unauthorized action')
        return redirect(url_for('prayers'))
    
    prayer.is_answered = True
    prayer.answered_date = datetime.utcnow()
    prayer.answer_description = request.form.get('answer_description', '')
    db.session.commit()
    
    flash('Prayer marked as answered! Praise God!')
    return redirect(url_for('prayers'))

@app.route('/community')
@login_required
def community():
    nearby_users = User.query.filter(User.id != current_user.id).limit(10).all()
    communities = Community.query.all()
    return render_template('community.html', users=nearby_users, communities=communities)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user_profile = UserProfile.query.filter_by(user_id=current_user.id).first()
    
    if request.method == 'POST':
        if not user_profile:
            user_profile = UserProfile(user_id=current_user.id)
        
        user_profile.first_name = request.form.get('first_name')
        user_profile.last_name = request.form.get('last_name')
        user_profile.bio = request.form.get('bio')
        user_profile.church_name = request.form.get('church_name')
        user_profile.denomination = request.form.get('denomination')
        user_profile.favorite_verse = request.form.get('favorite_verse')
        user_profile.spiritual_gifts = request.form.get('spiritual_gifts')
        user_profile.ministry_interests = request.form.get('ministry_interests')
        user_profile.city = request.form.get('city')
        user_profile.state = request.form.get('state')
        user_profile.country = request.form.get('country')
        user_profile.availability_for_mentoring = 'availability_for_mentoring' in request.form
        user_profile.looking_for_mentor = 'looking_for_mentor' in request.form
        
        if not UserProfile.query.filter_by(user_id=current_user.id).first():
            db.session.add(user_profile)
        
        db.session.commit()
        flash('Profile updated successfully')
        return redirect(url_for('profile'))
    
    return render_template('profile.html', profile=user_profile)

@app.route('/churches')
@login_required 
def churches():
    local_churches = Church.query.all()
    return render_template('churches.html', churches=local_churches)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)