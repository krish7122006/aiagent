from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    skills = request.form['skills']
    photo = request.files['photo']

    photo.save(os.path.join(UPLOAD_FOLDER, photo.filename))  # Save uploaded photo

    return f"<h1>Details submitted:</h1><p>Name: {name}</p><p>Age: {age}</p><p>Skills: {skills}</p><p>Photo saved as: {photo.filename}</p>"

if __name__ == '__main__':
    app.run(debug=True)
