#model usage

import pickle
f=None
model=None
try:
	f=open("lp.model","rb")
	model=pickle.load(f)
except Exception as e:
	print("issue ",e)
finally:
	if f is not None:
		f.close()
if model is not None:
	data=[[1,1,0,1,2,5600,1240,1100,360,1,0]]
	print(model.predict(data))
else:
	print("model issue")

	