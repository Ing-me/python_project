# This program create a right triangle

for i in range(1, 6):
    print("* " * i)

print("")

# Inverted right triangle
for i in range(5, 0, -1):
    print("* " * i)

# Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
    
print("")

# Inverted pyramyd
n = 5
for i in range(n, 0, -1):
    print(" " * (n -i) + "* " * i)

print("square")
for i in range(6):
    str = ""
    for j in range(6):
        str +="* "
    print(str)
    