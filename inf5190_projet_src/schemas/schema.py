from flask import request, jsonify
from functools import wraps


edit_glissade = {
  "type": "object",
  "properties": {
    "name": {"type": "string", "minLength": 1},
    "date_maj": {
        "type": "string", 
        "oneOf":[
            {
                "pattern": "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])\s*(0[0-9]|1[0-9]|2[0-3])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$"
            },
            {
                "pattern": "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])T(0[0-9]|1[0-9]|2[0-3])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$"
            },
            {
                "pattern":"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])\s*(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$"
            }
        ]
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
  "required": ["name", "date_maj", "ouvert", "deblaye", "condition", "arrondissement_id"]
}


# def required_params(required):
#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             _json = request.get_json()
#             missing = [r for r in required.keys() if r not in _json]
#             if missing:
#                 response = {
#                 "status": "error",
#                 "message": "Request JSON is missing some required params",
#                 "missing": missing
#                                   }
#                 return jsonify(response), 400
#             wrong_types = [r for r in required.keys() if not isinstance(_json[r], required[r])]
#             if wrong_types:
#                 response = {
#                 "status": "error",
#                 "message": "Data types in the request JSON doesn't match the required format",
#                 "param_types": {k: str(v) for k, v in required.items()}
#                 }
#                 return jsonify(response), 400
#             return fn(*args, **kwargs)
#         return wrapper
#     return decorator