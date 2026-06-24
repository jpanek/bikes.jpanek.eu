# app.py

from flask import Flask, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return redirect(url_for('lang_index', lang='en'))

@app.route('/<lang>/')
def lang_index(lang):
    return render_template(f'{lang}/index.html', lang=lang)

@app.route('/<lang>/services/')
def lang_services(lang):
    return render_template(f'{lang}/services.html', lang=lang)

@app.route('/<lang>/contact/')
def lang_contact(lang):
    return render_template(f'{lang}/contact.html', lang=lang)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)