import numpy as np
import random
# print(np.random.randint(1,10,4))
# print(np.random.randint(1,10,4))
a=np.array([1,2,3,4,5])
sample=np.random.choice(a,size=3,replace=False)
print(sample)