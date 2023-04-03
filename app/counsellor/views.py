from . import counsellor
from ..decorators import is_counsellor
from flask_login import login_required, current_user
from flask import render_template, request, flash
from .forms import EditCounsellorProfile
from ..model import User


@counsellor.route("/counsellor-profile", methods=["GET", "POST"])
@login_required
@is_counsellor
def counsellor_profile():
    form = EditCounsellorProfile()

    if request.method == "POST":
        if form.validate_on_submit():
            return "submitted"
        else:
            for key in form.errors.keys():
                for error in form.errors[key]:
                    flash(error)

    return render_template("counsellor/counsellor-profile.html", form=form)


@counsellor.route("/counsellor/<id>")
def post(id):
    counsellor = User.query.get(id)
    return render_template("counsellor/post.html", counsellor=counsellor)













