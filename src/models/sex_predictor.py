#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:50:49 2020

@author: gabriel
"""
import argparse
import pandas as pd
import os
import pickle
import warnings
warnings.filterwarnings('ignore')

def main():
    # getting the dataset
    parser = argparse.ArgumentParser(
            prog='sex_predictor.py',
            usage='sex_predictor.py --<input_file> ',
            description='Predict the sex of an individual')
    parser.add_argument(
            '--input_file',
            type=str,
            help='Full path to the input file')

    args = parser.parse_args()
    file_path = args.input_file
    
    # fiding root path
    script_path = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(script_path))
    
    # load model
    model = pickle.load(open(os.path.join(root, "models", "model.pickle.dat"),
                             "rb"))
    # load dataset
    print(" Loading Dataset")
    data = pd.read_csv(file_path)
    # pre process data
    print(" Pre-processing data")
    data = pre_process(data)
    print(" Starting inference")
    prediction = model.predict(data)
    
    # using information obtained during analisys to imporve prediction
    idx = data.chol > 335
    for i in range(len(idx)):
        if idx[i]:
            prediction[i] = 'M'
    print(" Saving prediction")
    # it says to save the result in the same directory,
    # so I will save in the root
    pd.DataFrame({"sex":prediction}).to_csv(
            os.path.join(root, "newsample_PREDICTIONS_gabrielLopesSilva.csv"))
    
# Process the data to be predictible by the model 
def pre_process(data):
    # selecting features
    data = data[ ['trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                'exang', 'oldpeak', 'slope', 'ca', 'thal', 'hc', 'sk', 'trf']]
    
    # fill nan if any
    data.slope = data.slope.fillna(0)
    data.chol = data.chol.fillna(236)
    # if there is any ca = 4 it will turn to 0 because it's the one with more 
    # samples
    data.ca = data.ca.replace(4, 0)
    
    # transform TRF
    data.trf = pd.DataFrame(data.trf.values / 60).astype(int)
    
    # making dummy variables
    for feature in [ 'fbs', 'restecg', 'exang', 'ca', 'thal', 'hc', 'sk',
                    'slope']:
        data = pd.concat([data,
                        pd.get_dummies(data[feature], prefix = feature)],
                        axis=1).drop([feature],
                        axis=1)
    return data    
    
if __name__ == '__main__' :
    main()