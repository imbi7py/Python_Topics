#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# flatten Solution
___ flatten(arr
    resultArr = []
    ___ custItem __ arr:
        __ ty..(custItem) __ li__:
            resultArr.ex..(flatten(custItem))
        ____
            resultArr.ap..(custItem)
    r_ resultArr 



print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]