from item_factories import *
from user_factories import *
from app import db


def setup_factories(test):
    db.session.remove()
    db.drop_all()
    db.create_all()

    test.user = UserFactory.create()
    test.user.save()

    test.item = ItemFactory.create(user_id=int(test.user.id))
    test.item.save()
    test.item = ItemFactoryTwo.create(user_id=int(test.user.id))
    test.item.save()
    test.item = ItemFactoryThree.create(user_id=int(test.user.id))
    test.item.save()
    test.item = ItemFactoryFour.create(user_id=int(test.user.id))
    test.item.save()
    test.item = ItemFactoryFive.create(user_id=int(test.user.id))
    test.item.save()


def tear_down_factories():
    db.session.remove()
    db.drop_all()
