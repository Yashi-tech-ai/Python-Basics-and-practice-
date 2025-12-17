a = {"name": "Bambi", "age": 19}

# clear()
# a.clear()  → a becomes {}

# copy()
b = a.copy()  # b is a clone of a

# fromkeys()
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

# get()
print(a.get("name"))       # Bambi
print(a.get("height", "N/A"))  # N/A

# items()
for key, value in a.items():
    print(key, value)

# keys() and values()
print(list(a.keys()))   # ['name', 'age']
print(list(a.values())) # ['Bambi', 19]

# pop()
a.pop("age")  # Removes age

# popitem()
a.popitem()  # Removes last item inserted

# setdefault()
a.setdefault("gender", "female")  # Adds gender if not already there

# update()
a.update({"country": "India", "language": "Python"})
