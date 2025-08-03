def char_frequency(l):
    freq = {}
    for char in l:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


freq = char_frequency("salamlarlarlarlar")

sorted_items = sorted(freq.items(), key=lambda x: x[1])
print(sorted_items)
sorted_alpha = sorted(freq.items(), key=lambda x: x[0])
print(sorted_alpha)
sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)