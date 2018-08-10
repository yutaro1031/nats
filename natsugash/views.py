from flask import request, redirect, url_for, render_template, flash
from natsugash import app


@app.route('/')
def show_top_page():
    return render_template('toppage.html')

@app.route('/main')
def show_main_page():
    return render_template('mainpage.html')

@app.route('/score')
def show_score_page():
    return render_template('scorepage.html')
