from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Resource, Api, reqparse
from candidate import Candidate

app = Flask(__name__)

CANDIDATES = []


@app.route('/')
def root():
    return redirect(url_for("index"))


@app.route('/candidates', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        new_candidate = Candidate(
            request.form['cnc-c-name-input'], request.form['cnc-c-age-input'], request.form['cnc-c-language-input'])
        CANDIDATES.append(new_candidate)
        print(new_candidate)
        return redirect(url_for("index"))

    return render_template('index.html', Candidate=CANDIDATES)


if __name__ == "__main__":

    app.run(debug=True, port=3000)
