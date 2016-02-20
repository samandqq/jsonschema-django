from libs.common.exception import JsonValidationException
import dump.jsonschema
from dump.jsonschema import FormatChecker
from libs.cons import schemas
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import ugettext_lazy as _


class JsonValidationException(APIException):
    """
    APIException class for exception of json validation moduleS
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('json validation error.')

    def __init__(self, errors, detail=None):
        APIException.__init__(self, detail)
        self.errors = errors



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

    return dump.jsonschema.validators.extend(
        validator_class, {"properties": set_defaults})


class JSONSchemaParser(JSONParser):
    """
    Parses JSON-serialized data with schema
    """

    def parse(self, stream, media_type=None, parser_context=None):
        print "--------in parse"
        data = super(JSONSchemaParser, self).parse(stream, media_type, parser_context)
        try:
            default_validating_draft4_validator = extend_with_default(dump.jsonschema.Draft4Validator)
            v = default_validating_draft4_validator(schemas.json[parser_context['view'].schema_name])
            v.format_checker = FormatChecker()

            errors = []
            for error in sorted(v.iter_errors(data), key=str):
                errors.append('{}'.format(error.message))
            if bool(errors):
                raise JsonValidationException(errors)
        except ValueError as error:
            raise ParseError(detail=error.message)
        except dump.jsonschema.exceptions.ValidationError as error:
            raise ParseError(detail=error.message)
        else:
            return data
