# jsonschema-django
## middleware.py is an example shows how to use django middleware to validate json with jsonschemal.

## parsers.py using speical parser to vaildate json with jsonschemal

""" add following to Django settings """  
REST_FRAMEWORK = {  
    'DEFAULT_PARSER_CLASSES': (  
        'xxx.xxx.JSONSchemaParser',          
    )  
}

