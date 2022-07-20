"""
@Aaron and @yaw
"""


def pyramid_one_side(num):
    res = []
    for i in range(num+1):
        asteric_num = i+1
        pattern = "*" * asteric_num + "\n"
        res.append(pattern)
    return "".join(res)



def pyramid_space_between(num):
    res = []
    cnt = num - 1
    bottom = num+(num-1)
    for i in range(1, (bottom) + 1, 2):
        if i==1:
            res.append(" "*num + "*" +"\n")
            cnt -= 1
            continue
        pattern = " " * (cnt) + "*" + " " * i + "*" + "\n"
        res.append(pattern)
        cnt -= 1
    return "".join(res)



#in ascending order
def pyramid_nums_between(num):
    res = []
    cnt = num - 1
    bottom = num+(num-1)
    middle_num = 1
    j,k = 2, 0

    for i in range(1, (bottom) + 1, 2):
        num_length = len(str(middle_num))
        if num_length == 1:
            if i==1:
                res.append(" "*num + "*" +"\n")
                cnt -= 1
                continue
            pattern = " " * (cnt) + "*" + (" " * (i-j)) + str(middle_num) + (" " * (i-j)) + "*" + "\n"
            j += 1
            middle_num += 1
            res.append(pattern)
            cnt -= 1
        else:
            k = num_length - (num_length-1)
            if i==1:
                res.append(" "*num + "*" +"\n")
                cnt -= 1
                continue
            pattern = " " * (cnt) + "*" + (" " * (i-j-k)) + str(middle_num) + (" " * (i-j)) + "*" + "\n"
            j += 1
            middle_num += 1
            res.append(pattern)
            cnt -= 1
    return "".join(res)


#In descending order
def pyramid_nums(num):
    res = []
    cnt = num - 1
    bottom = num+(num-1)
    middle_num = num
    j,k = 2, 0

    for i in range(1, (bottom) + 1, 2):
        num_length = len(str(middle_num))
        if num_length == 1:
            if i==1:
                res.append(" "*num + "*" +"\n")
                cnt -= 1
                continue
            pattern = " " * (cnt) + "*" + (" " * (i-j)) + str(middle_num) + (" " * (i-j)) + "*" + "\n"
            j += 1
            middle_num -= 1
            res.append(pattern)
            cnt -= 1
        else:
            k = num_length - (num_length-1)
            if i==1:
                res.append(" "*num + "*" +"\n")
                cnt -= 1
                continue
            pattern = " " * (cnt) + "*" + (" " * (i-j-k)) + str(middle_num) + (" " * (i-j)) + "*" + "\n"
            j += 1
            middle_num -= 1
            res.append(pattern)
            cnt -= 1
    return "".join(res)



def pyramid(num):
    res = []
    for i in range(num+1):
        asteric_num = i+1
        pattern = "  " * ((num-i)//2) + "*" * asteric_num + "\n"
        res.append(pattern)
    return "".join(res)



def main():
    print("Please input a number:")
    try:
        t = int(input())
        print(pyramid(t))
        print(pyramid_one_side(t))
        print(pyramid_space_between(t))
        print(pyramid_nums_between(t))
        print(pyramid_nums(t))
    except ValueError:
        print("Invalid input!!")
        main()


import os
if __name__ == "__main__":
    os.system("cls")
    main()

