letter = "yashi" 
# yashi is string
#len(string) = to give string
#string.endswith("hi") = this will give true
#string.startsswith("ya") = this will give true
#string.capatalize() = gives the word with first letter capital
name = "Yashi"
print(name.lower())  # Output: yashi
print(name.capitalize())
shout = "don't yell"
print(shout.upper())  # Output: DON'T YELL
text = "   hello there   "
print(text.strip())  # Output: "hello there"
line = "I love Java"
print(line.replace("Java", "Python"))  # Output: I love Python
data = "apple,banana,cherry"
print(data.split(","))  # Output: ['apple', 'banana', 'cherry']
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # Output: apple, banana, cherry
quote = "be kind to every kind"
print(quote.find("kind"))  # Output: 3 (first 'kind' starts here)
song = "midnight rain"
print(song.startswith("midnight"))  # True
print(song.endswith("rain"))        # True
lyrics = "la la la la"
print(lyrics.count("la"))  # Output: 4
#string.find(word)
