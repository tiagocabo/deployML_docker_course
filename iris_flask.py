
from flask import Flask, request
from flasgger import Swagger
import pandas as pd
from sklearn.metrics import accuracy_score

app = Flask(__name__)

swagger = Swagger(app)

model = pd.read_pickle("./rf.pkl")
test_data = pd.read_csv('./test_data.csv', index_col=0)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Generates documentation for iris predictor
    ---
    parameters:
      - name: id
        in: formData
        type: number
        required: true
    """
    flower_id = int(request.form['id'])
    print(flower_id)

    prediction = model.predict(test_data.iloc[flower_id, :4].values.reshape(1, -1))[0]
    print("Expected res: ", test_data.iloc[flower_id, -1])
    print("actual res: ", prediction)

    return str(prediction)

@app.route('/predict_file', methods=['POST'])
def predict_file():
    """
       Generates documentation for iris predictor
       ---
       parameters:
         - name: input_file
           in: formData
           type: file
           required: true
       """
    path = request.files.get("input_file")
    print('PATH ', path)
    path = './API_data.csv'
    test_data = pd.read_csv(path, index_col = 0)

    prediction = model.predict(test_data.iloc[:, :4].values)

    print("Expected res: ", test_data.iloc[:, -1])
    print("actual res: ", prediction)

    return str(list(prediction))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
