# Implicit Type Conversion

a = 10
b = 1.75
print('a + b =', a + b) # 11.75
print('type of (a + b) is', type(a + b)) # float

c = '2'
# print('a + c = ', a + c)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Explicit Conversion: int(), float(), str()

print('Convert c from string to number:', int(c))
