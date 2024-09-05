
def insertion(A,j):
    value = A[j] #The value to be inserted is assigned to a variable
    sub_array = A[:j] # create a sub array to run the search on
    i = j - 1
    while  i >= 0:
        if value > A[i]:
            A[j] = value
            break
        else:
            A[j] = A[i]
            i = i-1
            j = j-1

    return A #returns a sorted array of A[1,...,j-1]

def insertion_sort(A):
    i = 1
    for j in range(i,len(A)):
        insertion(A,j)
    return A

A = [2,5,3,6,200,31,545,100,7,1,0,222,976]

print(insertion_sort(A))