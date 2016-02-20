# jsonschema-django
There are two ways using jsonschemal integrate with django 'middleware' or 'parsers'.

* middleware.py is an example shows how to use django middleware to validate json with jsonschemal.  
            """ add following to Django settings """  
            MIDDLEWARE_CLASSES += (
              \....
              'webapi.middleware.JsonMiddleware',
            )  
  

* parsers.py using speical parser to vaildate json with jsonschemal

            """ add following to Django settings """  
            REST_FRAMEWORK = {  
              'DEFAULT_PARSER_CLASSES': (  
                    'xxx.xxx.JSONSchemaParser',          
                 )  
            }

