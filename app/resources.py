import json
from datetime import datetime
from app import db, app
from flask.ext.restful import Resource
from flask import request, jsonify, make_response
from models import Item


class ItemResource(Resource):
    def get(self, id=None):
        if id:
            return self.get_member_by_id(id)
        else:
            items = Item.query.all()
            results = dict(items=[item.to_json() for item in items])
            return make_response(jsonify(results), 200)

    def get_member_by_id(self, id):
        item = Item.query.filter(Item.id == id).first()
        if item:
            return make_response(jsonify(item.to_json()), 200)
        else:
            return make_response("The requested item was not found", 404)

    def post(self):
        data = json.loads(request.data)
        if 'name' not in data:
            return make_response('The list item name is required', 400)
        else:
            name = data.get('name')
            description = data.get('description') if 'description' in data else None
            due_date = datetime.strptime(data.get('due_date'), "%Y-%m-%d") if 'due_date' in data else None
            item = Item(name, description, due_date)
            item.save()
            return make_response(jsonify(item.to_json()), 200)

    def put(self, id):
        data = json.loads(request.data)
        if data.get('due_date'):
            data['due_date'] = datetime.strptime(data.get('due_date'), "%Y-%m-%d")
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
