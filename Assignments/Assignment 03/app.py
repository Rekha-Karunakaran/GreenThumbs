from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login1', methods = ['POST',"GET"])
def login1():
    EMAIL = request.form['EMAIL']
    PASSWORD = request.form['PASSWORD']
    if EMAIL == "rekha23@gmail.com" and PASSWORD == "IBMcloud23":
        return "login successful & Welcome to my portal"
    else:
        return render_template("register.html")
    
@app.route('/register', methods = ['POST',"GET"])
def register1():
    NAME = request.form['NAME']
    EMAIL = request.form['EMAIL']
    PASSWORD = request.form['password']
    CONFIRMPASSWORD = request.form['confirm password']
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug = True,port = 8080)
    



