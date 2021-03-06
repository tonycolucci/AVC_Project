import pytest
import pandas as pd
import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
# from sklearn.model_selection import train_test_split
from src_test.train_model import split_response, model_training
from src_test.score_model import generate_score


data = pd.DataFrame({'Xdist': [4, 20, 8, 26, 7, 5, 6, 8, 42, 7],
                     'Ydist': [8, 5, 0, 2, 0, 4, 7, 5, 6, 2],
                     'Stall': [4, 6, 2, 1, 5, 2, 9, 2, 4, 0],
                     'completion': [1, 0, 0, 1, 1, 1, 1, 1, 1, 0]})

data.to_csv("test_data.csv")



def test_split_response():
  test_features, test_response = split_response(data, ["completion"], ["Xdist","Ydist","Stall"])
  assert test_features.shape[1] == 3
  assert test_response.shape[1] == 1
  assert test_features.shape[0] == test_response.shape[0]

test_features, test_response = split_response(data, ["completion"], ["Xdist","Ydist","Stall"])

def test_model_training():
  test_model = model_training(test_features, test_response, 3, 10)
  assert test_model.coef_.shape[1] == 3