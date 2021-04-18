
from flask import Flask, render_template, request, json, redirect
from flaskext.mysql import MySQL
from flask import session

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qq5201314'
app.config['MYSQL_DATABASE_DB'] = 'FavoritePlaces'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

########## Insert couple places to DB
# INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Lucky City", "3215 Independence Pkwy, Plano, TX 75075, USA", 33.0397033,-96.7542972, "restaurant");
# INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Mudleaf Coffee", "3100 Independence Pkwy #300, Plano, TX 75075, USA", 33.0406858,-96.75085820000001, "cafe");
# INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Bull Daddy Noodle Bistro", "3309 Coit Rd #100, Plano, TX 75093, USA", 33.0425785,-96.7705574, "restaurant");
# INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("East Wall Chinese Cuisine", "3033 W Parker Rd #214, Plano, TX 75023, USA", 33.0425315,-96.7526559, "restaurant");
# INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("Olive Burger Plano", "2129 W Parker Rd #301, Plano, TX 75023, USA", 33.0429329,-96.733908, "restaurant");
# INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("First Chinese BBQ Plano", "3304 Coit Rd, Plano, TX 75023, USA", 33.04231600000001,-96.76936099999999, "restaurant");
# INSERT INTO restaurants(name, address, lat, lng, type) VALUES ("King Buffet Plano", "521 E Central Pkwy, Plano, TX 75074, USA", 33.026728,-96.708162, "restaurant");

# pip3 install flask-mysql

app.secret_key = 'secret key can be anything!'


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/getFavoritePlaces', methods=['GET'])
def getFavoritePlaces():
    try:
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM restaurants")
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        data = cursor.fetchall()
        for result in data:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    except Exception as e:
        print(e)
        return "error"
    finally:
        cursor.close()
        con.close()

if __name__ == "__main__":
    app.run()
