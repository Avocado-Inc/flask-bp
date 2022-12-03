import json
from flask import Blueprint, jsonify, request
from app.db.get_db import get_db
from app.models import Pet

pet_route = Blueprint('pets', __name__, url_prefix='/pets')


@pet_route.get('/')
def list_pets():

    print(request)
    page = request.args.get('page', 1)
    db = get_db()
    data = db.query(Pet).all()
    print(data)
    response = []
    for i in data:
        response.append({
            "id": i.id
        })
    return jsonify(response)

@pet_route.get('/aa')
def pet():

    print(request)
    page = request.args.get('id', 1)
    db = get_db()
    result = db.execute('select * from pets')
    print(result)
    return []


@pet_route.post('/')
def create_pet():
    data = request.get_json()
    db = get_db()
    print(data)
    pet = Pet(name=data.get('name', 'Cat'))
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return jsonify({
        "id": pet.id,
        "name": pet.name
    })