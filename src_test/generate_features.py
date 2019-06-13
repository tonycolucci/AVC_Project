# Imports
import logging
import yaml
import pandas as pd
import numpy as np
 
logger = logging.getLogger(__name__)

def open_data(data_address):
    """ Generates a score for given input data from a logistic regression model
    Args:
        data_address (str): The relative address of the input data in string format
    Returns:
        throw_analysis (:py:class:`pandas.DataFrame`): DataFrame containing the columns for use in model training
    """
    # Read data in from data folder
    throws = pd.read_csv(data_address)
    logger.info("open_data: Read {} rows and {} columns from {}".format(throws.shape[0], throws.shape[1], data_address))

    # Take the columns for use in analysis and drop any NA rows
    throw_analysis = throws[["Xdist","Ydist","Stall","completion"]].dropna()
    logger.info("open_data: Returned {} rows and {} columns".format(throw_analysis.shape[0], throw_analysis.shape[1]))

    # Take absolute value of cross field throws
    throw_analysis["Ydist"] = abs(throw_analysis["Ydist"])

    return throw_analysis

if __name__ == "__main__":
    # Load configuration
    with open("config/config.yml","r") as yml:
        config = yaml.load(yml)
    config = config["generate_features"]

    # Find input data and take appropriate columns for analysis
    data_address = config["input_address"]
    analysis_data = open_data(data_address)

    # Save data for analysis to separate file
    output_address = config["output_address"]
    analysis_data.to_csv(output_address)