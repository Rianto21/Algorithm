import random

user_input = int(input("Masukan jumlah elemen dalam list: "))

arr1 = list()

for i in range (user_input): # make random list
  arr1.append(random.randint(0, 9))


print(f"{'Unsorted List': <15}: {arr1}") #printf with unsorted list is left text align using 15 char space and print arr

def find_min_index(arr, start):
  index = start
  for i in range(start, len(arr)):
    if arr[i] < arr[index]:
      index = i
  return index

def selection_sort(arr):
  for i in range(len(arr)) :
    min_index = find_min_index(arr, i)
    if i != min_index:
      arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr

selection_sort(arr1)
print(f"{'sorted List': <15}: {arr1}") #printf with sorted list is left text align using 15 char space and print sorted_arr
