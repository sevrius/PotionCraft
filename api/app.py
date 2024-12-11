from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise toutes les origines par défaut

potions = [
    {"id": 1, "name": "Potion de guérison", "ingredients": ["Herbe", "Eau bénite"], "effect": "Restaure 50 PV"},
    {"id": 2, "name": "Potion de force", "ingredients": ["Racine de mandragore", "Sang de troll"], "effect": "Augmente la force de 20 points"},
]

@app.route("/potions", methods=["GET"])
def get_potions():
    return jsonify(potions)

@app.route("/potions", methods=["POST"])
def add_potion():
    data = request.json
    new_potion = {
        "id": len(potions) + 1,
        "name": data["name"],
        "ingredients": data["ingredients"],
        "effect": data["effect"],
    }
    potions.append(new_potion)
    return jsonify(new_potion), 201

@app.route("/potions/<int:potion_id>", methods=["DELETE"])
def delete_potion(potion_id):
    global potions
    potions = [p for p in potions if p["id"] != potion_id]
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
