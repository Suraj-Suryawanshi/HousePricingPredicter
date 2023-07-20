# from flask import Flask, jsonify, render_template, request
# from test2 import predict_output 

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():    
#     house_features = [x for x in request.form.values()]
#     print(house_features)    
#     houselist = [int(house_features[0]),int(house_features[1]),int(house_features[2]),int(house_features[3]),int(house_features[4]),house_features[5],house_features[6],house_features[7],house_features[8],house_features[9]]
#     result = predict_output(houselist)
    
#     return render_template('index.html', predictedResult='Predicted Price is {}'.format(result))

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, render_template, request
from test2 import predict_output

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    house_features = [x for x in request.form.values()]
    houselist = [int(house_features[0]), int(house_features[1]), int(house_features[2]), int(house_features[3]), int(house_features[4]), house_features[5], house_features[6], house_features[7], house_features[8], house_features[9]]
    try:
        result = predict_output(houselist)
        return render_template('index.html', predictedResult='Predicted Price is {}'.format(result))
    except ValueError as e:
        return render_template('index.html', predictedResult=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)

