from collections import defaultdict
from wsgiref.util import application_uri

word = ["Apple", "banana", "Avocado", "cherry", "apricot", "blueberry", "Coconut"]

groups=defaultdict(list)

for word in words:
    key=word[0].lower()
    groups[key].append(word)

for letter in groups:
    groups[letter].sort()

    