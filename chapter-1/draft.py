
items=[1,2,3,4,5,6,6]

def find_target(target):
    for item in items:
        if item == target:
            print(f"Found: {target}")
            break
    else:
        print("Item not found.")  # runs only if no `break` happened

find_target(3)