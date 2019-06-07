import logging
import yaml 
import pickle
import pandas as pd

def generate_score(model, input):
    """
    """

    score = model.predict_proba(input)
        
    # out = logistic.predict_proba(X_test)
    return score

if __name__ == "__main__":
    # Load configuration
    with open("../config/config.yml","r") as yml:
        config = yaml.load(yml)
    config = config["score_model"]

    model = pickle.load( open( "trained_model.pkl", "rb" ) )

    data_address = config["data_address"]
    if user_input == "":
        user_input = pd.DataFrame({ Xdist:-2.0, Ydist:17.0, backhand:1, forehand:0, hammer:0})
    
    generate_score(model,)
