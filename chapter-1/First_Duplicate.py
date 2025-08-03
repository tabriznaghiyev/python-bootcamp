def first_duplicate(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)
    return None

print("Duplicate:", first_duplicate([2, 5, 3, 1, 5, 2]))