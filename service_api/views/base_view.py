from http import HTTPStatus

from flask.views import MethodView
from flask import jsonify, make_response


class BaseView(MethodView):

    def _validate_request(self, request):
        pass

    @staticmethod
    def _get_response(data, status=HTTPStatus.OK.value):
        resp_obj = {
            'data': data,
            'status': 'success'
            if (status == HTTPStatus.OK.value or status == HTTPStatus.CREATED.value)
            else 'failed'
        }
        return make_response(jsonify(resp_obj))
