#string slicing  = process of pulling out a specific part of a string using its index numbers
name = "Yashi"
# length_of_string = len(name)
# print(length_of_string)
# shortname = name[3] # when counted from left to right start from 0 and from right to left then -1,-2,-3 ...
# sliced_string = name[0:3] # start from 0 to 3 (excluding 3)
# print(sliced_string)

# negative slicing 
sliced_string = name[-4:-1] # excludes - 1
print(sliced_string)
sliced_string2 = name[:4] #means [0:4]
print(sliced_string2)
sliced_string3 = name[1:5] 
print(sliced_string3)
sliced_string4 = name[1:] # same as [1:5]
print(sliced_string4)
# sliced_string5 = name[-1:-4]
# print(sliced_string5) = error 