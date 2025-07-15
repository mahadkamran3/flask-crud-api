from flask import Blueprint, request, jsonify
from app.models import Item
from app import db

crud_bp = Blueprint('crud_bp', __name__)

@crud_bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    item = Item(name=name, description=description)
    db.session.add(item)
    db.session.commit()

    return jsonify({'message': 'Item created', 'id': item.id}), 201
