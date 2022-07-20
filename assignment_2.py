num = int(input("Number of rows to generate: "))
row = 0
print("*")
while row < num:
    row += 1
    if row == 1:
        continue
    else:
        print(" *" * row)
print()
