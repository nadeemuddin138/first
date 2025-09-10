def sum_with_for_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage:
num = int(input("Enter a positive number: "))
if num > 0:
    print(f"Sum using for loop: {sum_with_for_loop(num)}")
else:
    print("Please enter a positive number.")4
