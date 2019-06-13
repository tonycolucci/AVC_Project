# Imports
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, MetaData, Float
import sqlalchemy as sql
import logging
import pandas as pd
import os

from src.sqlalchemy_generate_table import Throw

Base = declarative_base()

logger = logging.getLogger(__name__)

def store_data(data_to_store):
  """ Stores predicted values along with the inputs used to generate those predictions in RDS table
  Args:
    data_to_store (:py:class:`pandas.DataFrame`): DataFrame containing a users input data and the predicted probability from the model
  Returns:
    None
  """
  # Create connection with SQL Alchemy session on RDS instance
  conn_type = "mysql+pymysql"
  user = os.environ.get("MYSQL_USER") 
  password = os.environ.get("MYSQL_PASSWORD")
  host = os.environ.get("MYSQL_HOST")
  port = os.environ.get("MYSQL_PORT")
  DATABASE_NAME = 'msia423' 
  engine_string = "{}://{}:{}@{}:{}/{}".\
  format(conn_type, user, password, host, port, DATABASE_NAME)
  engine = sql.create_engine(engine_string)
  Base.metadata.create_all(engine)

  # Start session based on connection
  Session = sessionmaker(bind=engine)  
  session = Session()

  # Loop through input database, create Throw object for each row and add that row to the session
  for index, row in data_to_store.iterrows():
    stall = int(row["Stall"])
    Xdist = int(row["Xdist"])
    Ydist = int(row["Ydist"])
    prediction = float(row["prediction"])
    throw = Throw(stall = stall, Xdist = Xdist, Ydist = Ydist, prediction = prediction)
    session.add(throw)
  
  # Commit the session to add new row(s) to the RDS database
  session.commit()

  return


if __name__ == "__main__":
  logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
  logger = logging.getLogger(__file__)
  # Load configuration
  # os.chdir("../config/")
  with open("config/config.yml","r") as yml:
      config = yaml.load(yml)
  # os.chdir("../src/")
  config = config["postprocess"]
