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
    return jsonify([power.to_dict(only=("id", "name")) for power in powers])  # Fixed typo

@app.route('/powers/<int:id>', methods=['GET'])  # Fixed syntax error
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.json
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["Description must be at least 20 characters long."]}), 400
    
    power.description = description
    db.session.commit()
    return jsonify(power.to_dict())

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    strength = data.get("strength")
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")

    # Validate required fields
    if not strength or not hero_id or not power_id:
        return jsonify({"errors": ["Missing required fields"]}), 400

    # Validate strength values
    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'."]}), 400

    # Validate Hero and Power exist
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["Hero or Power not found"]}), 404

    hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero_power.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
