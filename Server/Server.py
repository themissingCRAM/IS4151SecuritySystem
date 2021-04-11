import connexion
from flask import render_template,request,url_for,redirect
import secrets
app = connexion.App(__name__, specification_dir='./')
secret =  secrets.token_urlsafe(32)
app.secret_key = secret
#app.add_api('swagger.yml')
# app.add_api('swaggerfull.yml')



@app.route('/')
def index():

  return render_template('login.html')

@app.route('/login',methods=["POST"])
def login():
  if request.method == "POST":
    username = request.form.get("uname")
    password = request.form.get("psw")
    if username == "user" and password == "password": 
      return redirect(url_for("dashboard", loginSuccess = True))
    else :
      return render_template("login.html",result="login failed")
@app.route('/dashboard/<loginSuccess>')
def dashboard(loginSuccess):
   if loginSuccess:
      print("LoginSuccess string")
      return render_template("dashboard.html",loginSuccess = "Logged in successfully.") 
   else: 
     print("loginSuccess string gone")
     return render_template("dashboard.html") 
# If we're running in stand alone mode, run the application
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)

