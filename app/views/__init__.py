from flask import Flask

from .lead_view import bp

def init_app(app: Flask):
    app.register_blueprint(bp)
