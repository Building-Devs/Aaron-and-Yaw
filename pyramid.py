import os

def pyramid_one_side(num):
    res = []
    for i in range(1, num+1):
        pattern = "*" * i + "\n"
        res.append(pattern)
    return "".join(res)

def pyramid_space_between(num):
    pass

#in ascending order
def pyramid_nums_between(num):
    pass
#In descending order
def pyramid_nums(num):
    pass

def pyramid(num):
    pass


"""
if user input is for example 5
output>>
1.
    *
    **
   ***
  ****
 *****
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


"""
