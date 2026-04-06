# This program is about to store students' scores in a list called "scores"
# And different methods are being used to manipulate the list.
# Then the length of the list depends on how many scores the professor insert into the list
print("#" * 40)
print(" " * 5, "Welcome to the advanced list 1" )
print("#" * 40, "\n")

number_scores = int(input("How many scores do you want to store: "))

i = 1
scores = []
while number_scores > 0:
    score = int(input(f"Enter score {i}: "))
    scores.append(score)
    number_scores -= 1
    i += 1

print(f"This is the original scores list: {scores}")

even_indexed_scores = scores[::2];
print(f"This is the score list found at even indexes {even_indexed_scores}")

odd_indexed_scores = scores[1::2]
print(f"This is the score list found at odd indexes {odd_indexed_scores}")

scores.sort()
print(f"This is the sorted scores using the sort() method: {scores}")

sorted_scores = sorted(scores)
print(f"This the sorted scores using the sorted function: {sorted_scores}")

scores.reverse()
print(f"This the reversed scores using the reverse() method: {scores}")

reversed_scores = sorted_scores[::-1]
print(f"This the reversed scores using the -1 method: {reversed_scores}\n")

number = int(input("Enter the score you want to check in the list: "))
is_member = number in scores
if is_member:
    print(f"The score {number} is in the scores.")

count_number = int(input("Enter the number you want to find its occurrence: "))
occurrence_number = scores.count(count_number)
print(f"The score {count_number} appears {occurrence_number} times in the list")

max_score = max(scores)
print(f"The maximum score is {max_score}")

min_score = min(scores)
print(f"The min score is {min_score}")

average_score = sum(scores) / len(scores)
print(f"The average score is: {average_score:.2f}")