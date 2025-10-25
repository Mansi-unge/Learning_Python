# Python Set Example
# Problem: Can we put a list [7,1] inside a set?

# This will give an error:
# s = {14, 5, 3, "mansi", [7,1]}
# TypeError: unhashable type: 'list'
# Reason: Sets can only contain immutable (unchangeable) items.
# Lists are mutable, so Python cannot put them in a set.

# ✅ Correct way: Use a tuple instead of a list
s = {14, 5, 3, "mansi", (7,1)}
print(s)
# Output: {14, 3, 5, 'mansi', (7, 1)}

# Note:
# - Tuple (7,1) is immutable, so it can be added to a set.
# - You cannot change values inside the tuple once it's in the set.
#   For example: (7,1)[0] = 10  --> This will give an error

# Summary:
# Sets = only immutable items (int, str, tuple)
# Lists, dicts, sets cannot go inside a set.
