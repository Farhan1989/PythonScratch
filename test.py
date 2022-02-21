#!/usr/bin/python
import math
import random
import numpy as np
# str = "Hello, Python!"
# print(str[-3:-5]);

# tinytuple = (123, 'john');
# tinytuple = tinytuple *2;
# tinytuple[1] = 1000;
# print(tinytuple);


# if True:
#    print ("True");
# else:
#    print ("False");
#    print("False");


# var1 = 100
# if False: print ("1 - Got a true expression value"); print (var1);


# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# print (dict.values());


# age = input("What is your age : ");
# print("Your age after 10 years will be: " + str(int(age) + 10));


# if not(1==2 and 2==2):
#     print("hello");

# if(21 in [12, 13, 14]):
#     print("hello")

# if(21 not in [12,13,14]):
#     print("hello")

# a =10
# b=10

# if(a is b): print("hello")
# print("hello")


# for letter in "Python":     # First Example
#    print ('Current Letter :', letter)


# fruits = ['banana', 'apple',  'mango', 'pineapple']
# for fruit in fruits:        # Second Example
#    print ('Current fruit :', fruit)


# fruits = ['banana', 'apple',  'mango']
# print (len(fruits))

# c = range(3);
# print(c);
# for index in range(len(fruits)):
#     print('Current fruit :', index)
#     print ('Current fruit :', fruits[index])


# c =10
# d =20
# print("I will eat %d icecream. Dania will eat %d icecream"%(c,d))


# print(abs(-16))
# print(math.fabs(-16))
# print(math.modf(16.63))

# print(random.randrange(2, 8, 2));


# var1 = 'Hello World!'
# print (var1[6:-1]);

# var1 = 'Hello World!'
# print (var1[6:]);
# print("H" not in var1);


# aList = [123, 'xyz', 'zara', 'abc'];
# aList.pop(2);
# print(aList);

# aList = [123, 'xyz', 'zara', 'abc', 123];
# aList.remove(123);
# aList.remove(123)
# print(aList);


# # Reshaping 3X4 array to 2X2X3 array
# arr = np.array([[1, 2, 3, 4],
#                 [5, 2, 4, 2],
#                 [1, 2, 0, 1]])

# newarr = arr.reshape(2, 2, 3)

# print("\nOriginal array:\n", arr)
# print("Reshaped array:\n", newarr)


# # An exemplar array
# arr = np.array([[-1, 2, 0, 4],
#                 [4, -0.5, 6, 0],
#                 [2.6, 0, 7, 8],
#                 [3, -7, 4, 2.0]])

# # Slicing array
# temp = arr[:2, 1:2]
# print("Array with first 2 rows and alternate"
#       "columns(0 and 2):\n", temp)

# a = np.array([[1, 2],
#               [3, 4]])
# b = np.array([[4, 3],
#               [2, 1]])

# # add arrays
# print("Array sum:\n", a + b)

# # multiply arrays (elementwise multiplication)
# print("Array multiplication:\n", a*b)

# # matrix multiplication
# print("Matrix multiplication:\n", a.dot(b))


a = np.array([[1, 3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10, 12]])

# horizontal splitting
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 2))

# vertical splitting
print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(a, 2))
