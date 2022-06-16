kwargs_length = lambda **x: len(x)

dictionary = {"name": "Peter", "age": 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
