from crypt import methods
from logging import exception
import sys
from flask import Flask
from housing.exception import HousingException
from housing.logger import logging


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    try:
        raise Exception("We are raising exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)



    logging.info("We are testing logging module")
    return "Starting machine learning project"


if __name__=="__main__":
    app.run(debug=True)

