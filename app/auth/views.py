from . import auth
from .forms import LoginForm, SignInForm
from ..model import User
from flask_login import login_user, logout_user, login_required
from flask import flash, request, redirect, url_for, render_template
from ..utils import printf
from .. import db


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # Checking if used details are valid
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash("Successfully logged in")
            next = request.args.get("next")
            return redirect(next or url_for("main.index"))
        else:
            flash("invalid credentials")

    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Successfully logged out")
    return redirect(url_for("main.index"))


@auth.route("/signin", methods=["GET", "POST"])
def create_account():
    form = SignInForm()

    if request.method == "POST":
        if form.validate_on_submit():
            printf("Data")
            print(form.gender.data)
            user = User(username=form.username.data, age=form.age.data,
                        gender_id=int(form.gender.data),
                        role_id=1,  # role_Id = 1 = User
                        email=form.email.data, password=form.password.data)

            db.session.add(user)
            db.session.commit()

            flash("Account Created. Login to proceed further")
            return redirect(url_for("auth.login"))

        else:
            printf("Error flash")
            print(form.errors.keys())
            print(form.errors)
            for x in form.errors.keys():
                for _ in form.errors[x]:
                    flash(_)

    return render_template("auth/signin.html", form=form)
