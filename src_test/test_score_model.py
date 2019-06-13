import pytest
import pandas as pd
import os
import sys
import pickle
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
# from sklearn.model_selection import train_test_split
from src_test.score_model import generate_score

data = pd.DataFrame({'Xdist': [4],
                     'Ydist': [8],
                     'Stall': [4]})
model = pickle.load( open( "../models/trained_model.pkl", "rb" ) )

def test_score_model():
  test_score = generate_score(model, data)
  assert test_score > 0
  assert test_score < 1