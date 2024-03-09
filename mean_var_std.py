#Mean-Variance-Standard Deviation Calculator
#Juan Pablo Pulido Angel

import numpy as np

def calculate(list):

    if len(list)!=9:
       raise ValueError("The list must contain nine numbers")
    else:
        m=np.array(list).reshape(3,3)  #The list is converted to a matrix 3X3
        #Caulculating the mean
        axis1_mean=np.mean(m,axis=0)
        axis2_mean=np.mean(m,axis=1)
        flatted_mean=(np.mean(m))
        #Calculating de variance
        axis1_var=np.var(m,axis=0)
        axis2_var=np.var(m,axis=1)
        flatted_var=(np.var(m))
        #Calculating the Standard deviation
        axis1_std=np.std(m,axis=0)
        axis2_std=np.std(m,axis=1)
        flatted_std=(np.std(m))
        #Calculating the max
        axis1_max=np.max(m,axis=0)
        axis2_max=np.max(m,axis=1)
        flatted_max=(np.max(m))
        #Calculating the min
        axis1_min=np.min(m,axis=0)
        axis2_min=np.min(m,axis=1)
        flatted_min=(np.min(m))
        #Calculating se sum
        axis1_sum=np.sum(m,axis=0)
        axis2_sum=np.sum(m,axis=1)
        flatted_sum=(np.sum(m))

    return {
        "Mean": [axis1_mean.tolist(),axis2_mean.tolist(),flatted_mean],
        "Variance": [axis1_var.tolist(),axis2_var.tolist(),flatted_var],
        "Standard deviation": [axis1_std.tolist(),axis2_std.tolist(),flatted_std],
        "Max": [axis1_max.tolist(),axis2_max.tolist(),flatted_max],
        "Min": [axis1_min.tolist(),axis2_min.tolist(),flatted_min],
        "Sum": [axis1_sum.tolist(),axis2_sum.tolist(),flatted_sum],
    }

results=calculate([0,1,2,3,4,5,6,7,8])
print(results)
