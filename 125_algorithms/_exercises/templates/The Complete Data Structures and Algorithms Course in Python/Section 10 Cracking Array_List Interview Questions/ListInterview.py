#   Created by Elshad Karimov on 15/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Question 1

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


___ findMissing(list, n
    sum1 = sum(list)
    sum2 = 100*101/2
    print(sum2-sum1)


# findMissing(mylist, 100)

# Question 2
___ findPairs(list, sum
    ___ i __ range(le_(list)):
        ___ j __ range(i+1,le_(list)):
            __ (list[i]+list[j]) __ sum:
                print(list[i],list[j])
# findPairs(mylist, 100)


# Question 3
import numpy as np 
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

___ findNumber(array, number
    ___ i __ range(le_(array)):
        __ array[i] __ number:
            print(i)

findNumber(myArray, 12)

# Question 3

___ findMaxProduct(array
    maxProduct = 0
    ___ i __ range(le_(array)):
        ___ j __ range(i+1,le_(array)):
            __ array[i]*array[j] > maxProduct:
                maxProduct = array[i]*array[j]
                pairs = str(array[i])+ "," + str(array[j])
    print(pairs)
    print(maxProduct)

findMaxProduct(myArray)



#Question 5 - isqunieuq
___ isUnique(list
  a=[]
  ___ i __ list:
    __ i __ a:
        print(i)
        r_ F..
    ____
        a.ap..(i)
  r_ T..

print(isUnique(myList))



#Question 6 - permutation

___ permuntation(list1, list2
    print(list1)
    print(list2.reverse())
    __ list1 __ list2:   # if list1 == list2.reverse() -- false
        r_ T..
    ____
        r_ F..

# print(permuntation([1,2,3], [3,2,1]))


# Question 7

___ rotate_matrix(matrix
    '''rotates a matrix 90 degrees clockwise'''
    n = le_(matrix)
    ___ layer __ range(n // 2
        first, last = layer, n - layer - 1
        ___ i __ range(first, last
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    r_ matrix

matrix = [[1,2], [3,4]]
print(matrix)
print(rotate_matrix(matrix))