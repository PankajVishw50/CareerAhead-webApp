from flask import render_template, url_for, request, flash, redirect, abort, session
from flask_login import login_required, current_user
from ..model import User, CounsellorType, Permission
from ..decorators import authority, is_user
from . import user
import json
from ..utils import get_maxPage, get_counsellors
from .forms import EditUserProfile
from .. import db


@user.route("/dashboard")
@login_required
def dashboard():
    return render_template("user/dashboard.html")


@user.route("/user-profile", methods=["GET", "POST"])
@login_required
@is_user
def user_profile():
    form = EditUserProfile()

    if request.method == "POST":
        if form.validate_on_submit():
            config_userdata(form)
            return redirect(url_for("user.user_profile"))
        else:
            for key in form.errors.keys():
                for error in form.errors[key]:
                    flash(error)

    return render_template("user/user_profile.html", form=form)


@user.route("/market")
@login_required
def market_page():
    types = CounsellorType.query.all()

    return render_template("user/market.html", types=types)


# This function returns with html with counsellor details
@user.post("/get-counsellors")
def provide_counsellor_template():
    page = session["page"]
    base = session["base"]

    counsellor = get_counsellors()

    start_index = (page - 1) * base
    end_index = page * base

    query = counsellor[start_index if start_index >= 0 else abort(404): end_index]

    return render_template("user/get-counsellor.html", counsellors=query)


# Returns current user position if not returns default value: page=1, base=10
@user.post("/get-info")
def current_pageBase():
    page = session.get("page")
    base = session.get("base")
    maxPage = session.get("maxPage")
    return dict(page=page if page else 1, base=base if base else 10,
                maxPage=maxPage)


@user.route("/book")
@is_user
def book():
    mail = request.args.get("counsellorMail")

    if not mail:
        return "Invalid request body", 404

    counsellor = User.query.filter_by(email=mail).first()

    if not counsellor:
        return "Invalid request", 404

    if counsellor.fee > current_user.balance:
        return "Not enough Balance.Please add balance first", 404

    current_user.balance -= counsellor.fee

    if counsellor in current_user.sessions:
        print("counsellor inside current_user")
        current_user.sessions.remove(counsellor)
        db.session.commit()
    counsellor.clients.append(current_user)
    db.session.commit()
    return "Session Booked: We will contact you through email for session schedule"


# This function updates user information
@authority(Permission.CHANGE_ACCOUNT)
def config_userdata(form):
    user = User.query.get(current_user.id)

    if form.username.data:
        filter = User.query.filter_by(username=form.username.data).first()
        if filter is None:
            user.username = form.username.data.lower()

    if form.age.data:
        user.age = form.age.data

    if form.email.data:
        filter = User.query.filter_by(email=form.email.data).first()
        if filter is None:
            user.email = form.email.data

    if int(form.gender.data) > 0:
        user.gender_id = int(form.gender.data)

    if form.new_password.data:
        user.password = form.new_password.data

    db.session.add(user)
    db.session.commit()

    return True


# This function called before every request of this blueprint and this config important data
@user.before_request
def initialize():
    if request.data:
        data = json.loads(request.data)

        session["filterName"] = ""  # setting it to empty because filter for name is not ready for now

        if data.get("type"):
            session["filterList"] = data["type"]
        if data.get("gender"):
            session["filterGender"] = data["gender"]
        if data.get("name"):
            session["filterName"] = data["name"]
        if data.get("price_upto"):
            session["filterPriceUpto"] = data["price_upto"]
        if data.get("page"):
            session["page"] = data["page"]
        if data.get("base"):
            session["base"] = data["base"]
        if session.get("maxPage"):
            session["maxPage"] = get_maxPage()

    if session.get("page") is None:
        session["page"] = 1
    if session.get("base") is None:
        session["base"] = 10
    if session.get("filterGender") is None:
        session["filterGender"] = 0
    if session.get("filterPriceUpto") is None:
        session["filterPriceUpto"] = 5000
    if session.get("filterName") is None:
        session["filterName"] = ""
    if session.get("filterList") is None:
        session["filterList"] = [-1]
        session["filterList"] = [0 for x in range(len(get_counsellors()))]
        if len(session["filterList"]) < 1:
            session["filterList"] = [-1]    # -1 = no filter
    if session.get("maxPage") is None:
        session["maxPage"] = get_maxPage()

