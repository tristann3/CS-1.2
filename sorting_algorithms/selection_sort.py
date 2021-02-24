def selection_sort(lst):
  ''' This is an implementation of a selection sort '''
  n = len(lst)
  passes = n - 1

  # Loop for n-1 times
  for i in range(passes):

    # initially assumes the first element (index 0) is the max
    max_val_index = 0

    for j in range(0, n - i):

      current = lst[j]
      print(f'Current Element: {current}')
      print(f'Current Max: {lst[max_val_index]}')
      if current > lst[max_val_index]:
        max_val_index = j
        print(f'Found new max val {current} at index {j}')

    print(f'Old List: {lst}')
    last_index = passes - i
    lst[max_val_index], lst[last_index] = lst[last_index], lst[max_val_index]
    print(f'New List: {lst}')

    print("----------")

def recursive_selection_sort(A, index, n):
  min = index
  for j in range(index + 1, n):
    if A[j] < A[min]:
      min = j
  A[index], A[min] = A[min], A[index]

  if index + 1 < n:
    recursive_selection_sort(A, index + 1, n)

  return(A)

print(recursive_selection_sort([4, 2, 7, 1, 3], 0, 5))