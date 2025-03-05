from flask import *

import ibm_db

conn = ibm_db.connect("DATABASE = bludb;HOSTNAME = 6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY = SSL;SSLServerCertificate = DigiCertGlobalRootCA.crt;UID = lcx34343;PWD = bIwm6K3SSakdPqoI",'','')
print(conn)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


# Registration page routing

@app.route('/register1',methods=['POST'])
def register1():
    x = [x for x in request.form.values()]
    print(x)
    USERNAME=x[0]
    EMAIL=x[1]
    PASSWORD=x[2]
    CONFIRMPASSWORD=X[3]
    sql = "SELECT * FROM register WHERE EMAIL =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,EMAIL)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    print(account)
    if account:
        return render_template('login.html', pred="You are already a member, please login using your details")
    else:
        insert_sql = "INSERT INTO  REGISTER VALUES (?, ?, ?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, NAME)
        ibm_db.bind_param(prep_stmt, 2, EMAIL)
        ibm_db.bind_param(prep_stmt, 3, PASSWORD)
        ibm_db.execute(prep_stmt)
        return render_template('login.html', pred="Registration Successful, please login using your details")
       
          
    
@app.route('/login1',methods=['POST'])
def login1():
    EMAIL = request.form['EMAIL']
    PASSWORD = request.form['PASSWORD']
    sql = "SELECT * FROM login WHERE EMAIL =? AND PASSWORD=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,EMAIL)
    ibm_db.bind_param(stmt,2,PASSWORD)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    print (account)
    print(EMAIL,PASSWORD)
    if account:
            return render_template('login.html', pred="Login successful")
    else:
        return render_template('login.html', pred="Login unsuccessful. Incorrect username/password !") 
      
        
if __name__ == "__main__":
    app.run(debug = False, port = 8888)