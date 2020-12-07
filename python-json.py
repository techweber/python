# convert from json to python
#import json
# x = '{"name": "John", "age" : 30, "city": "New York"}'
# y = json.loads(x)
# print(y["age"])

# convert from python to json
import json
# x = {
# 	"name" : "John",
# 	"age" : 30,
# 	"city" : "New York"
# }

# y = json.dumps(x)

# print(y)

# print(json.dumps(42))
# print(json.dumps("New York"))
# print(json.dumps(True))
# print(json.dumps(None))
x = {
	"name" : "John",
	"age" : 30,
	"city" : "New York"
}
json.dumps(x,sort_keys = True)
print(x)