Title : Loan Approval Predictor

About :
This project will walk you through by exploring and building a loan prediction system/application as a data science and machine learning problem.we will apply Machine Learning Classification algorithm using supervised learning to predict Loan Approval binomiality.We will understand how Loan prediction analysis helps to determine whether or not the loan should get approved by using specific parameters about a loan application.

Motivation:
Loan Prediction using machine learning tools and techniques can help financial institutions quickly process applications by rejecting high-risk customers entirely, accepting worthy customers, and then assigning them to a manual review.

Tools/Libraries Used:
Python ,Flask ,Jupyter, ML Regression Algorithms , scikitLearn, Matplotlib , seaborn , pandas ,pickle, Html Forms , Session

Usage:
Customers can directly use the flask based webapp , provide there inputs and determine status/chances of approval of Loan . Besides there is signup/login based authentication approach to have secure  endpoints.

Procedure:
1) The jupyter notebook depicts the whole ML Lifecycle discussed as :
Loading dataset
Data Preprocessing [null and categorical]
Exploratory Data Analysis [Univariate & Multivariate Analysis ]
Feature Engineering
Correlation using HeatMap
Feature Selection
Train Test Split 
Model Selection by comparing different Classifiction Models
2)Model Deployment using Flask for which code is written in app.py

Implementation Logic:
1)Refer this Readme to know a quick overview.
2)Refer the Jupyter notebook file [.ipynb] to understand about the whole ML Lifecycle.
3)Refer the loanapp folder for :-
i) app.py -> Tells us about the code view , logic ,signup/login approach ,flask deployment
ii) templates folder for html ; rendering the display/output.
iii) lp.model is our model creation file created through p1.py and then we use this in app.py to predict the outcome.

Observations:
After EDA & feature Importance ; Applicants with very high incomes and co-applicant income with a good credit history have an excellent chance of getting loan approval.
After comparing score of Classification models; Random Forest Classifier performs best wrt to train_data{ Accuracy : 98% } and test_data {Accuracy : 82%}. 
For more analysis , visualisation and depiction refer attached jupyter notebook .

Conclusion:
Out of all models RandomForest Classifier provides best fit.
We gathered some insights about data through various graphs which depicts as similar to real life scenario
and understood patterns in the relation between the independent features and the chances of appoval of Loan.
The application can help in reducing the manual intervention , reduce processing time and smoothen the process.



