"""print("Let me learn")
x=input("Enter your name:")
print(x)

# prime number tester
x=input("Enter a number to be tested:")
y=int(x)/2
p=int(x)%2
if p==0:
    print(x+" is not a prime")
else: print("May be prime to be tested")"""

# Function to calculate and return results
def student_results(student_scores):
    results = []
    for index, score in enumerate(student_scores):
        if score >= 50:  # Assuming 50 is the passing mark
            results.append(f"Student {index + 1}: Pass")
        else:
            results.append(f"Student {index + 1}: Fail")
    return results

# Input scores for 3 students
scores = []
for i in range(3):
    score = float(input(f"Enter the marks for Student {i + 1}: "))
    scores.append(score)

# Get and display results
results = student_results(scores)
for result in results:
    print(result)
