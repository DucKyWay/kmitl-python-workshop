score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
elif score < 50:
    print("Grade F")
elif score < 60:
    print("Grade D")
elif score < 70:
    print("Grade C")
elif score < 80:
    print("Grade B")
else:
    print("Grade A")
