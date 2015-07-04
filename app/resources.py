import json

from app import db
from flask.ext.restful import Resource
from flask import request, jsonify, make_response
from models import Item, User


class ItemResource(Resource):
    def get(self, id=None):
        items = Item.query.filter(Item.user_id == id)
        results = dict(items=[item.to_json() for item in items])
        return make_response(jsonify(results), 200)

    def post(self):
        data = json.loads(request.data)
        if 'name' not in data:
            return make_response('The list item name is required', 400)
        else:
            name = data.get('name')
            user_id = data.get('user_id')
            description = data.get('description') if 'description' in data else None
            priority = data.get('priority') if 'priority' in data else None
            item = Item(user_id, name, priority, description)
            item.save()
            return make_response(jsonify(item.to_json()), 200)

    def put(self, id):
        data = json.loads(request.data)
        Item.query.filter(Item.id == id).update(data)
        db.session.commit()
        return make_response("Successfully updated", 200)

    def delete(self, id):
        item_to_delete_query_filter = Item.query.filter(Item.id == id)
        item = item_to_delete_query_filter.first()
        if item:
            item_to_delete_query_filter.delete()
            db.session.commit()
            return make_response("Successfully deleted", 200)
        else:
            return make_response("The requested item was not found", 404)


class UserResource(Resource):
    def post(self):
        data = json.loads(request.data)
        if 'username' not in data or 'email' not in data:
            return make_response('username and email required', 400)
        else:
            username = data.get('username')
            email = data.get('email')

            user = User(username, email)
            user.save()
            return make_response(jsonify(user.to_json()), 200)
