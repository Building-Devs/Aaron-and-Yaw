num = int(input("Number of rows to generate: "))
space = " "
indent = 2
row = 0

while row < num:
    row += 1
    print((space * indent) + ("*" * row))
    if row >= 2:
        indent -= 1