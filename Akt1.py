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

# Function to get results based on exam numbers
def get_results(exam_numbers):
    results = []
    for number in exam_numbers:
        if number >= 50:
            results.append("Pass")
        else:
            results.append("Fail")
    return results

# Main code
exam_numbers = []
for i in range(3):
    while True:
        try:
            number = int(input(f"Enter the exam number for student {i+1}: "))
            if 0 <= number <= 100:
                exam_numbers.append(number)
                break
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

results = get_results(exam_numbers)

# Display results
for i, result in enumerate(results):
    print(f"Student {i+1} result: {result}")


