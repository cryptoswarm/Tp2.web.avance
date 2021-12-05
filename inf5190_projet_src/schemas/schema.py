from flask import request, jsonify, current_app
from functools import wraps
from jsonschema import validate
from jsonschema import exceptions
from jsonschema.exceptions import ErrorTree, ValidationError
from jsonschema.validators import Draft3Validator, Draft4Validator, Draft7Validator


edit_glissade = {
  "type": "object",
  "properties": {
    "name": {"type": "string", "minLength": 1},
    "date_maj": {
        "type": "string", 
        "format": "date-time"
        # "oneOf":[
        #     {
        #         "pattern": "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])\s*(0[0-9]|1[0-9]|2[0-3])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$"
        #     },
        #     {
        #         "pattern": "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])T(0[0-9]|1[0-9]|2[0-3])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$"
        #     },
        #     {
        #         "pattern":"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])\s*(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$"
        #     }
        # ]
    },
    "ouvert": {
        "type": "string", 
        "enum":["0", "1"]
    },
    "deblaye": {
        "type": "string", 
        "enum":["0", "1"]
    },
    "condition": {
        "type": "string", 
        "minLength": 1
    },
    "arrondissement_id": {"type": "integer"},
  },
  "required": ["name", "date_maj", "ouvert", "deblaye", "condition", "arrondissement_id"],
  "additionalproperties": False

}

create_profile = {
  "type": "object",
  "properties": {
    "complete_name": {"type": "string", "minLength": 4},
    "email": {"type": "string"},
    "followed_arr": {
      "type": "array",
      "items": {
                  "type": "string",
                  "minLength": 3
              },
      "minItems": 1
      }
  },
  "required": ["complete_name", "email", "followed_arr"],
  "additionalproperties": False
}


def validate_schema(request, schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            response = []
            try:
                with current_app.app_context():
                  validate(request.get_json(), schema) 
            except ValidationError as err:
              raise err
            return f(*args, **kw)
        return wrapper
    return decorator