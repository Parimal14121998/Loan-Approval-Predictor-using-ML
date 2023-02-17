#import lib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix,classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

data=pd.read_csv("lap.csv")
print(data.head())

#understand data
res=data.isnull().sum()
print(res)


#fillna
data["LoanAmount"].fillna(data["LoanAmount"].mean(),inplace=True)
data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].mean(),inplace=True)
data["Gender"].fillna(data["Gender"].mode()[0],inplace=True)
data["Married"].fillna(data["Married"].mode()[0],inplace=True)
data["Dependents"].fillna(data["Dependents"].mode()[0],inplace=True)
data["Self_Employed"].fillna(data["Self_Employed"].mode()[0],inplace=True)
data["Credit_History"].fillna(data["Credit_History"].mode()[0],inplace=True)

data.drop(["Loan_ID"],axis=1,inplace=True)

#cat data
data = data.replace({"Gender":{"Male":1, "Female":0 }})
data = data.replace({"Married" :{"Yes":1, "No":0}})
data = data.replace({"Self_Employed":{"Yes":1, "No":0 }})
data = data.replace({"Education":{"Graduate":1, "Not Graduate":0 }})
data['Property_Area'] = data['Property_Area'].map({'Rural': 0, 'Urban': 1, 'Semiurban': 2})
data['Loan_Status'] = data.Loan_Status.map({'Y': 1, 'N': 0}).astype(int)
data['Dependents'] = data['Dependents'].replace('3+', '3')
data['Dependents']=pd.to_numeric(data['Dependents'], errors='coerce')

#f&t
f=data.drop(["Loan_Status"],axis=1)
t=data["Loan_Status"]

#train_test_split
x_train,x_test,y_train,y_test=train_test_split(f,t,test_size=0.2,random_state=11)

#model
rf = RandomForestClassifier(n_estimators=10)
rf.fit(f,t)
'''
cr=classification_report(y_test,rf.predict(x_test))
print(cr)
cr=classification_report(y_train,rf.predict(x_train))
print(cr)
'''
print(data[0:2])
#save the model
f=None
try:
	f=open("lp.model","wb")
	pickle.dump(rf,f)
except Exception as e:
	print("issue ",e)
finally:
	if f is not None:
		f.close()


    


