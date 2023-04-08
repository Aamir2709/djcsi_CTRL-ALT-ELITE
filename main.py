from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
from flask_cors import CORS,cross_origin
import requests,bs4
from bs4 import BeautifulSoup


app = Flask(__name__,template_folder='templates')

@app.get("/")
def index():
    
    return render_template("index.html")


if __name__=="__main__":
    app.run()