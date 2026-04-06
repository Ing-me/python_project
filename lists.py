scores = []
number_score = int(input("How many score wish you enter? "))
i = 1
while number_score > 0:
    score = float(input(f"Enter score {i}: "))
    scores.append(score)
    i += 1
    number_score -= 1

print(scores)