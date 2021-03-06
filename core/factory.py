"""
    core.factory
    ~~~~~~~~~~~~

    core factory module

"""

from flask import Flask
from .helpers import register_blueprints

def create_app(package_name, package_path, settings_override=None):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the core platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    """

    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('core.settings')
    app.config.from_pyfile('settings.cfg', silent=True)

    register_blueprints(app, package_name, package_path)

    return app
