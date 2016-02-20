# jsonschema with django example
JSONSchema is Common data format definition library, – Clear, human- and machine-readable data format definition  
* Use JSONSchema for input validation  
– Strong validation, then avoid internal errors  
– Return useful error message if a client sends invalid format data  
– Clean up logic code by separating validation code  
– Validation code also can be reduced  

[Understanding JSON Schema pdf](http://spacetelescope.github.io/understanding-json-schema/UnderstandingJSONSchema.pdf)<br />  

## Requirements
* Python 2.7+
* Django 1.9+
* jsonschema 2.5+


### The below are two brief example of how to using jsonschema integrate with django: 'middleware' or 'parsers' they are alternative.  ###

* way 1: middleware.py is an example shows how to use django middleware to validate json with jsonschema.  
            """ add following to Django settings """  
            MIDDLEWARE_CLASSES += (  
                 ....  
              'webapi.middleware.JsonMiddleware',  
            )  
  

* way 2: parsers.py using speical parser to vaildate json with jsonschema  
            """ add following to Django settings """  
            REST_FRAMEWORK = {  
              'DEFAULT_PARSER_CLASSES': (  
                    'xxx.xxx.JSONSchemaParser',          
                 )  
            }

