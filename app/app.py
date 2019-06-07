import flask
import pickle
import os
import yaml

# os.chdir("../src")
from src.score_model import generate_score

# os.chdir("../app")

with open("../config/config.yml","r") as yml:
    config = yaml.load(yml)
config = config["app"]

with open( config["model_address"], "rb" ) as file:
    model = pickle.load(file)

app = flask.Flask(__name__, template_folder='templates')
@app.route('/')

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        temperature = flask.request.form['temperature']
        humidity = flask.request.form['humidity']
        windspeed = flask.request.form['windspeed']
    
if __name__ == '__main__':
    with open("../config/hwconfig.yml","r") as yml:
        config = yaml.load(yml)
    config = config["app"]
    app.run()

    