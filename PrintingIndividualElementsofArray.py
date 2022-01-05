import numpy as np
arr=np.array([[[1,2],[3,5]],[[1,2],[3,5]]])
for i in arr:
    for j in i:
        for k in j:
            print(k)