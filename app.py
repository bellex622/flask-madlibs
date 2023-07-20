from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def choose_template():
    




@app.get('/questions')
def show_prompts():
    """Shows form allowing user to input madlib answers"""

    prompts = Story.prompts

    return render_template("questions.html", prompts=prompts)


@app.get('/results')
def display_story():
    """Displays completed madlib story"""

    answers = request.args

    print("ANSWERS >>>>", answers)

    story = Story.get_result_text(answers)

    return render_template("results.html", story=story)


