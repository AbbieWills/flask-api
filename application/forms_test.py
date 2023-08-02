import pytest
from application.forms import AddCharacterForm

def test_valid_form_data():
    form_data = {
        'name': 'Ross',
        'age': 30,
        'catch_phrase': 'Pivot!'
    }
    form = AddCharacterForm(data=form_data)
    assert form.validate() is True

def test_empty_form_data():
    form_data = {}
    form = AddCharacterForm(data=form_data)
    assert form.validate() is False

def test_invalid_name():
    form_data = {
        'name': 'R',
        'age': 30,
        'catch_phrase': 'Pivot!'
    }
    form = AddCharacterForm(data=form_data)
    assert form.validate() is False

def test_missing_age():
    form_data = {
        'name': 'Ross',
        'catch_phrase': 'Pivot!'
    }
    form = AddCharacterForm(data=form_data)
    assert form.validate() is False

def test_invalid_age():
    form_data = {
        'name': 'Ross',
        'age': 'thirty',
        'catch_phrase': 'Pivot!'
    }
    form = AddCharacterForm(data=form_data)
    assert form.validate() is False

def test_invalid_catch_phrase():
    form_data = {
        'name': 'Ross',
        'age': 30,
        'catch_phrase': 'P'
    }
    form = AddCharacterForm(data=form_data)
    assert form.validate() is False
