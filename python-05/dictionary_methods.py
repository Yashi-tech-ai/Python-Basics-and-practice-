marks = {
    "Yashi" : 100,
    "Anay"  : 90,
    "rohan" : 56,
    0 : 54.6
}
print(marks.items()) # gives all the items in it

# print(marks.keys()) gives all the keys

#  print(marks.values()) #gives all the values

# print(marks.update({"Yashi" : 99})) updates marks can also add stuff 

# print(marks.get("Anay")) prints the value for anay

# print(marks.get("Anay2")) returns none 

# print(marks["rohan2"]) returns error

# a = {"name": "Bambi", "age": 19}
 # clear()
# # a.clear()  → a becomes {}

 # copy()
# b = a.copy()  # b is a clone of a

#  fromkeys()
# keys = ["a", "b", "c"]
# default_dict = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

 # get()
# print(a.get("name"))       # Bambi
# print(a.get("height", "N/A"))  # N/A

 # items()
# for key, value in a.items():
#     print(key, value)

# keys() and values()
# print(list(a.keys()))   # ['name', 'age']
# print(list(a.values())) # ['Bambi', 19]

 # pop()
# a.pop("age")  # Removes age

 # popitem()
# a.popitem()  # Removes last item inserted

 # setdefault()
# marks.setdefault("gender", "female")  # Adds gender if not already there
# print(marks)

# # update()
# a.update({"country": "India", "language": "Python"})

