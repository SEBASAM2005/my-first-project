
data = input("Enter the numbers separated by a space: ").split()

numbers = [float(num) for num in data]

total = sum(numbers)

average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)
print("\n :Calculation results")
print(f"total: {total}")
print(f"avarage: {average}")
print(f"maximum: {maximum}")
print(f"minimum: {minimum}")
