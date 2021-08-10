# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.fred_routes import fred_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(fred_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)