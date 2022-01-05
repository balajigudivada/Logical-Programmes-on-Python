import numpy as np
#0  dimension
arr=np.array(10)
print(arr.ndim," dimension")
print(arr)
#1  dimension
arr1=np.array([1,2,3,4])
print(arr1.ndim,"dimension")
print(arr1)
#2  dimension
arr2=np.array([[1,2,3],[3,4,5],[5,7,8]])
print(arr2.ndim,"dimension")
print(arr2)
arr3=np.array([[[1,2,3],[4,5,6]],[[1,3,6],[2,5,7]]])
print(arr3.ndim,"dimension")
print(arr3)