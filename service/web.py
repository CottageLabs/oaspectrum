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


from flask import render_template
from octopus.lib.webapp import custom_static

@app.route("/")
def root():
    return render_template("index.html")

# this allows us to override the standard static file handling with our own dynamic version
@app.route("/static/<path:filename>")
def static(filename):
    return custom_static(filename)

# this allows us to serve our standard javascript config
from octopus.modules.clientjs.configjs import blueprint as configjs
app.register_blueprint(configjs)

from octopus.modules.crud.api import blueprint as crud
app.register_blueprint(crud, url_prefix="/api")

from octopus.modules.es.query import blueprint as query
app.register_blueprint(query, url_prefix="/query")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    initialise()
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'], threaded=False)

