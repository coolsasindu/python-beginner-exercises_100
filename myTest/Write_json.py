import json
# a = json.dumps({"name": "Rahul","age": 15,"brothers": None,
#                  "cars": [{"model": "Mercedes-Benz", "mpg": 27.5},{"model": "Ferrari", "mpg": 24.1}]},
#                sort_keys=True, indent=2)
# print(a)
# print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=2))

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])