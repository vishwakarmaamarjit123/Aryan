from flask import Flask,request,jsonify
import pickle
import numpy as np

model = pickle.load(open('aryannewlog3.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"


@app.route('/predict', methods=['POST'])
def predict():
    percentage_in_Algorithms = request.form.get('percentage in Algorithms')
    Percentage_in_Software_Engineering = request.form.get('Percentage in Software Engineering')
    Percentage_in_Computer_Networks = request.form.get('Percentage in Computer Networks')
    Logical_quotient_rating = request.form.get('Logical quotient rating')
    hackathons = request.form.get('hackathons')
    coding_skills_rating = request.form.get('coding skills rating')



    input_query = np.array([[percentage_in_Algorithms,Percentage_in_Software_Engineering,Percentage_in_Computer_Networks,Logical_quotient_rating,hackathons,coding_skills_rating]])

    result = model.predict(input_query)[0]

    return jsonify({"Suggested Job Role": str(result)})






if __name__  == '__main__':
    app.run(debug=True)

