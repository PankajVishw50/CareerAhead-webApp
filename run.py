from app import create_app, db
from app.utils import get_maxPage, print_counsellor_type
from app.model import Gender, Role, User, CounsellorType, Session, CounsellorTypeAssociation, Permission
import os
from werkzeug.security import generate_password_hash, check_password_hash
import db_controller

app = create_app("production")  # Pass development, production, testing according to your need.
app.jinja_env.globals.update(os=os, app=app)


@app.context_processor
def context_processor():
    return dict(print_counsellor_type=print_counsellor_type, get_maxPage=get_maxPage, Permission=Permission)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role,
                Gender=Gender, Session=Session,
                CounsellorType=CounsellorType,
                clear=lambda: os.system('cls'),     # to clear terminal easily using clear()
                CounsellorTypeAssociation=CounsellorTypeAssociation,
                generate_password_hash=generate_password_hash, check_password_hash=check_password_hash,
                db_controller=db_controller)


app.add_template_global(context_processor()['print_counsellor_type'], name='print_counsellor_type')

if __name__ == "__main__":
    app.run()
