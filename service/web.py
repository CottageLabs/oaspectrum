from octopus.core import app, initialise, add_configuration

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="pycharm debug support enable")
    parser.add_argument("-c", "--config", help="additional configuration to load (e.g. for testing)")
    args = parser.parse_args()

    if args.config:
        add_configuration(app, args.config)

    pycharm_debug = app.config.get('DEBUG_PYCHARM', False)
    if args.debug:
        pycharm_debug = True

    if pycharm_debug:
        app.config['DEBUG'] = False
        import pydevd
        pydevd.settrace(app.config.get('DEBUG_SERVER_HOST', 'localhost'), port=app.config.get('DEBUG_SERVER_PORT', 51234), stdoutToServer=True, stderrToServer=True)
        print "STARTED IN REMOTE DEBUG MODE"

    initialise()

# most of the imports should be done here, after initialise()
from flask import render_template, redirect, url_for, abort, send_file
from octopus.lib.webapp import custom_static
from service import models
from octopus.modules.cache import cache

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/score/<identifier>")
def score(identifier):
    score = models.Score.pull_by_issn(identifier)
    if score is None:
        score = models.Score.pull(identifier)
    if score is None:
        abort(404)

    if score.score_id != identifier:
        return redirect(url_for("score", identifier=score.score_id))

    return render_template("score.html", score=score)

@app.route("/api")
def apidox():
    return render_template("api.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/sponsors")
def sponsors():
    return render_template("sponsors.html")

@app.route("/csv")
def csv():
    cf = cache.load_file("csv")
    if cf is None:
        abort(404)
    return send_file(cf.path, mimetype="text/csv", as_attachment=True, attachment_filename=cf.filename + ".csv")

# this allows us to override the standard static file handling with our own dynamic version
@app.route("/static/<path:filename>")
def static(filename):
    return custom_static(filename)

# this allows us to serve our standard javascript config
from octopus.modules.clientjs.configjs import blueprint as configjs
app.register_blueprint(configjs)

# mount the crud and the search at the same root
from octopus.modules.crud.api import blueprint as crud
app.register_blueprint(crud, url_prefix="/api")

from octopus.modules.es.searchapi import blueprint as searchapi
app.register_blueprint(searchapi, url_prefix="/api")

from octopus.modules.es.query import blueprint as query
app.register_blueprint(query, url_prefix="/query")
app.register_blueprint(query, url_prefix="/account_query")

# adding account management, which enables the login functionality
from octopus.modules.account.account import blueprint as account
app.register_blueprint(account, url_prefix="/account")

from service.views.admin import blueprint as admin
app.register_blueprint(admin, url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'], threaded=False)

