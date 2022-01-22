""""
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
"""

# str
x = "Hello World"
print(x)
print(type(x))

# int
x = 20
print(x)
print(type(x))

# float
x = 20.5 
print(x)
print(type(x))
# complex
x = 1j
print(x)
print(type(x))

# list
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

# tuple
x = ("apple", "banana", "cherry")
print(x)
print(type(x))

# range
x = range(6)
print(x)
print(type(x))

# dict
x = {"name" : "John", "age" : 36}
print(x)
print(type(x))

# frozennet
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

# boolean
x = True
print(x)
print(type(x))

# bytes
x = b"Hello"
print(x)
print(type(x))

# bytearray
x = bytearray(5)
print(x)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(x)
print(type(x))
