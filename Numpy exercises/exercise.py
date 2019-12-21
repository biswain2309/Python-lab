import numpy as np
import pandas as pd
lst = [5, 10, 0, 200]
arr = np.array(lst)
#print(arr+5)

lst1 = [1, 2, 3, 'text', True, 3+2j]
arr1 = np.array(lst1)
#print(type(arr1[3]),type(arr1[4]),type(arr1[5]))

lst2 = [56, 45, 12, 6]
arr2 = np.array(lst2)
#print(np.sys.getsizeof(lst2))
#print(arr.nbytes)

arr3 = np.array([2,5,6,8], dtype = int)
#print(type(arr3))
#print(np.result_type(arr3))

#print(np.linspace(0, 160, 5, dtype = np.float64))

arr4 = [25, 56, 12, 85, 34, 75]
arr5 = [42, 3, 86, 32, 856, 46]

arr4 = (np.array(arr4).reshape(2,3))
arr5 = (np.array(arr5).reshape(2,3))
arr4i = arr4.astype(complex)
arr5i = arr5.astype(complex)
result1 = np.square(arr4i) - np.square(arr5i)
#print(result1)
result2 = arr4i - arr5i
result = result1 / result2
#print(result)
arr8 = np.arange(4).reshape(4,-1)
#arr9 = np.array([[0,2]])
#print(arr8)
#print(arr8.shape)
arr6 = arr8.reshape(2,2)
twos_mat = np.ones((2, 4)) * 2
#print(twos_mat)

mat1 = np.zeros((4,4),dtype=np.float64)
mat2 = [0., 4., 0., 0.]
mat2arr = np.array(mat2)
mat3 = [0., 0., 5., 0.]
mat3arr = np.array(mat3)
r1 = mat1[0] + mat2arr
r2 = mat1[1] + mat3arr
#print(r1 + r2)

arr9 = np.arange(11)
#print(arr9)
m = (arr9 > 6) & (arr9 < 10)
arr9[m] *= -1
#print(arr9)
#print(np.linspace(0, 10, 5, dtype = np.int32))
arra = np.array([10,5,6,7]).reshape(2,-1)
#print(arra)
#print(arra.sum(axis = 0))
mat1 = np.matrix([[111, 1322],
                  [785, 554]])

#print(mat1.sum(axis = 1).shape)
#print(mat1.sum(axis = 1).shape)

arr = np.arange(9, dtype = "float").reshape(3,3)
#print(arr)
ind1 = np.array([[1,2],[0,1]])
ind2 = np.array([[0,2],[1,2]])
#print(ind1)
#print(ind2)
#print(arr[ind1, ind2])
#print(arr[ind1, ind2].sum())

import os.path
import skimage
from skimage.io import imread
from skimage import data_dir
import matplotlib.pyplot as plt
import numpy as np
# Original Image
img = imread(os.path.join(data_dir, 'ihc.png'))
plt.imshow(img)

mat1 = np.arange(4).reshape(2,2)
mat2 = (np.arange(4)*2).reshape(2,2)
mat3 = (np.arange(4)*3).reshape(2,2)

#print(mat1)
#print(mat2)
#print(mat3)

arri=np.floor(np.linspace(0,4,5))
#print(arri)

a = np.arange(8).reshape(4,-1)
#a1 = a.reshape(3,-1)
b = np.ceil(np.linspace(7,15,9)).reshape(3,-1)
#print(a)
#print(a1)
#print(b)
#print(np.greater_equal(a,b))
#print(np.count_nonzero(np.greater_equal(a,b)))

mat = np.matrix([0,1,2,3]).reshape(2,-1)
#print(np.linalg.det(mat))

df = pd.DataFrame([[2, 5],
                   [56, 20]],
                  index=list('pq'),
                  columns=list('ab'))
#print(df)

def loc(a, b):
    try:
        out = df.loc[a, b]
    except:
        return 0
    return out


def iloc(a, b):
    try:
        out = df.iloc[a, b]
    except:
        return 0
    return out

df = pd.DataFrame({'A' : [1,-4,7],
                   'B' : [-2,5,-8],
                   'C' : [-3,-6,9]},
                   index = list('STU'))
#print(df.apply(np.sum, axis = 0).sum())

df1 = pd.DataFrame({'A': [1,4,7],
                    'B': [2,5,8],
                    'C': [3,6,9]},
                    index = list ('PQR'))
df2 = pd.DataFrame({'A': [1,-4,-7],
                    'B': [-2,5,-8],
                    'C': [-3,-6,9]},
                    index = list ('STU'))
#print(df1.sub(df2))
#print(df1.sub(df2).count().sum())

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3,4,np.nan,-1],
                   [np.nan, np.nan, np.nan, 5]],
                  columns = list('ABCD'))
#print(df.dropna(axis = 1, how = 'all'))

df = pd.DataFrame([[15,12],
                  [33,54],
                  [10,32]],
                  index = ['one','two','three'],
                  columns = ['col1', 'col2'])
#print(df.filter(regex = 'e$', axis = 0))

df = pd.DataFrame([[15,12],
                   [33,54],
                   [10,32]],
                   columns = list('AB'))
#print(df.eval('B-A').median())

df = pd.DataFrame([[15,12], [33,54], [10,32]],
                   index = list('ABC'),
                   columns = list('DE'))
#print(df.iloc['B', 'D'])

df  = pd.DataFrame({'P1':[10,20,30],'P2':[["A","B","C"],["A","D","E"],["C","D","F"]]})
df['P3'] = df["P2"].apply(lambda x: " ".join(["_".join(i.split(" ")) for i in x]))
##print (df['P3'])

mat1 = np.array([[ 0,  1,  2,  3],
                 [ 4,  5,  6,  7],
                 [ 8,  9, 10, 11]])

indA = np.array([[2,2],[1,1]])
indB = np.array([[2,1],[1,0]])

mat1[indA, indB] = np.array([[100, 90],[50, 40]])
#print(mat1)

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5]],
                   columns=list('ABCD'))
df.cumsum(axis=1)
df.dropna(axis = 1, how = 'all')
#print(df.dropna(axis = 1, how='any'))

df1 = pd.DataFrame({'A': [1,4,7],
                    'B': [2,5,8],
                    'C': [3,6,9]},
                    index = list('PQR'))
df3 = pd.DataFrame({'A': [1,-4,-7],
                    'B': [-2,5,-8],
                    'C': [-3,-6,9]},
                    index = list('STU'))
#print(df1.sub(df3).count())

df = pd.DataFrame([[15, 12],
                   [33, 54],
                   [10, 32]],
                   index = ['one','two','three'],
                   columns = ['col1', 'col2'])

#print(df.filter(regex = 'e$', axis = 0).shape)
#print(df.filter(regex = '^c', axis = 1).shape)

arr1 = np.arange(4).reshape(2,2)
arr2 = arr1.copy()
arr2[1,1] = 50
#print(arr1)

num1 = 50
num2 = 2
num3 = 3
num4 = 8
r = num1//num4
print(r)
result = num1/num4-num3*num2+num4
#print(result)
1+1


#print(iloc(0, 'b'))
#print(loc(0, 'b'))
#print(loc('q', 'a'))
#print(iloc('q', 'b'))

"""mat = np.array([['abc', 'A'], ['def', 'B'], ['ghi', 'C'], ['jkl', 'D']])
arr10 = np.array(['abc', 'dfe', 'ghi', 'kjl'])
i=0
for row in mat:
    while arr10[i] = mat[row]
    print(mat)"""


