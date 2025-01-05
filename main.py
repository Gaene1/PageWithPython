from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class StringEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

# Initialize DB
@app.before_first_request
def init_db():
    db.create_all()

@app.route('/')
def index():
    entries = StringEntry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if request.method == 'POST':
        new_entry = request.form['text']
        entry = StringEntry(text=new_entry)
        db.session.add(entry)
        db.session.commit()
        update_git_repo()  # Call function to update the Git repository
        return redirect(url_for('index'))

# Function to commit and push changes to GitHub
def update_git_repo():
    # Ensure that the repo is in the correct directory
    os.chdir('/path/to/your/repo')
    
    # Git add, commit, and push
    subprocess.run(['git', 'add', 'database.db'])
    subprocess.run(['git', 'commit', '-m', 'Updated database'])
    subprocess.run(['git', 'push'])

if __name__ == '__main__':
    app.run(debug=True)