from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/static_files')
def static_files():
    static_dir = os.path.join(app.root_path, 'static')
    static_files = []
    
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            file_path = os.path.join(root, file)
            static_files.append(file_path)
    
    return render_template('static_files.html', static_files=static_files)



