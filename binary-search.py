# Python 3 program for recursive binary search. 
# Modifications needed for the older Python 2 are found in comments. 
  
# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
        print(f'Index: {mid} is {arr[mid]}')

  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Test array 
arr = [3, 8, 12, 34, 54, 84, 91, 110] 
x = 54
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 

def low_and_high(arr):
  low = 1000000000
  high = -1
  for num in arr:
    #low num
    if low > num:
      low = num
  for num in arr:
    if high < num:
      high = num
  print(f"Low: {low} High: {high}")

low_and_high([3, 8, 12, 34, 54, 84, 91, 110])


# Recursive Python3 code to sort 
# an array using selection sort 
  
# Return minimum index 
def minIndex( a , i , j ): 
    if i == j: 
        return i 
          
    # Find minimum of remaining elements 
    k = minIndex(a, i + 1, j) 
      
    # Return minimum of current  
    # and remaining. 
    return (i if a[i] < a[k] else k)

# Recursive selection sort. n is  
# size of a[] and index is index of  
# starting element. 
def recurSelectionSort(a, n, index = 0): 
  
    # Return when starting and  
    # size are same 
    if index == n: 
        return -1
          
    # calling minimum index function  
    # for minimum index 
    k = minIndex(a, index, n-1) 
      
    # Swapping when index and minimum  
    # index are not same 
    if k != index: 
        a[k], a[index] = a[index], a[k] 
          
    # Recursively calling selection 
    # sort function 
    recurSelectionSort(a, n, index + 1) 

# Driver code 
arr = [3, 1, 5, 2, 7, 0] 
n = len(arr) 
  
# Calling function 
recurSelectionSort(arr, n) 

# printing sorted array 
for i in arr: 
    print(i, end = ' ') 