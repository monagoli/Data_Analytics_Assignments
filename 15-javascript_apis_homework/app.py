# we have to create a flask app to access our sqlite database...
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
#importing this will allow us to automap the classes and relationships from a database (in our case it will be the bellybutton sqlite connection)
from sqlalchemy.orm import Session 
#this allows us to establish a connection with the database
from sqlalchemy import create_engine,func
#this allows us to create an engine that will connect to the databse
from flask import Flask,render_template,jsonify,request
#from flask we are importing the Flask class, render_template which will allow us to render the HTML through flask, and jsonify will allow us to print pretty json
import pandas as pd
import numpy as np

app=Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

engine = create_engine('sqlite:///belly_button_biodiversity.sqlite')
Base=automap_base()
Base.prepare(engine,reflect=True)

Samples = Base.classes.samples 
OTU = Base.classes.otu
Metadata=Base.classes.samples_metadata

session = Session(engine)

@app.route('/')
def home():
	return render_template('index.html')

	
@app.route('/names')
def names():
	##this is storing your query of the Samples table in the variable names
	names=db.session.query(Samples).statement
	##create a pandas dataframe to hold the data in question  using the method read_sql_query 
	names_df = pd.read_sql_query(names,session.bind)
	##this will return a json list of the columns from the data frame you created above
	return jsonify(list(names_df.columns))

@app.route('/otu')
def otu():
	#now we want to return one column of the data from the otu data

	##to help find the column headings for the otu data...
	# test=db.session.query(OTU).statement
	# test_df=pd.read_sql_query(test,session.bind)
	# return jsonify(list(test_df.columns))
	##this returns like a list of lists....we need to unravel it and jsonify it
	otu_data = session.query(OTU.lowest_taxonomic_unit_found).all()
	unravel_otu=list(np.ravel(otu_data))
	return jsonify(unravel_otu)

@app.route('/metadata/<int:sample>')
def metadata(sample):
	##now we're trying to find the meta data from the samples metadata table and return a json object for each unique sample id
	metadata=session.query(Metadata.SAMPLEID,Metadata.AGE,Metadata.BBTYPE,Metadata.LOCATION,Metadata.ETHNICITY).filter(Metadata.SAMPLEID==sample).all()
	##here we are giving each value a column heading
	metadata_df=pd.DataFrame(metadata,columns=['SAMPLEID','AGE','BBTYPE','LOCATION','ETHNICITY'])
	##now we need to create a dictionary fomr the pandas dataframe...
	# sample = (jsonify(metadata_df.to_dict(orient='records')))
	return (jsonify(metadata_df.to_dict(orient='records')))

# @app.route('/wfreq/<int:sample>')
# def wfreq(sample):
# 	#essentially same idea as above....i hope...
# 	wfreq=session.query(Metadata.SAMPLEID).filter(Metadata.SAMPLEID==sample).all()
# 	wfreq_df=pd.DataFrame(wfreq,columns=['SAMPLEID'])
# 	test=list(np.ravel(wfreq_df))
# 	# return (jsonify(wfreq_df.to_dict(orient='records')))
# 	return jsonify(test)


@app.route('/wfreq/<int:sample>')
def wfreq(sample):
	##now we're trying to find the meta data from the samples metadata table and return a json object for each unique sample id
	wfreq=session.query(Metadata.WFREQ).filter(Metadata.SAMPLEID==sample).all()
	unravel_wfreq=np.ravel(wfreq)
	# ##here we are giving each value a column heading
	# wfreq_df=pd.DataFrame(unravel_wfreq,columns=['WFREQ'])
	# ##now we need to create a dictionary fomr the pandas dataframe...
	# # sample = (jsonify(metadata_df.to_dict(orient='records')))
	# # TEST =jsonify(wfreq_df.to_dict(orient='records'))
	# return jsonify(wfreq_df.to_dict(orient='records'))
	# wfreq=session.query(Metadata.SAMPLEID,Metadata.WFREQ).filter(Metadata.SAMPLEID==sample).all()
	# wfreq_df=pd.DataFrame(wfreq,columns=['SAMPLEID','WFREQ'])
	return jsonify(int(unravel_wfreq[0]))


# @app.route('/sample')
# def samples():
# 	names=session.query(Samples).statement
# 	names_df = pd.read_sql_query(names,session.bind)
# 	names_df['otu_id'].replace('BB_','',regex=True,inplace=True)

# 	return jsonify(list(names_df['otu_id']))

@app.route('/samples/<sample>')
def samples(sample):
    """Return a list dictionaries containing `otu_ids` and `sample_values`."""
    samplesearch = session.query(Samples).statement
    sample_df = pd.read_sql_query(samplesearch, session.bind)

    # Return any sample values greater than 1
    sample_df = sample_df[sample_df[sample] > 1]

    # Sort the results by sample in descending order
    sample_df = sample_df.sort_values(by=sample, ascending=0)

    # Format the data to send as json
    sampledata = [{
        "otu_ids": sample_df[sample].index.values.tolist(),
        "sample_values": sample_df[sample].values.tolist()
    }]
    return jsonify(sampledata)






if __name__ == "__main__":
    app.run(debug=True)



	##wanna return the sample ID without the BB...have to strip it somehow...
	#lets query the sqlite database for those values and then strip them of the bb...??
	# names=session.query(Samples.otu_id).statement
	# ##create a pandas dataframe to hold the data in question  using the method read_sql_query 
	# names_df = pd.DataFrame(names,columns=['otu_id'])

	# # names_df = names_df.sort_values(by=sample,descending=0)

	# # samplesinfo = [{
 # #        "otu_ids": names_df[sample].index.values.tolist(),
 # #        "sample_values": names_df[sample].values.tolist()
 # #    }]
	# return jsonify(names_df.to_dict(orient='records'))

	#jsonify(list(names_df.columns))


