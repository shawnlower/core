from flask import Flask, request
from core import factory

app = factory.create_app(__name__)
print("Debug is set to: {}".format(app.config['DEBUG']))


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello from {}'.format(__name__)

@app.route('/', methods=['PUT', 'POST'])
def count_bytes():
    """Count the number of bytes sent by the user."""
    return 'Received %s bytes' % len(request.get_data())

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

