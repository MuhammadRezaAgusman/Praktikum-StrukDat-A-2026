x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)

#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#slicing strings
b = "Hello, World!"
print(b[2:6])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:-1])

#uppercase string 
a = "Hello, World!"
print(a.upper())

#remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#split the string
a = "Hello, World!,,"
print(a.split(",")) # returns ['Hello', ' World!']