# Importing Dependencies
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# import prediction_model
# from prediction_model import train_pipeline
from prediction_model.predict import make_prediction
import pandas as pd

# Create a FastAPI instance and assign it to the app so that the app will be a point of interaction while creating the API.
app = FastAPI(
	title="Loan Prediction Model API",
    description="A simple API that use ML model to predict the Loan application status",
    version="0.1",
	)

# CORS (Cross-Origin Resource Sharing) refers to the situation when a front end running in a browser has JavaScript code that communicates with a back end, 
# and the back end is of a different origin than the front end. 
# However, it depends on your application and requirement whether to use it or not.

origins = [
    "*"
	]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
	)

# Define the class LoanPred, which defines the data type expected from the client.
# You can use the LoanPred class for the data model that is inherited from BaseModel.
# Then, add a root view of the function that returns 'message': 'Loan Prediction App' for the home page.

class LoanPred(BaseModel):
	Gender: str
	Married: str
	Dependents: str
	Education: str
	Self_Employed: str
	ApplicantIncome: float
	CoapplicantIncome: float
	LoanAmount: float
	Loan_Amount_Term: float
	Credit_History: float
	Property_Area: str

@app.get('/')
def index():
    return {'message': 'Loan Prediction App'}

# Defining the function which will make the prediction use the data which the user inputs.
# Here, create /predict_status as an endpoint, also known as the route. 
# Then, add predict_loan_status() with a parameter of the type data model that you created as LoanPred.

@app.post('/predict_status')
def predict_loan_status(loan_details: LoanPred):
	data = loan_details.dict()
	Gender = data['Gender']
	Married = data['Married']
	Dependents = data['Dependents']
	Education = data['Education']
	Self_Employed = data['Self_Employed']
	ApplicantIncome = data['ApplicantIncome']
	CoapplicantIncome = data['CoapplicantIncome']
	LoanAmount = data['LoanAmount']
	Loan_Amount_Term = data['Loan_Amount_Term']
	Credit_History = data['Credit_History']
	Property_Area = data['Property_Area']

	# Making predictions 
	input_data = [Gender,  Married,  Dependents,  Education,
				Self_Employed,  ApplicantIncome,  CoapplicantIncome,
				LoanAmount,  Loan_Amount_Term,  Credit_History,  Property_Area]
	cols = ['Gender','Married','Dependents',
			'Education','Self_Employed','ApplicantIncome',
			'CoapplicantIncome','LoanAmount','Loan_Amount_Term',
			'Credit_History','Property_Area']
	data_dict = dict(zip(cols,input_data))
	prediction = make_prediction([data_dict])['prediction'][0]

	if prediction == 'Y':
		pred = 'Approved'
	else:
		pred = 'Rejected'

	return {'status':pred}

# The following function will create the UI for user input. 
# Here, create /predict as an endpoint, also known as a route, and declare input data types expected from users.

@app.post('/predict')
def get_loan_details(Gender: str, Married: str, Dependents: str, 
	Education: str, Self_Employed: str, ApplicantIncome: float, 
	CoapplicantIncome: float, LoanAmount: float, Loan_Amount_Term: float, 
	Credit_History: float, Property_Area: str):

	input_data = [Gender,  Married,  Dependents,  Education,
				Self_Employed,  ApplicantIncome,  CoapplicantIncome,
				LoanAmount,  Loan_Amount_Term,  Credit_History,  Property_Area]
	cols = ['Gender','Married','Dependents',
			'Education','Self_Employed','ApplicantIncome',
			'CoapplicantIncome','LoanAmount','Loan_Amount_Term',
			'Credit_History','Property_Area']

	data_dict = dict(zip(cols,input_data))
	prediction = make_prediction([data_dict])['prediction'][0]
	if prediction == 'Y':
		pred = 'Approved'
	else:
		pred = 'Rejected'

	return {'status':pred}

if __name__ == '__main__':
	uvicorn.run(app)