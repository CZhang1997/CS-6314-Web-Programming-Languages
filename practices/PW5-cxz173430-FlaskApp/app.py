
from flask import Flask, render_template, request, json, redirect
from flaskext.mysql import MySQL
from flask import session

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'TodoList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

# pip3 install flask-mysql
# use todolist;
# drop table tbl_user;
# CREATE TABLE tbl_user( userid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) , email VARCHAR(30),password VARCHAR(30));
# CREATE TABLE tbl_todo( id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(30) , description VARCHAR(60), userid int(11));



app.secret_key = 'secret key can be anything!'


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/showAddItem')
def showAddItem():
    return render_template('addItem.html')

@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        con = mysql.connect()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM tbl_user WHERE email = %s", (_email))

        data = cursor.fetchall()
        if len(data) > 0:
            if str(data[0][3]) == _password:
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        con.close()


@app.route('/signUp',methods=['POST'])
def signUp():

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO tbl_user(name, email, password) VALUES (%s, %s, %s)", (_name, _email, _password))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            cursor.execute("SELECT * FROM tbl_user WHERE email = %s", (_email))
            data = cursor.fetchall()
            session['user'] = data[0][0]
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})


    else:
        return json.dumps({'html':'<span>Enter the required fields!</span>'})

@app.route('/addItem',methods=['POST'])
def addItem():
    # read the posted values from the UI
    try:
        if session.get('user'):
            _title = request.form['inputTitle']
            _description = request.form['inputDescription']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tbl_todo(title, description, userid) VALUES (%s, %s, %s)", (_title, _description, _user))
            data = cursor.fetchall()

            if len(data) == 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return json.dumps({'error':str(data[0])})

    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()

@app.route('/getTodoList', methods=['GET'])
def getTodoList():
    try:
        if session.get('user'):
            con = mysql.connect()
            cursor = con.cursor()
            _user = session.get('user')

            cursor.execute("SELECT * FROM tbl_todo WHERE userid = %s", (_user))
            row_headers=[x[0] for x in cursor.description]
            json_data=[]
            data = cursor.fetchall()
            for result in data:
                json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data) 

    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        con.close()

if __name__ == "__main__":
    app.run()
