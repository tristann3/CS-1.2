def insertion_sort(lst):
  ''' This is an implementation of an insertion sort '''

  for index in range(1, len(lst)):

    current_value = lst[index]
    position = index

    while position > 0 and current_value < lst[position - 1]:
      lst[position] = lst[position - 1]
      position -= 1

    lst[position] = current_value

  return lst

answer = insertion_sort([13, 4, 9, 5, 3, 16, 12])
print(answer)