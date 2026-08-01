# # Python List → General-purpose container
# # NumPy Array → Super-fast container for numbers
#
# numbers = [10, 20, 30, 40]
# import numpy as np
#
# number = np.array([10, 20, 30, 40]) # Creating a 1D Array
# value = np.array( # 2D Array
#     [1,2,3],
#     [4,5,6])
# integer = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) # N dimensional array
# print(integer)
# print(type(numbers))
# print(number)
# print(type(number))
# print(numbers)
import numpy as np
number = np.array([1,2,3,4,5,6,7,8,9])
print(number - 5) # Subtracting from a numpy array
print(number + 5) # Adding from a numpy array
print(number * 5) #
print(number / 5)

b = np.array([1,2,3,4])
c = np.array([5,6,7,8])
print(b + c)

# Similarly, a NumPy array has:
# Number of dimensions (ndim)
# Shape
# Size
# Data type
# Memory size
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr.ndim)
print(number.ndim) # Dimension of the numpy array
print(number.itemsize) #This tells you how many bytes each element uses in memory.
print(arr.shape) # This tells you the number of rows and columns.
# How to access elements in a 3D array arr[1, 0, 1]
print(arr.dtype) # Giving the data type of the array
print(arr.size) # tells you the total number of elements (values) inside an array.

# Creating numpy arrays with predefine elements instead of writing the elements manually
types = np.zeros(5) # Creating a numpy array with 5 zeros
name  = np.zeros((3,2)) # Creating a 2D numpy array with zeros
one = np.ones((3,2)) # Same
two = np.empty(5) # Creating a 1D array without initialising
three = np.empty((3,2)) # Same
four = np.full((5,7))  # Creates an array filled with a specific value you choose: Output = [7,7,7,7,7], syntax np.full(shape, fill_value)
five = np.full((3,3),10)
six = np.eye(3) # Creating an identity matrix
seven = np.identity(3) # Still creating an identity matrix
eight = np.eye(3,3,3)
nine  = np.arange(5)
print(np.arange(1,10,2)) # It works like Python's range() but returns a NumPy array
print(types)
ten = np.random.randint(1,9,) # Creating a random integer
eleven = np.random.randint(1,10,5) # Creating random integers in the range 1 to 10
twelve = np.random.rand() # Generating random floats between 0 and 1 by default
thirteen = np.random.rand(2,5) # Random floats between 2 and 5
fourteen  = np.random.choice(ten) # Choosing a number randomly from a give list
fifteen = np.random.choice(ten,5) # Choosing multiple values
sixteen = np.random.choice(ten,replace=False) # Choosing random integer without replacement
np.random.shuffle(ten) # randomly changes the order of elements in an array.
print(number.shape())
number.flatten() # Converting an n size dimensional array into 1D array
number.reshape(10)
np.save("model_data.npy", arr)
np.load("model_data.npy")
number.copy() # Creating an independent copy of an array
ab = np.array([1,2,3])
ba = np.array([4,5,6])
result = np.hstack((ab,ba)) # Horizontal stack: Used to join 2 arrays together horizontally
a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
# Output
# [[1 2 5 6]
#  [3 4 7 8]]
print(np.hstack((a,b)))
print(result)
a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
# Output
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
print(np.vstack((a,b)))
arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
result = np.hsplit(arr, 2) # Used to split the array horizontally into 2 parts
print(result)
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
result = np.vsplit(arr, 2) # Used to split the array vertically into 2 parts
print(result)