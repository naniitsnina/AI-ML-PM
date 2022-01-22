a = "Hello"
print(a)

# three single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello World"
print(a[1])

# Looping through a String
for x in "banana":
    print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check String in an 'if' statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Example : Print only if "expensive in NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

# Check if NOT
txt = "The best thing in life are free!"
print("expensive" not in txt)