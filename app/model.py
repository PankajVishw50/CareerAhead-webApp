from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from flask_login import UserMixin, AnonymousUserMixin


@login_manager.user_loader
def load_user(id):
    return User.query.get(str(id))


# Setting Permission flags
class Permission:
    BOOK_SESSION = 0x01
    CHANGE_ACCOUNT = 0x02
    POST = 0x04
    APPROVE_SESSION = 0x08
    COUNSELLOR = 0x0e
    ADMINISTER = 0xff


CounsellorTypeAssociation = db.Table("CounsellorTypeAssociation",
                                     db.Column("counsellor_id", db.Integer, db.ForeignKey("User.id")),
                                     db.Column("type_id", db.Integer, db.ForeignKey("CounsellorType.id")))

Session = db.Table("Session",
                   db.Column("user_id", db.Integer, db.ForeignKey("User.id")),
                   db.Column("counsellor_id", db.Integer, db.ForeignKey("User.id")))


class Gender(db.Model):
    __tablename__ = "Gender"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(12 * 1), unique=True, nullable=False)
    user_id = db.relationship("User", backref="user_gender", lazy=True)

    def __repr__(self):
        return f"<Gender {self.gender}>"


class Role(db.Model):
    __tablename__ = "Role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12 * 2), unique=True, nullable=False)
    permissions = db.Column(db.Integer)
    user_id = db.relationship("User", backref="user_role", lazy=True)

    @staticmethod
    def insert_roles():
        roles = {
            "user": Permission.BOOK_SESSION | Permission.CHANGE_ACCOUNT,     # 0b00000011
            "counsellor": Permission.CHANGE_ACCOUNT | Permission.APPROVE_SESSION | Permission.POST,    # 0b00001110
            "administer": Permission.ADMINISTER     # Ob11111111
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r, permissions=roles[r])
                db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12 * 2), unique=True, nullable=False)
    email = db.Column(db.String(12 * 5), unique=True, nullable=True)
    balance = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(12 * 9), nullable=False)
    image = db.Column(db.String(12 * 5), default="/user/user.img")
    age = db.Column(db.Integer)
    fee = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    description = db.Column(db.Text)
    role_id = db.Column(db.Integer, db.ForeignKey("Role.id"))
    gender_id = db.Column(db.Integer, db.ForeignKey("Gender.id"))

    clients = db.relationship("User", secondary=Session,
                              primaryjoin="Session.c.counsellor_id==User.id",
                              secondaryjoin="Session.c.user_id==User.id",
                              backref="sessions")

    type_of = db.relationship("CounsellorType", secondary=CounsellorTypeAssociation,
                              backref="counsellor")


    @property
    def password(self):
        return AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, permissions):
        return self.role_id is not None and (self.user_role.permissions & permissions) == permissions



    def __repr__(self):
        return f"<User {self.username}>"


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_adminstrator(self):
        return False

    def is_counsellor(self):
        return False


class CounsellorType(db.Model):
    __tablename__ = "CounsellorType"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(12 * 5), unique=True, nullable=False)

    def __repr__(self):
        return f"<CounsellorType {self.type}>"


























