from models import User
import factory


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = "Thabiso"
    email = "thabiso@mail.com"
