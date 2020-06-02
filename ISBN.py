isbn = [9, 7, 8, 0, 3, 0, 6, 4, 0, 6, 1, 5]

digits = []
i = 1 
while len(digits) < 3:
    digits.append(int(input(f"put digit {i}: ")))

print(digits)

count = 0
for i in digits:
    if (i % 2) == 0:
        digits[count] = 3 * i
    count += 1
print(digits)