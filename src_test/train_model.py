# Imports
import logging
import yaml
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegressionCV

logging.basicConfig(level=logging.INFO, format="%(name)-12s %(levelname)-8s %(message)s")
logger = logging.getLogger()


def split_response(data, response_col, analysis_cols): #, train_share
    """ Splits the data set into separate dataframes, one with features and one with response for model training.
    Args:
        data (:py:class:`pandas.DataFrame`): DataFrame containing the features
        analysis_cols (:obj:`list`): List of columnms to use as features
        response_col (:obj:`list`): List of a single column to use as the response column
    Returns:
        features (:py:class:`pandas.DataFrame`): DataFrame containing features columns
        response (:py:class:`pandas.DataFrame`): DataFrame containing a single column for the response variable
    """
    # Split out features and response dataframes
    features = data[analysis_cols]
    response = data[response_col]

    return features, response

def model_training(X_train, y_train, CV_folds, random_state):
    """ Trains a logistic regression model using cross validation
    Args:
        X_train (:py:class:`pandas.DataFrame`): DataFrame containing features columns
        y_train (:py:class:`pandas.DataFrame`): DataFrame containing a single column for the response variable
        CV_folds (int): Integer indicating the number of folds over which to run cross validation.
    Returns:
        logistic (sklearn model object): The model generated by regressing the response over the features
    """
    
    logistic = LogisticRegressionCV(cv = CV_folds, random_state = random_state).fit(X_train, y_train)

    return logistic



if __name__ == "__main__":
    # Load config
    with open("config/config.yml","r") as yml:
        config = yaml.load(yml)
    config = config["train_model"]

    # Get data with features
    data_address = config["data_address"]
    analysis_data = pd.read_csv(data_address)
    logger.info("train_model: data read in from {}".format(data_address))
    
    # Load arguments for splitting data and split out response column
    response_col = config["response_col"]
    analysis_cols = config["analysis_cols"]
    features, response = split_response(analysis_data, response_col, analysis_cols)

    # Load argument for model training and return the trained model
    CV_folds = config["CV_folds"]
    random_state = config["random_state"]
    logger.info("train_model: Training using logistic regression with {}-fold cross validation and random state of {}".format(CV_folds, random_state))
    model = model_training(features, response, CV_folds, random_state)

    # Create a pickle object containing the model
    pickle.dump( model, open( config["model_address"], "wb" ) )