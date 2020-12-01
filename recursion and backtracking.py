def printFunc(n):
    if n == 0:   #this is terminating based case
        return 0
    else:
        print(n)
        return printFunc(n-1) #recursion call to itself again
print(printFunc(4))
print(printFunc(14))
print(printFunc(40))

#given an array,check whether the array is in sorted order with recursion.
def isArrayInSortedOrder(A):
    #Base case
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])
A = [123,23,233,434,43534,3,45,543]
print(isArrayInSortedOrder(A)) 

