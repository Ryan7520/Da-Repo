from flask import Flask
from flask import jsonify
import connexion
import numpy as np
from joblib import load

#load the model

my_model = load('reg_model.pkl')

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("master.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Welcome to my ML application!"}
    return jsonify(msg)

#create a URL route to send in model prediction data, returning the prediction
#@app.route("/predict/<data>")
#def predict(data):
	#predict using model, do I need to PCA my input or will the saved model do that already?
	#msg = my_model.predict(np.array(data))
	#return jsonify(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
