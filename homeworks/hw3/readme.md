@Author: Churong Zhang

# Current MySQL configurations

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'TodoList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

please change it to appropriate settting based on your local in app.py
app.py also contain the code to set up mysql database

todo item status, title, description, delete an item can be perform in the /userHome route
