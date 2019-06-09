# Imports
import logging
import yaml
import pickle
import pandas as pd
import numpy as np
import sklearn
import os
from sklearn.linear_model import LogisticRegressionCV

logging.basicConfig(level=logging.INFO, format="%(name)-12s %(levelname)-8s %(message)s")
logger = logging.getLogger()

def open_data(data_address):
    """
    """
    throws = pd.read_csv(data_address)

    # throw_types = pd.get_dummies(throws.throw_type).rename(columns = {"BH":"backhand","F":"forehand","H":"hammer"})

    # throw_analysis = pd.concat([throws,throw_types], axis = 1)[["Xdist","Ydist","backhand","forehand","hammer","completion"]].dropna()
    throw_analysis = throws[["Xdist","Ydist","Stall","completion"]].dropna()
    throw_analysis["Ydist"] = abs(throw_analysis["Ydist"])
    throw_analysis.to_csv("../data/analysis_data.csv")

    return throw_analysis

def split_response(data, response_col): #, train_share, random_state
    """
    """
    features = data.drop(columns = response_col)
    response = data[[response_col]]
    # X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(feature_cols, response,
    #                                                                             train_size=train_share,
    #                                                                             random_state=random_state)

    return features, response

def model_training(X_train, y_train, CV_folds):
    logistic = LogisticRegressionCV(cv = CV_folds).fit(X_train, y_train)
    
    
    # print(logistic.coef_)

    return logistic



if __name__ == "__main__":
    # Load configuration
    # os.chdir("../config/")
    with open("../config/config.yml","r") as yml:
        config = yaml.load(yml)
    # os.chdir("../src/")
    config = config["train_model"]

    data_address = config["data_address"]

    analysis_data = open_data(data_address)

    train_share = config["train_share"]
    response_col = config["response_col"]
    random_state = config["random_state"]

    features, response = split_response(analysis_data, response_col) #, random_state, train_share

    CV_folds = config["CV_folds"]
    model = model_training(features, response, CV_folds)

    pickle.dump( model, open( config["model_address"], "wb" ) )