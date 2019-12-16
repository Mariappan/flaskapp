
def models():
    pass


def add_models(app, db):

    class Member(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        member_name = db.Column(db.String(64), index=True, unique=True)
        member_age = db.Column(db.Integer, index=True, unique=True)

        def __repr__(self):
            return f"<Member {self.member_name} {self.member_age}>"

    models.Member = Member

    return models
