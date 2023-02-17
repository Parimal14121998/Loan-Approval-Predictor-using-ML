from flask import Flask,render_template,request,session,url_for,redirect
import pickle
from sqlite3 import *

app=Flask(__name__)
app.secret_key="pg1412"

@app.route("/",methods=["GET","POST"])
def home():
	if "un" in session:
		if request.method=="POST":
			if "submit2" in request.form:
				session.pop('un',None)
				return redirect(url_for('login'))
			if "submit1" in request.form:
				G1={"Male":1, "Female":0}
				M1={"Yes":1, "No":0}
				E1={"Graduate":1, "Not Graduate":0 }
				S1={"Yes":1, "No":0}
				P1={"Rural": 0, "Urban": 1, "Semiurban": 2}
				frame=[]
				msg1="Check for blank or invalid TEXTBOX input[0 or -ve]"
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
					ig=request.form["gender"]
					if ig in G1:
						frame.append(G1[ig])	
					im=request.form["married"]
					if im in M1:
						frame.append(M1[im])
					id=int(request.form["dependents"])
					frame.append(id)
					ie=request.form["education"]
					if ie in E1:
						frame.append(E1[ie])
					ise = request.form["self_employed"]
					if ise in S1:
						frame.append(S1[ise])
					try:
						ia=int(request.form["applicantincome"])
						if ia<=0:
							raise ValueError(msg1)
					except ValueError as e:
						return render_template("home.html",msg=msg1)
					else:
						frame.append(ia)

					try:
						ic=int(request.form["coapplicantincome"])
						if ic < 0:
							raise ValueError(msg1)
					except ValueError as e:
						return render_template("home.html",msg=msg1)
					else:
						frame.append(ic)
					try:
						ila=int(request.form["loanamount"])
						if ila <=0:
							raise ValueError(msg1)
					except ValueError as e:
						return render_template("home.html",msg=msg1)
					else:
						frame.append(ila)
					
					try:
						ilt=int(request.form["loan_amount_term"])
						if ilt <=0:
							raise ValueError(msg1)
					except ValueError as e:
						return render_template("home.html",msg=msg1)
					else:
						frame.append(ilt)
												
					ich=float(request.form["credit_history"])
					frame.append(ich)
					ipa=request.form["property_area"]
					if ipa in P1:
						frame.append(P1[ipa])
					print(frame)
					ans=model.predict([frame])
					print(ans)
					if ans==0:
						msg="Sorry , No Loan "
					if ans==1:
						msg="Congratulations! Loan Approved"
					return render_template("home.html",msg=msg)
				else:
					print("model issue")
		else:
			return render_template("home.html")
	else:
		return redirect(url_for('login'))


@app.route("/signup",methods=["GET","POST"])
def signup():
	if "un" in session:
		return redirect(url_for("home"))
	if request.method=="POST":
		un = request.form["un"]
		pw1 = request.form["pw1"]
		pw2 = request.form["pw2"]		
		if pw1==pw2:
			con=None
			try:
				con=connect("loan.db")
				cursor=con.cursor()
				sql="insert into users values('%s','%s')"
				cursor.execute(sql %(un,pw1))
				con.commit()
				return redirect(url_for('login'))
			except Exception as e:
				con.rollback()
				return render_template("signup.html",msg="User already exists -> " + str(e))
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("signup.html",msg="Password did not match")
	else:
		return render_template("signup.html")

@app.route("/login",methods=["GET","POST"])
def login():
	if "un" in session:
		return redirect(url_for("home"))
	if request.method=="POST":
		un = request.form["un"]
		pw = request.form["pw"]
		con=None
		try:
			con=connect("loan.db")
			cursor=con.cursor()
			sql="select * from users where username='%s' and password='%s'"
			cursor.execute(sql %(un,pw))
			data=cursor.fetchall()
			if len(data) == 0:
				return render_template("login.html",msg="Invalid Login")
			else:
				session["un"]=un
				return redirect(url_for('home'))
		except Exception as e:
			return render_template("login.html",msg=str(e))
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("login.html")

@app.errorhandler(404)
def not_found(e):
	return redirect(url_for('login'))



if __name__ == "__main__":
	app.run(debug=True,use_reloader=True)



		
		
			
	
