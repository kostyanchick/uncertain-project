from http import HTTPStatus

from service_api.views.base_view import BaseView


class HelloWorldView(BaseView):
    """View returning page with text 'Hello World!'"""

    def get(self):
        result = {'message': "Hello World!"}
        status = HTTPStatus.OK.value
        response = self._get_response(result, status)
        return response, status


class HelloUserView(BaseView):
    def get(self, user_name):
        result = {'message': f"Hello, {user_name}!"}
        status = HTTPStatus.OK.value
        response = self._get_response(result, status)
        return response, status
