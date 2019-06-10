import logging
import yaml 
import pickle
import pandas as pd

def generate_score(model, input):
    """
    """

    score = model.predict_proba(input)
    score = score[0][1]
    # out = logistic.predict_proba(X_test)
    return score

if __name__ == "__main__":
    # Load configuration
    with open("config/config.yml","r") as yml:
        config = yaml.load(yml)
    config = config["score_model"]

    model = pickle.load( open( config["model_address"], "rb" ) )

    # data_address = config["data_address"]
    # if user_input == "":
    user_input = pd.DataFrame(data={ "Xdist":[30.0], "Ydist":[-5.0], "Stall":[4]})
    
    print(generate_score(model, user_input))
