from joblib import load
import numpy as np

def predict (data):
	my_model = load('reg_model.pkl')
	final = np.array(data)
	finalT = final.reshape(1,-1)
	prediction = my_model.predict(finalT)
	if(prediction[0] == 1):
		return "Likely to have a heart attack"
	else:
		return "Unlikely to have a heart attack"