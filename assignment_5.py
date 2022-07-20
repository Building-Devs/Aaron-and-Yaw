num = int(input("Number of rows to generate: "))

row = 0
outside_space = " "
inside_space = " "

while row < num:
    row+= 1
    if row == 1:
        print((outside_space * (num)) + (" *" * row))
    else:
        indent = num - row
        print(f"{(outside_space * indent)}*{inside_space * row}{row-1}{inside_space * row}*")

