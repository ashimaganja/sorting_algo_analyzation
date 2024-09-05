from datetime import datetime

def time_complexity(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(func(*args, **kwargs))

        end = datetime.now()
        print(f"Time complexity: {end-start}")
    return wrapper

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

@time_complexity
def insertion_sort(A):
    i = 1
    for j in range(i,len(A)):
        insertion(A,j)
    return A


A = [2,5,3,6,200,31,545,100,7,1,0,222,976, 334,54546,656676,345,32,45234532,656,7645532,52,3525245,56,76,7664,6,345,21,424,54236,576,7456,353,2436,547,8,6586,75,643,56354,634,563,45634,4353,456534,56,345667,787,898,87,7]

B = insertion_sort(A)

print(B)