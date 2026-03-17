"""
Create a function named calculate() in mean_var_std.py that uses Numpy to output
the mean, variance, standard deviation, max, min, and sum of the rows, columns,
and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function
should convert the list into a 3 x 3 Numpy array, and then return a dictionary
containing the mean, variance, standard deviation, max, min, and sum along both
axes and for the flattened matrix.
The returned dictionary should follow this format:
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
If a list containing less than 9 elements is passed into the function, it should raise
a ValueError exception with the message: "List must contain nine numbers."
The values in the returned dictionary should be lists and not Numpy arrays.

For example, calculate([0,1,2,3,4,5,6,7,8]) should return:
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
Development
Write your code in mean_var_std.py. For development, you can use mean_var_std.py to test
your code. In order to run your code, type python3 mean_var_std.py into the Ona terminal
and hit enter. This will cause the included CPython interpreter to run the mean_var_std.py
file.

Testing
The unit tests for this project are in test_module.py. We imported the tests from
test_module.py to mean_var_std.py for your convenience.

Submitting
Copy your project's URL and submit it to freeCodeCamp.
"""
import numpy as np

#arr = np.array([0,1,2,3,4,5,6,7,8])

def calculate(array):
    if array.shape[1] != 9:
        raise ValueError('Array must have 9 dimensions')
    narray = np.reshape(array,(3,3))

    mean0 = np.mean(narray, axis=0).tolist()
    mean1 = np.mean(narray, axis=1).tolist()
    mean =np.mean(array).tolist()

    var0 = np.var(narray, axis=0).tolist()
    var1 = np.var(narray, axis=1).tolist()
    var_ = np.var(array).tolist()

    sdev0 = np.std(narray, axis=0).tolist()
    sdev1 = np.std(narray, axis=1).tolist()
    sdev = np.std(array).tolist()

    max0 = np.max(narray, axis=0).tolist()
    max1 = np.max(narray, axis=1).tolist()
    max_ = np.max(array).tolist()

    min0 = np.min(narray, axis=0).tolist()
    min1 = np.min(narray, axis=1).tolist()
    min_ = np.min(array).tolist()

    sum0 = np.sum(narray, axis=0).tolist()
    sum1 = np.sum(narray, axis=1).tolist()
    sum_ = np.sum(array).tolist()

    ans = {
    'mean': [mean0, mean1, mean],
    'variance': [var0, var1, var_],
    'standard deviation': [sdev0, sdev1, sdev],
    'max': [max0, max1, max_],
    'min': [min0, min1, min_],
    'sum': [sum0, sum1, sum_]
    }
    return ans


#calculate(arr)
