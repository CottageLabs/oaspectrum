from flask import Blueprint, render_template

from octopus.core import app
from octopus.lib.webapp import ssl_required
from flask.ext.login import login_required

blueprint = Blueprint('admin', __name__)

# admin page
@blueprint.route("/")
@ssl_required
@login_required
def admin():
    return render_template("admin/admin.html")