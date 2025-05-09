#chatgpt code
n = int(input("Enter a number: "))
original = n
count = len(str(n))  # Number of digits
sum = 0

# Use a single for loop to extract digits and compute sum of powers
for i in range(count):
    digit = n % 10
    sum += digit ** count
    n = n // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")