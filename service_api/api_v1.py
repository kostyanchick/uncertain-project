from flask import Blueprint
from flask import Flask

from service_api.views.hello_view import HelloUserView, HelloWorldView


def load_api(app: Flask):

    api_prefix = "/{service_name}/v1".format(service_name=app.config.get('SERVICE_NAME'))
    api_v1 = Blueprint("v1", __name__, url_prefix=api_prefix)

    api_v1.add_url_rule('/', view_func=HelloWorldView.as_view('home'))
    api_v1.add_url_rule('/hello_world', view_func=HelloWorldView.as_view('hello_world'))
    api_v1.add_url_rule('/hello/<user_name>', view_func=HelloUserView.as_view('hello_user'))

    app.register_blueprint(api_v1)


