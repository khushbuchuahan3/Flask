# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 18:52:55 2022

@author: hp
"""

from flask import Flask,request
import pandas as pd
import numpy as np

import pickle


app=Flask(__name__)

model=pickle.load(open("classifier.pkl","rb"))

@app.route("/")
def welcome():
    return "Welcome All"

@app.route("prediction")
def curruncy_prediction():
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction 


if __name__=="__main__":
    app.run()