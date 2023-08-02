from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/characters", methods=['POST'])
def create_character():
    data = request.json
    character = FriendsCharacter(data["name"], data["age"], data["catch_phrase"])
    db.session.add(character)
    db.session.commit()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route("/characters", methods=['GET'])
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return character_list
refactor routes into one using if and else statements

# @app.route("/characters", methods=['POST', 'GET'])
# def get_character():
#     character = FriendsCharacter.query.get(id)
#     if request.method == "GET":
#         return format_character(character)
#     elif request.method == "POST":
#         data = request.json
#         character.name = data["name"]
#         character.age = data["age"]
#         character.catch_phrase = data["catch_phrase"]
#         db.session.commit()
#         return format_character(character)
#         return "", 204

# GET /:id
@app.route("/characters/<int:id>")
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)


# DELETE /:id
@app.route("/characters/<int:id>", methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return f"Character deleted {id}"

# Patch /:id
@app.route("/characters/<int:id>", methods=['PATCH'])   
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data["name"], age=data["age"], catch_phrase=data["catch_phrase"]))
    db.session.commit()
    updatedCharacter = character.first()
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)


    
    
