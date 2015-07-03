from item_factories import *
from app import db


def setup_factories(test):
    db.session.remove()
    db.drop_all()
    db.create_all()

    test.item = ItemFactory.create()
    test.item.save()
    test.item = ItemFactoryTwo.create()
    test.item.save()
    test.item = ItemFactoryThree.create()
    test.item.save()
    test.item = ItemFactoryFour.create()
    test.item.save()
    test.item = ItemFactoryFive.create()
    test.item.save()


def tear_down_factories():
    db.session.remove()
    db.drop_all()
