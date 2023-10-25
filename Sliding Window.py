# Subarray of size k with given sum

# Given an array arr[], an integer K and a Sum. The task is to check if there exists any subarray with K elements whose sum is equal to the given sum. If any of the subarray with size K has the sum equal to the given sum then print YES otherwise print NO.
#
# Examples:
#
# Input: arr[] = {1, 4, 2, 10, 2, 3, 1, 0, 20}
#         k = 4, sum = 18
# Output: YES
# Subarray = {4, 2, 10, 2}
#
# Input: arr[] = {1, 4, 2, 10, 2, 3, 1, 0, 20}
#         k = 3, sum = 6
# Output: YES
# SO ONE WAY TO APPROACH THIS IS BY usin sliding window
# a window of size k will be used to check if their sum is equal to the value given to us
def checksubarraysum(arr,n,k,sum):

    currentsum=0

    # SO FOR THE FIRST WINDOW SUM
    for i in range(0,k):
        currentsum+=arr[i]
    if (currentsum==sum):
        return True

    for j in range(k,n):
            currentsum=(currentsum + arr[j]-arr[j-k])
            if currentsum==sum:
                return True
    return False
arr = [1, 4, 2, 10, 2,
           3, 1, 0, 20]
k = 4
sumV = 18

n = len(arr)

if (checksubarraysum(arr, n, k, sumV)):
    print("YES")
else:
    print("NO")
