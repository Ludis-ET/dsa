from array import *

#1. creating an array and tranverse it
my_array = array('i',[1,2,3,4,5])

for i in my_array:
    print(i) # transversing is listing out all the elements


# 2. access individual elements through indexes


print(f'step 2 -> {my_array[4]}')


# 3. append any value to the array using append() method


my_array.append(6)
print(f'step 3 -> {my_array}')


# 4. insert value in an array using insert() method


my_array.insert(1,22)
print(f'step 4 -> {my_array}')


# 5. extend python array using extend() method

my_2_array = array('i',[10,11,12,13])
my_array.extend(my_2_array)
print(f'step 5 -> {my_array}')


# 6. add items from list into array using fromlist() method


templist = [20,21,22,23]
my_array.fromlist(templist)
print(f'step 6 -> {my_array}')


# 7. remove any array element usign remove() method

my_array.remove(22)
print(f'step 7 -> {my_array}')


# 8. remove last array element using pop() method

my_array.pop()
print(f'step 8 -> {my_array}')


# 9. fetch any element through its index using index() method

print(f'step 9 -> {my_array.index(22)}')


# 10. reverse a python array using reverse() method

my_array.reverse()
print(f'step 10 -> {my_array}')


# 11. get array bufer information through buffer_info() method

print(f'step 11 -> {my_array.buffer_info()}')


# 12. check for number of occurrences of an element using count() method

print(f'step 12 -> {my_array.count(11)}')


# 13. convert an array to string using tostring() method

# strTemp = my_array.tostring()
# print(f'step 13. -> {strTemp}')
# not working

# 14. convert array to list

