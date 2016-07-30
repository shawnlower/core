from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


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

