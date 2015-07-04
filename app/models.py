from app import db


class ListItModel(db.Model):
    def save(self):
        db.session.add(self)
        db.session.commit()

    __abstract__ = True


class Item(ListItModel):
    def __init__(self, user_id, name, priority=None, description=None):
        self.name = name
        self.priority = priority
        self.description = description
        self.user_id = user_id

    def to_json(self):
        return dict(id=self.id,
                    user_id=self.user_id,
                    name=self.name,
                    priority=self.priority,
                    description=self.description
                    )

    def formatted_date(self):
        formatted_date = None
        if self.due_date:
            formatted_date = self.due_date.isoformat()
        return formatted_date

    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    priority = db.Column(db.String(128))
    creation_date = db.Column(db.DateTime, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')


class User(ListItModel):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_json(self):
        return dict(id=self.id,
                    username=self.username,
                    email=self.email)

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(150))
    items = db.relationship('Item', cascade="all, delete-orphan", lazy="dynamic")
