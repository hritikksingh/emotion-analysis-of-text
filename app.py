import pandas as pd
from flask import Flask, jsonify, request
import pickle
from keras.models import model_from_json,model_from_yaml
import clean_data as cd

yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
model = model_from_yaml(loaded_model_yaml)
# load weights into new model
model.load_weights("model.h5")

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    data= data["Text"]
    
    # predictions
    result=cd.get_sentiment(model, data)
    result=result.to_json()
    # send back to browser
    output = {'results': result}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)