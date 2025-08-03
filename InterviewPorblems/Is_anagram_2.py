from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())


if __name__ == "__main__":
    user_input = input("Enter words seperated by space: ").strip()
    words = user_input.split()
    result = group_anagrams(words)

    for group in result:
        print(group)