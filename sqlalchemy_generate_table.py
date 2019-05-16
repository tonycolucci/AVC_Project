from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, MetaData
import sqlalchemy as sql
import logging
import pandas as pd
import os

Base = declarative_base()

class Throw(Base):
	"""Create a data model for the database to be set up for capturing songs """
	__tablename__ = 'throws'
	id = Column(Integer, primary_key=True)
	hand_rl = Column(String(20), unique=False, nullable=True)
	throw_type = Column(String(100), unique=False, nullable=True)
	stall = Column(Integer, unique=False, nullable=True)
	completion = Column(Integer, unique=False, nullable=True)
	Xdist = Column(Integer, unique=False, nullable=True)
	Ydist = Column(Integer, unique=False, nullable=True)
  	  
	def __repr__(self):
		return '<throw %r>' % self.id

# the engine_string format
#engine_string = "{conn_type}://{user}:{password}@{host}:{port}/DATABASE_NAME"
conn_type = "mysql+pymysql"
user = os.environ.get("MYSQL_USER") 
password = os.environ.get("MYSQL_PASSWORD")
host = os.environ.get("MYSQL_HOST")
port = os.environ.get("MYSQL_PORT")
DATABASE_NAME = 'msia423' ## UPDATE
engine_string = "{}://{}:{}@{}:{}/{}".\
format(conn_type, user, password, host, port, DATABASE_NAME)
#print(engine_string)
engine = sql.create_engine(engine_string)
Base.metadata.create_all(engine)

# set up looging config
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)
# create a db session
# Session = sessionmaker(bind=engine)  
# session = Session()
# # add a record/track
# throw1 = Track(id = 1, hand_rl = "R", throw_type = "F", stall = 2, completion = 1, Xdist = 11, Ydist = 3)  
# session.add(throw1)
# session.commit()
# query = "SELECT * FROM throws WHERE completion == 1"
# df = pd.read_sql(query, con=engine)
# print(df)
# session.close()
