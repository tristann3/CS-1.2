def bubble_sort(lst):
  ''' This is an implementation of bubble sort '''
  n = len(lst)
  passes = n - 1

  # repeats process n-1 times
  for i in range(passes):
    
    for j in range(0, passes, -1):

      #If current element is greater than whats next
      if lst[j] > lst[j+1]:

        # This assigns the two variables at the same time to avoid overriding
        lst[j], lst[j+1] = lst[j+1], lst[j] 
  return lst