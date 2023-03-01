from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('resume.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/blog')
def blog():
    return render_template('blog.html')

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Message sent!', category='success')
        return redirect(url_for('views.contact'))
    return render_template('contact.html')

@views.route('/interactive', methods=['GET', 'POST'])
def interactive():
    if request.method == 'POST':
        flash('Message sent!', category='success')
        return redirect(url_for('views.interactive'))
    return render_template('interactive.html')

@views.route('/resume',)
def resume():
    return render_template('resume.html')





