import os

def pyramid_one_side(num):
    res = []
    for i in range(1, num+1):
        pattern = "*" * i + "\n"
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
    pass



def pyramid(num):
    res = []
    cnt = num - 1
    bottom = num+(num-1)
    for i in range(1, (bottom) + 1, 2):
        pattern = " " * cnt + "*" * i + "\n"
        res.append(pattern)
        cnt -= 1
    return "".join(res)



def main():
    try:
        t = int(input())
        print(pyramid_one_side(t))
        print(pyramid_space_between(t))
        print(pyramid(t))
        print(pyramid_nums_between(t))
    except ValueError:
        print("Invalid input!!")
        main()



if __name__ == "__main__":
    os.system("clear")
    main()

"""
if user input is for example 5
output>>
1.
     *
    ***
   *****
  *******
 *********
2.
*
**
***
****
*****

3.

     *
   *   *
  *     *
 *       *
*         *

4.

     *
   * 1 *
  *  2  *
 *   3   *
*    4    *

5.

     *
   * 1 *
  *  2  *
 *   3   *
*    4    *

process

difference in space [num-1]---> *
                               ***
                              *****
                             *******
bottom [num+= num-1]--->    *********

"""
