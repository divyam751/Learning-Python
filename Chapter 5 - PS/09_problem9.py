# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 9




# The code you provided will raise an error due to a fundamental constraint in Python regarding sets. Specifically, **sets cannot contain mutable objects**, such as lists. Let's break this down:

# ### Explanation:
# - In Python, sets are collections of unique elements that must be **immutable**. This means that the elements inside a set cannot be changed once they are added. For example, numbers, strings, and tuples can be included in a set because they are immutable.
# - However, **lists** are mutable (i.e., you can change their contents after creation). Since sets require all elements to be immutable, you cannot place a list inside a set.

# ### Problem with the code:
# ```python
# s = {8, 7, 12, "Harry", [1, 2]}  # This will raise a TypeError
# ```
# In this case, `[1, 2]` is a list, and trying to include it in the set will result in a `TypeError`:
# ```
# TypeError: unhashable type: 'list'
# ```

# ### Solution:
# If you need to store a similar structure, you could convert the list `[1, 2]` into a tuple (which is immutable) so that it can be placed inside the set.

# ```python
# s = {8, 7, 12, "Harry", (1, 2)}  # Use a tuple instead of a list
# ```

# However, if you still need to modify the contents of a collection, consider using a **list** or **dictionary**, where you can include mutable types like other lists.