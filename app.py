from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/questions')
def loading_questions():
    """display the form to fill in"""
    words = silly_story.prompts 

    return render_template("questions.html",words = words)


