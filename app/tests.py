import unittest
import json

from setup_test_db import setup_factories, tear_down_factories
from models import Item, User
from app import app, db


class TestItemResource(unittest.TestCase):
    def setUp(self):
        setup_factories(self)
        self.app_test_client = app.test_client()

    def tearDown(self):
        tear_down_factories()

    def test_create_list_item(self):
        list_item_data = {
            'user_id': 1,
            'name': "pair with bukiwe",
            'priority': "High",
            'description': "This is the description for pairing",

        }
        response = self.app_test_client.post("/api/items", data=json.dumps(list_item_data))

        self.assertEqual('200 OK', response.status)

        response_data = json.loads(response.data)
        self.assertEqual("pair with bukiwe", response_data.get("name"))
        self.assertEqual("This is the description for pairing", response_data.get("description"))

    def test_require_list_item_name_to_create(self):
        list_item_data = {
            'user_id': 1,
            'description': "This is the description for pairing",
            'priority': "High"
        }
        response = self.app_test_client.post("/api/items", data=json.dumps(list_item_data))

        self.assertEqual('400 BAD REQUEST', response.status)
        self.assertEqual('The list item name is required', response.data)

    def test_create_list_item_without_description(self):
        list_item_data = {
            'user_id': 1,
            "name": "android coded in braam"
        }
        response = self.app_test_client.post("/api/items", data=json.dumps(list_item_data))

        self.assertEqual('200 OK', response.status)
        response_data = json.loads(response.data)
        self.assertEqual("android coded in braam", response_data.get("name"))

    def test_should_get_list_of_users_items(self):
        response = self.app_test_client.get('/api/user/items/1')
        self.assertEqual("200 OK", response.status)
        response_data = json.loads(response.data)
        self.assertEqual(5, len(response_data.get('items')))

    def test_should_delete_list_item_by_id(self):
        url = '/api/items/1'
        response = self.app_test_client.delete(url)

        self.assertEqual("200 OK", response.status)
        self.assertEqual("Successfully deleted", response.data)

    def test_should_handle_deleting_list_item_with_wrong_id(self):
        response = self.app_test_client.delete('/api/items/20')

        self.assertEqual("404 NOT FOUND", response.status)
        self.assertEqual("The requested item was not found", response.data)

    def test_should_update_list_item(self):
        list_item_data = {
            'user_id': 1,
            'name': "This is an update message",
            'description': "This is the description of the update",
            'priority': "Medium"
        }

        url = '/api/items/4'
        response = self.app_test_client.put(url, data=json.dumps(list_item_data))
        self.assertEqual("200 OK", response.status)
        self.assertEqual("Successfully updated", response.data)


class UserResource(unittest.TestCase):
    def setUp(self):
        setup_factories(self)

        self.app_test_client = app.test_client()

    def tearDown(self):
        tear_down_factories()

    def test_should_register_user(self):
        user_data = {
            "username": "Bokang",
            "email": "bokang@mail.com"
        }

        response = self.app_test_client.post("/api/user/register", data=json.dumps(user_data))

        self.assertEqual('200 OK', response.status)

        response_data = json.loads(response.data)
        self.assertEqual("Bokang", response_data.get("username"))
        self.assertEqual("bokang@mail.com", response_data.get("email"))


class TestItemModel(unittest.TestCase):
    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_format_item_to_json(self):
        item = Item(1, "test name", "Medium", "This is a test description")
        item.save()
        results = item.to_json()
        expected_results = dict(id=1, user_id=1, name="test name", priority="Medium",
                                description="This is a test description")
        self.assertEqual(expected_results, results)


class TestUserModel(unittest.TestCase):
    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_format_item_to_json(self):
        user = User("Karabo", "karabo@mailer.com")
        user.save()
        results = user.to_json()
        expected_results = dict(id=1, username="Karabo", email="karabo@mailer.com")
        self.assertEqual(expected_results, results)
