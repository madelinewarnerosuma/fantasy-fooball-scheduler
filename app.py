# -*- coding: utf-8 -*-

import flask
from flask import request, render_template
from flask.typing import ResponseReturnValue

app = flask.Flask(__name__)


@app.route("/scheduler/twelve_teams")
def get_input_twelve_team():
    return render_template("src/templates/twelve_team_input.html")


@app.route("/scheduler/schedule_twelve_teams", methods=["POST"])
def create_schedule():
    form_input_data = {
        "division_one": {
            "team_one": request.form["div_one_team_one"],
            "team_two": request.form["div_one_team_two"],
            "team_three": request.form["div_one_team_three"],
            "team_four": request.form["div_one_team_four"]
        },
        "division_two": {
            "team_one": request.form["div_one_team_one"],
            "team_two": request.form["div_one_team_two"],
            "team_three": request.form["div_one_team_three"],
            "team_four": request.form["div_one_team_four"]
        },
        "divison_three": {
            "team_one": request.form["div_one_team_one"],
            "team_two": request.form["div_one_team_two"],
            "team_three": request.form["div_one_team_three"],
            "team_four": request.form["div_one_team_four"]
        }
    }
    # TODO: create a schedule
    return render_template("src/templates/twelve_team_schedule.html")



#TODO: Make this into a Flask app with an exposed endpoint that takes in the teams per division and returns the schedule
# Step 1: Set up app.py to receieve a POST with the names
# Step 2: Update schedulecreator.py to take in that type of input
# Step 3: Clean up the schedule creator - make into classes, use iterators, what have you
#    Mid-step: Get into the logic of this. Does it need to be perscriptive, or could we build in randomness?
# Step 4: write tests for schedulecreator, depending on logic used
# Step 4: Set up Dockerfile and spin up instance, test in postman
# Step 5: Test Dockerfile
# Step 6: Set up a basic HTML template that can take the inputs in a web page (use this example https://github.com/lvthillo/python-flask-docker/blob/master/src/templates/index.html)
# Step 7: Test Deployment!


#TODO: Bonus steps:
# Update this to take in any number of teams?
# Create another repo with a basic react app instead of the templates & figure out how to get these to work together! (look at Series stuff)
