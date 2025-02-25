maths operations:
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))



print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

string concatenation:


a = input("Enter your first name: ")
b = input("Enter your last name: ")
print('Hello', a + ' ' + b + '! Welcome to the Python program.')


Even or odd:



Num = int(input("Enter an integer: "))

# Checking whether the number is even or odd
if Num % 2 == 0:
    print(f"{Num} is an even number.")
else:
    print(f"{Num} is an odd number.")

 range of 1 to 51
# Initialize sum variable
total_sum = 0

# Iterate over numbers from 1 to 50
for num in range(1, 51):
    total_sum += num  # Add each number to total_sum

# Display the final sum
print("The sum of numbers from 1 to 50 is:", total_sum)
