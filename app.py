from flask import Flask, request, jsonify

from models import Hero, Power, HeroPower, db, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) 
migrate.init_app(app, db) 

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=("id", "name", "super_name")) for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict())

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([powers.to_dict(only=("id", "name")) for power in powers])

@app.route('/powers/<int: id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@app.route('/powers/<int: id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "validation errors"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    try:
        if 'name' in data:
            power.name = data['name']
        db.session.commit()
        return jsonify(power.to_dict())
    except KeyError:
        return jsonify({"error": "Invalid fields"}), 400
    
@app.route('/powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    if not data:
        return jsonify({"error": "validation errors"}), 400
    # try:
    new_powers = Power(name=data['name'])
    db.session.add(new_powers)
    db.session.commit()
    return jsonify(new_powers.to_dict()), 201
    # except KeyError:
    #     return jsonify({"error": "Missing required fields"})


if __name__ == '__main__':
    app.run(debug=True)