# jsonschema-django
JSONSchema is Common data format definition library, – Clear, human- and machine-readable data format definition  
* Use JSONSchema for input validation  
– Strong validation, then avoid internal errors  
– Return useful error message if a client sends invalid format data  
– Clean up logic code by separating validation code  
– Validation code also can be reduced  

### There are two ways using jsonschemal integrate with django 'middleware' or 'parsers'.  ###

* middleware.py is an example shows how to use django middleware to validate json with jsonschemal.  
            """ add following to Django settings """  
            MIDDLEWARE_CLASSES += (  
                 ....  
              'webapi.middleware.JsonMiddleware',  
            )  
  

* parsers.py using speical parser to vaildate json with jsonschemal  
            """ add following to Django settings """  
            REST_FRAMEWORK = {  
              'DEFAULT_PARSER_CLASSES': (  
                    'xxx.xxx.JSONSchemaParser',          
                 )  
            }

