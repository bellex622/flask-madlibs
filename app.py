from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/questions')
def show_prompts():
    """display the form to fill in"""
    words = silly_story.prompts

    return render_template("questions.html",words = words)


@app.get('/results')
def display_story():
    """display the form to fill in"""
    answers = request.args.to_dict()

    print("ANSWERS >>>>", answers)

    story = silly_story.get_result_text(answers)

    return render_template("results.html", story = story)


