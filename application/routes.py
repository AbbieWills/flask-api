from application import app, db
from flask import request, jsonify, render_template, redirect
from application.models import FriendsCharacter
from application.forms import AddCharacterForm

def format_character(character):
    return {
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# POST 
@app.route("/characters", methods=["GET", "POST"])
def create_character():
    form = AddCharacterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            character = FriendsCharacter(name=form.name.data, age=form.age.data, catch_phrase=form.catch_phrase.data)
            db.session.add(character)
            db.session.commit()
            return redirect('/')
        # else:
            # error handling
    return render_template("add_character.html", form=form)

# Implement templates for all of your routes
# Validate the form and sanitise the input
# Create tests for the form and new items created
# Find a creative way to implement conditional rendering in a template

        

    # Retrieved data from client
    data = request.json
    # Created a new character using the data
    character = FriendsCharacter(data['name'], data['age'], data['catch_phrase'])
    # Send character to datbase
    db.session.add(character)
    db.session.commit()
    # Return JSON response back to the user/client
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route("/characters", methods=['GET'])
def get_characters():
    form = AddCharacterForm()
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return render_template('characters.html', characters=character_list, title="Friends Characters", form=form)

# GET /:id
@app.route('/characters/<id>')
def get_character(id):
    # filter_by
    character = FriendsCharacter.query.filter_by(id=id).first()
    return render_template("character.html", character=character)
# (id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

# DELETE /:id
@app.route("/characters/<id>", methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return f"Character deleted {id}"

# PATCH /:id
@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data["name"], age=data["age"], catch_phrase=data["catch_phrase"]))
    # Commit the change to the database
    db.session.commit()
    # Retrieve specific character from the filtering
    updatedCharacter = character.first()
    # Return JSON response to client 
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)
