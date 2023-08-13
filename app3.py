# server.py
"""from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# API endpoint for sending notifications
@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    message = data['message']
    
    # You can add your notification logic here
    # For simplicity, we'll just return the message in this example
    
    response = jsonify({'message': message})
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(debug=True)"""



from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pyodbc
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://LAPTOP-MTEB9CR1\SQLEXPRESS/hello?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    accountType = db.Column(db.String(80))
    # Add more columns as per your requirements
with app.app_context():
    db.create_all()


from flask import request

@app.route('/add_user', methods=['POST'])
def add_user():
    usernam = request.get_json()  # Get the username from the request form data
    email = usernam['email']
    password = usernam['password']
    accountType = usernam['accountType']

    # Create a new user instance
    new_user = User2(email=email,password=password,accountType=accountType)

    # Add the user to the database session
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'id': new_user.id,
        'email': new_user.email,
        'password': new_user.password,
        'accountType': new_user.accountType
        # Add more attributes as needed
    })
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = User2.query.filter_by(email=email, password=password).first()
    if user:
        return jsonify({
            'message': 'Login successful',
            
                'id': user.id,
                'username': user.email,
                'accountType': user.accountType
            
        })
    else:
        return jsonify({'message': 'Invalid username or password'})

if __name__ == '__main__':
    app.run(debug=True)    