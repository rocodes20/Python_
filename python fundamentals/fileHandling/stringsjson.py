import json

json_Str = '{ "name":"rohit","age":20,"ismajor":true }'

py_object = json.loads(json_Str)
print(py_object)

js_Str = json.dumps(py_object)
print(js_Str)