import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
m1 = Base.classes.measurements
s1 = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)


app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def percipitation():
	query1=session.query(m1.date,m1.prcp).filter(m1.date >= '2010-1-1' , m1.date < '2011-1-1').all()
	query1 = query1.set_index('date')
	query1 =query1.to_dict()
	return jsonify(query1)

# @app.route("/api/v1.0/stations")
# def stationNames():
# 	results = session.query(Station.name).all()
# 	station_names = list(np.ravel(results))
# 	return jsonify(station_names)

# @app.route("/api/v1.0/tobs")
# def tobs():



# if __name__ == '__main__':
# 	app.run(debug=True)





