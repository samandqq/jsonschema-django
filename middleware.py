import json

from django import http
from rest_framework import status as HTTP_STATUS
import jsonschema
from jsonschema import FormatChecker
from libs.cons import schemas


def extend_with_default(validator_class):
    """
    In this code, we add the default properties to each object before the properties are validated,
    so the default values themselves will need to be valid under the schema.
    "
    :param validator_class:
    :return:
    """
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for error in validate_properties(validator, properties, instance, schema):
            yield error
        for property, subschema in properties.iteritems():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

    return jsonschema.validators.extend(
        validator_class, {"properties": set_defaults})


class JsonMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Parse JSON in POST, PUT and PATCH requests.
        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                data = json.loads(request.body)
                default_validating_draft4_validator = extend_with_default(jsonschema.Draft4Validator)
                v = default_validating_draft4_validator(
                    schemas.json[view_func.__name__ + "." + request.method.lower()])
                v.format_checker = FormatChecker()

                errors = []
                for error in sorted(v.iter_errors(data), key=str):
                    errors.append('{}'.format(error.message))
                if bool(errors):
                    return http.HttpResponse(
                        json.dumps({"errors": errors}, indent=4), content_type="application/json",
                        status=HTTP_STATUS.HTTP_400_BAD_REQUEST
                    )
                setattr(request, 'parsed_json', data)
            except ValueError as error:
                return http.HttpResponse(json.dumps({"error": [
                    'Input validation error - {0}'.format(error.message)]}, indent=4),
                    content_type="application/json",
                    status=HTTP_STATUS.HTTP_400_BAD_REQUEST
                )

        return None
