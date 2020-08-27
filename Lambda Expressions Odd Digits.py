form functools import reduce
   my_list= [1,2,3]

def only_odd(item):
   return item%2!=0

print(list(filter(lambda item: item%2!=0, my_list)))

print(my_list)