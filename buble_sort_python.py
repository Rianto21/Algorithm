import random

user_input = int(input("Masukan jumlah elemen dalam list: "))

arr = list()

for i in range (user_input): # make random list
  arr.append(random.randint(0, 9))

print(f"{'Unsorted List': <15}: {arr}") #printf with unsorted list is left text align using 15 char space and print arr

sorted_arr = arr.copy() #make copy

for i in range(0, len(sorted_arr)): # buble sorting
  for j in range(i, len(sorted_arr)):
    if sorted_arr[i] > sorted_arr[j]: # > ascending or < descending
      sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i] # swap if follow

print(f"{'sorted List': <15}: {sorted_arr}") #printf with sorted list is left text align using 15 char space and print sorted_arr
