a = {1, 2}
b = {2, 3}
print(a.union(b))
print(a.intersection(b))

a = {1, 2, 3}
b = {2, 3}
print(a.difference(b))  # {1}

a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b)) # A △ B = (A ∪ B) - (A ∩ B)

a = {1, 2}
b = {3}
a.update(b)
print(a)  # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)  # {2, 3}

a = {1, 2, 3}
b = {2}
a.difference_update(b)
print(a)  # {1, 3}

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True
print(a <= b)         # True

a = {1, 2, 3}
b = {2}
print(a.issuperset(b))  # True
print(a >= b)           # True

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True . It checks if two sets have NOTHING in common.

f = frozenset([1, 2, 3])
# f.add(4)  # ❌ Error: frozenset is immutable

