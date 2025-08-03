from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


s = input(str("Enter your first input: "))
t = input(str("Enter your second input: "))

print(f"Your inputs {s} & {t} anagram result: {is_anagram(s, t)}")
