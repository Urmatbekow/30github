from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)


model = tf.keras.models.load_model('path_to_your_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(input_data)
    prediction_list = prediction.tolist()
    return jsonify({'prediction': prediction_list})

if __name__ == '__main__':
    app.run(debug=True)