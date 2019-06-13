import flask
import pickle
import os
import yaml
import pandas as pd
import sklearn

# os.chdir("../src")
from src.score_model import generate_score
from src.postprocess import store_data

# os.chdir("../")

with open("config/config.yml","r") as yml:
    config = yaml.load(yml)
config = config["app"]

with open( config["model_address"], "rb" ) as file:
    model = pickle.load(file)

app = flask.Flask(__name__, template_folder='templates')

# app.config.from_pyfile("flask_config.py")
# print(app.config["HOST"])

@app.route('/', methods=['GET', 'POST'])

def main():
    # app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        Xdist = flask.request.form["Xdist"]
        Ydist = flask.request.form["Ydist"]
        Stall = flask.request.form["Stall"]

        input_variables = pd.DataFrame([[Xdist, Ydist, Stall]],
                                       columns=["Xdist", "Ydist", "Stall"],
                                       dtype=float)
        
        # prediction = model.predict_proba(input_variables)
        
        output = generate_score(model, input_variables) #prediction[0][1]

        data_to_save = input_variables.assign(prediction=[output])

        store_data(data_to_save)

        return flask.render_template('main.html',
                                     original_input={"Xdist":Xdist,
                                                     "Ydist":Ydist,
                                                     "Stall":Stall},
                                     result=output,
                                     )
    
if __name__ == '__main__':
    # with open("config/hwconfig.yml","r") as yml:
    #     config = yaml.load(yml)
    # config = config["app"]
    app.run()

    