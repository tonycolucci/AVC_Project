import flask
import pickle
import os
import yaml
import pandas as pd

# os.chdir("../src")
from src.score_model import generate_score

# os.chdir("../app")

with open("../config/config.yml","r") as yml:
    config = yaml.load(yml)
config = config["app"]

with open( config["model_address"], "rb" ) as file:
    model = pickle.load(file)

app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        Xdist = flask.request.form["Xdist"]
        Ydist = flask.request.form["Ydist"]
        Stall = flask.request.form["Stall"]

        input_variables = pd.DataFrame([[Xdist, Ydist, Stall]],
                                       columns=["Xdist", "Ydist", "Stall"],
                                       dtype=float)
        
        prediction = model.predict_proba(input_variables)
        output = prediction[0][1]

        return flask.render_template('main.html',
                                     original_input={"Xdist":Xdist,
                                                     "Ydist":Ydist,
                                                     "Stall":Stall},
                                     result=output,
                                     )
    
if __name__ == '__main__':
    with open("../config/hwconfig.yml","r") as yml:
        config = yaml.load(yml)
    config = config["app"]
    app.run()

    