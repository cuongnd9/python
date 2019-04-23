numbers = {1, 5, 6, 8, 85, 'ten'}

print(numbers)
numbers.add(7)
print(numbers)
numbers.update([1, 5, 8])
print(numbers)
numbers.remove(1)
print(numbers)

A = {1, 2, 3}
B = {2, 3, 4, 5}

# Equivalent to A.union(B) 
# Also equivalent to B.union(A)
print(A | B) # Output: {1, 2, 3, 4, 5}

# Equivalent to A.intersection(B)
# Also equivalent to B.intersection(A)
print (A & B) # Output: {2, 3}

# Set Difference
print (A - B) # Output: {1}

# Set Symmetric Difference
print(A ^ B)  # Output: {1, 4, 5}
