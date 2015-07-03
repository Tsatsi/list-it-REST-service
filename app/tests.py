import unittest
from datetime import date, datetime
import json

from setup_test_db import setup_factories, tear_down_factories
from models import Item
from app import app, db


class TestItemResource(unittest.TestCase):
    def setUp(self):
        setup_factories(self)
        self.app_test_client = app.test_client()

    def tearDown(self):
        tear_down_factories()

    def test_create_list_item(self):
        list_item_data = {
            'name': "pair with bukiwe",
            'description': "This is the description for pairing",
        }
        response = self.app_test_client.post("/api/items", data=json.dumps(list_item_data))

        self.assertEqual('200 OK', response.status)

        response_data = json.loads(response.data)
        self.assertEqual("pair with bukiwe", response_data.get("name"))
        self.assertEqual("This is the description for pairing", response_data.get("description"))

    def test_require_list_item_name_to_create(self):
        list_item_data = {
            'description': "This is the description for pairing",
            'due_date': "2015-08-04"
        }
        response = self.app_test_client.post("/api/items", data=json.dumps(list_item_data))

        self.assertEqual('400 BAD REQUEST', response.status)
        self.assertEqual('The list item name is required', response.data)

    def test_create_list_item_without_description_and_due_date(self):
        list_item_data = {
            "name": "android coded in braam"
        }
        response = self.app_test_client.post("/api/items", data=json.dumps(list_item_data))

        self.assertEqual('200 OK', response.status)
        response_data = json.loads(response.data)
        self.assertEqual("android coded in braam", response_data.get("name"))

    def test_should_get_list_of_items(self):
        response = self.app_test_client.get('/api/items')
        self.assertEqual("200 OK", response.status)
        response_data = json.loads(response.data)
        self.assertEqual(5, len(response_data.get('items')))

    def test_should_get_item_with_id(self):
        response = self.app_test_client.get('/api/items/2')

        self.assertEqual("200 OK", response.status)
        response_data = json.loads(response.data)
        self.assertEqual("my list item 2", response_data.get("name"))
        self.assertEqual("this is a description of my list item 2", response_data.get("description"))
        self.assertEqual(datetime.strptime("2015-08-04", "%Y-%m-%d").isoformat(), response_data.get("due_date"))

    def test_should_handle_getting_list_item_with_wrong_id(self):
        response = self.app_test_client.get('/api/items/20')

        self.assertEqual("404 NOT FOUND", response.status)
        self.assertEqual("The requested item was not found", response.data)

    def test_should_delete_list_item_by_id(self):
        url = '/api/items/1'
        response = self.app_test_client.delete(url)

        self.assertEqual("200 OK", response.status)
        self.assertEqual("Successfully deleted", response.data)
        deleted_item_get_response = self.app_test_client.get(url)
        self.assertEqual("404 NOT FOUND", deleted_item_get_response.status)

    def test_should_handle_deleting_list_item_with_wrong_id(self):
        response = self.app_test_client.delete('/api/items/20')

        self.assertEqual("404 NOT FOUND", response.status)
        self.assertEqual("The requested item was not found", response.data)

    def test_should_update_list_item(self):
        list_item_data = {
            'name': "This is an update message",
            'description': "This is the description of the update",
            'due_date': "2015-07-04"
        }

        url = '/api/items/4'
        response = self.app_test_client.put(url, data=json.dumps(list_item_data))
        self.assertEqual("200 OK", response.status)
        self.assertEqual("Successfully updated", response.data)

        updated_list_item_get_response = self.app_test_client.get(url)

        self.assertEqual("200 OK", updated_list_item_get_response.status)
        response_data = json.loads(updated_list_item_get_response.data)
        self.assertEqual("This is an update message", response_data.get("name"))
        self.assertEqual("This is the description of the update", response_data.get("description"))
        self.assertEqual(datetime.strptime("2015-07-04", "%Y-%m-%d").isoformat(), response_data.get("due_date"))


class TestItemModel(unittest.TestCase):
    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_format_item_to_json(self):
        item = Item("test name", "This is a test description", date(2015, 6, 25))
        item.save()
        results = item.to_json()
        expected_results = dict(id=1, name="test name", description="This is a test description",
                                due_date="2015-06-25T00:00:00")
        self.assertEqual(expected_results, results)


