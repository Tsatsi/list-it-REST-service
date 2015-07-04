from models import Item
import factory


class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item'
    description = 'this is a description of my list item'
    priority = 'High'


class ItemFactoryTwo(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 2'
    description = 'this is a description of my list item 2'
    priority = 'High'


class ItemFactoryThree(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 3'
    description = 'this is a description of my list item 3'
    priority = 'High'


class ItemFactoryFour(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 4'
    description = 'this is a description of my list item 4'
    priority = 'High'


class ItemFactoryFive(factory.Factory):
    class Meta:
        model = Item

    name = 'my list item 5'
    description = 'this is a description of my list item 5'
    priority = 'High'
