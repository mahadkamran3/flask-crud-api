from flask import Flask, request,jsonify
from models import db, Person
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    with app.app_context(): 
        db.create_all()
        print("Database tables created")

@app.route('/people', methods= ['POST'])
def add_person():
    data = request.get_json()
    new_person = Person(
        name=data.get('name'),
        age=data.get('age'),
        gender=data.get('gender'),
        email=data.get('email')
    )
    db.session.add(new_person)
    db.session.commit()
    return jsonify(new_person.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)