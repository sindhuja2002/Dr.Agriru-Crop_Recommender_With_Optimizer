from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import numpy as np
import plotly
import json

import pickle
import tools

npk =[]
nut =[]
out="rice"
app = Flask(__name__, template_folder="templates")
model = pickle.load(open("./model.pkl", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("home.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	global npk
	global nut
	global out
	if request.method == "POST":

		# statw
		state_no = int(request.form['state'])
		state = tools.state_id(state_no)
		#print("state= ",state)
		# city
		city = str(request.form['city'])
		# nitrogen ratio
		N = float(request.form['N'])
		# potassium ratio
		K = float(request.form['K'])
		# phospours ratio
		P = float(request.form['P'])

		#secondary nutrients
		# calcium 
		calcium = float(request.form['calcium'])
		ca_unit = str(request.form['ca_unit'])

		# magnesium amount
		magnesium = float(request.form['magnesium'])
		mg_unit = str(request.form['mg_unit'])

		# sulphur amount
		sulphur = float(request.form['sulphur'])
		s_unit = str(request.form['s_unit'])
		
		# micro  nutrients

		#boron amount
		boron = float(request.form['boron'])
		b_unit = str(request.form['b_unit'])
		
		# iron amount
		iron = float(request.form['iron'])
		fe_unit = str(request.form['fe_unit'])

		# zinc amount
		zinc = float(request.form['zinc'])
		zn_unit = str(request.form['zn_unit'])

		# magnese amount
		magnese = float(request.form['magnese'])
		mn_unit = str(request.form['mn_unit'])
		# ph
		ph = float(request.form['ph'])
		
		npk = [N,P,K,ph]
		#print(npk)
		nut = [calcium,magnesium ,sulphur,zinc,iron,boron,magnese]
		unit =[ca_unit,mg_unit,s_unit,zn_unit,fe_unit,b_unit,mn_unit]
		#print(npk,nut,unit)
		nut = tools.convert(nut,unit)
		#print(nut)
		#append temp,humidity,rainfall in input_lst
		loc=tools.loc_att(state,city)
		input_lst=[npk[0],npk[1],npk[2],loc[0],loc[1],npk[3],loc[2]]
		input_lst = np.array(input_lst).reshape(1,-1)
		pred = model.predict(input_lst)
		out = pred[0]
		#print(out)
		

		return render_template("{}.html".format(out))
	
		


	return render_template("predict.html")

@app.route("/analiser",methods=['GET', 'POST'])
@cross_origin()
def analiser():
	global npk
	global nut
	global out
	l= npk
	#print(npk)
	#print(l,nut)
	avail= [l[0],l[1],l[2],nut[0],nut[1],nut[2],nut[5],nut[4],nut[3],nut[6],l[3]]
	opt = tools.graph_val(out)
	req = tools.graph_scaling(avail,opt)
	fig = tools.graph(avail , req)
	header="{} CROP OPTIMIZER".format(out.upper())
	graphJSON = plot_utl(fig)
	#print(graphJSON)
	return render_template('graph.html', graphJSON =graphJSON, header=header,required=req)

def plot_utl(fig):
	return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)



if __name__=='__main__':
	app.run(debug=True)