from flask import Blueprint, render_template, request, abort, flash

from octopus.core import app
from octopus.lib.webapp import ssl_required
from flask.ext.login import login_required
from service.importer import import_csv, ImportException

import os, uuid

blueprint = Blueprint('admin', __name__)

def _cleanup(path):
    try:
        os.remove(path)
    except:
        pass

# admin page
@blueprint.route("/", methods=["GET", "POST"])
@ssl_required
@login_required
def index():
    if request.method == "GET":
        return render_template("admin/admin.html")

    elif request.method == "POST":
        # check that we have somewhere to save the file
        upload = app.config.get("UPLOAD_DIR")
        if upload is None or upload == "":
            abort(500)

        # save the file to disk
        path = os.path.join(upload, uuid.uuid4().hex + ".csv")
        file = request.files["csv"]
        file.save(path)

        # now process the file
        try:
            import_csv(path)
        except ImportException as e:
            _cleanup(path)
            flash("Unable to import CSV: " + e.message, "error")
            return render_template("admin/admin.html")

        _cleanup(path)
        flash("CSV was successfully imported", "success")
        return render_template("admin/admin.html")