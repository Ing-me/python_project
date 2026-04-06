fruit_number = int(input("How many fruits do you have? "))

fruits = []
i = 1

while fruit_number > 0:
    fruit = input(f"Enter your fruit number {i}: ")
    fruits.append(fruit)
    i += 1
    fruit_number -= 1

print()
print(f"This is the list of your fruits: {fruits}\n")
print(f"{fruits[0]} is the first fruit in your list.\n")
print(f"{fruits[-1]} is the last fruit in your list. \n")


fruits_copy = fruits[:]
fruits_copy.append("mango")
print(f"This the original list: {fruits}, this is the copied list: {fruits_copy}")

has_cherry = "cherry" in fruits_copy

if has_cherry:
    fruits_copy.remove("cherry")
    print(f"A cherry has been removed from the copied list: {fruits_copy}")

print(f"copy: {fruits_copy}")

fruits_copy.insert(2, "date")
print(f"Your new copied fruits {fruits_copy}")

fruits_copy.sort()
print(f"Your sorted fruits: {fruits_copy}")

fruits_copy.reverse()
print(f"Your reversed fruit list: {fruits_copy}")

print(f"The length of the is: {len(fruits_copy)}")

new_fruits_list = sorted(fruits_copy)
print(f"Your new copied fruit list: {new_fruits_list}")