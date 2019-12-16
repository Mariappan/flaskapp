
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<Member {}>'.format(self.member_name)


def add_models(app, db):

    return Member



