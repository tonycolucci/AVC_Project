import logging
import yaml
import pandas as pd
import numpy as np
 
logger = logging.getLogger(__name__)

def open_data(data_address, output_address):
    """
    """
    throws = pd.read_csv(data_address)

    # throw_types = pd.get_dummies(throws.throw_type).rename(columns = {"BH":"backhand","F":"forehand","H":"hammer"})

    # throw_analysis = pd.concat([throws,throw_types], axis = 1)[["Xdist","Ydist","backhand","forehand","hammer","completion"]].dropna()
    throw_analysis = throws[["Xdist","Ydist","Stall","completion"]].dropna()
    throw_analysis["Ydist"] = abs(throw_analysis["Ydist"])

    return throw_analysis

if __name__ == "__main__":
    # Load configuration
    # os.chdir("../config/")
    with open("config/config.yml","r") as yml:
        config = yaml.load(yml)
    # os.chdir("../src/")
    config = config["generate_features"]

    data_address = config["input_address"]
    output_address = config["output_address"]

    analysis_data = open_data(data_address, output_address)

    analysis_data.to_csv(output_address)