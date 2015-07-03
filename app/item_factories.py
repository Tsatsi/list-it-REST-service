from datetime import datetime

from models import Item
import factory


class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    name = factory.Sequence(lambda n: 'my list item %s' % n)
    description = factory.Sequence(lambda n: 'this is a description of my list item %s' % n)
    due_date = datetime.strptime("2015-08-04", "%Y-%m-%d")


class ItemFactoryTwo(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 2'
    description = 'this is a description of my list item 2'
    due_date = datetime.strptime("2015-08-04", "%Y-%m-%d")


class ItemFactoryThree(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 3'
    description = 'this is a description of my list item 3'
    due_date = datetime.strptime("2015-08-04", "%Y-%m-%d")


class ItemFactoryFour(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 4'
    description = 'this is a description of my list item 4'
    due_date = datetime.strptime("2015-08-04", "%Y-%m-%d")


class ItemFactoryFive(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 5'
    description = 'this is a description of my list item 5'
    due_date = datetime.strptime("2015-08-04", "%Y-%m-%d")
