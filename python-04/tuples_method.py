friends = ("Yashi", "Pink", 5, 33.98,False,"Anay","Job")
# print(friends.count(5))
# index = prints the first occurence index

#operation on tuples
t = (1, 2, 3)
empty = ()
single = (5,)  # <- don’t forget the comma!

t[0]  # 1 indexing 
t[-1] # 3

t[1:]    # (2, 3) slicing 
t[:2]    # (1, 2)
t[::-1]  # (3, 2, 1) ← reverse

a = (1, 2) # concatetaion 
b = (3, 4)
c = a + b
# (1, 2, 3, 4)


#repetition 
a * 3
# (1, 2, 1, 2, 1, 2)


# membership
2 in a      # True
5 not in a  # True

len(t)  # 3 gives length 

list_version = list(t) # conversion 
tuple_again = tuple(list_version)

data = ("Bambi", 19, "Scorpio") # tuple packing and unpacking 
name, age, zodiac = data
# name → 'Bambi'
