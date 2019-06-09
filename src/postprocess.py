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
  """
  """
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

  Session = sessionmaker(bind=engine)  
  session = Session()

  for index, row in data_to_store.iterrows():
    stall = int(row["Stall"])
    Xdist = int(row["Xdist"])
    Ydist = int(row["Ydist"])
    prediction = float(row["prediction"])
    throw = Throw(stall = stall, Xdist = Xdist, Ydist = Ydist, prediction = prediction)
    session.add(throw)
  
  session.commit()

  return


if __name__ == "__main__":
  logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
  logger = logging.getLogger(__file__)
  # Load configuration
  # os.chdir("../config/")
  with open("../config/config.yml","r") as yml:
      config = yaml.load(yml)
  # os.chdir("../src/")
  config = config["postprocess"]


## Fire up SQL Alchemy session


## Build tables


# set up looging config



# create a db session


# Build an example throw
# prediction = Throw(id = 1, hand_rl = "R", throw_type = "F", stall = 2, completion = 1, Xdist = 11, Ydist = 3)  

# Add and commit that throw to the engine
