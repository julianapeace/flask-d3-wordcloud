from flask import Flask, render_template, jsonify
from nyt_api import most_popular_topics

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/headlines")
def headlines():
    data = most_popular_topics()
    return jsonify(data)


@app.route("/<name>")
def name(name):
    return render_template('name.html', name=name)

@app.route('/basic-form', methods=('GET', 'POST'))
#Flask-WTF is the library for forms
def submit():
    form = BasicForm(csrf_enabled=False)
    if form.validate_on_submit():
        return redirect('/'+ form.name.data)
    return render_template('basic-form.html', form=form)

app.run(debug=True)
