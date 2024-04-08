import numpy as np

def calculate(list):
        if len(list)!=9:
              raise ValueError("List must contain nine numbers.")
        
        
        ls=np.array(list).reshape(3,3)

        mean_columns=np.mean(ls,axis=0)
        mean_rows=np.mean(ls,axis=1)
        flatted_mean=(np.mean(ls))

        #Calculating de variance
        var_columns=np.var(ls,axis=0)
        var_rows=np.var(ls,axis=1)
        flatted_var=(np.var(ls))

        #Calculating the Standard deviation
        std_columns=np.std(ls,axis=0)
        std_rows=np.std(ls,axis=1)
        flatted_std=(np.std(ls))

        #Calculating the max
        max_columns=np.max(ls,axis=0)
        max_rows=np.max(ls,axis=1)
        flatted_max=(np.max(ls))
 
        #Calculating the min
        min_columns=np.min(ls,axis=0)
        min_rows=np.min(ls,axis=1)
        flatted_min=(np.min(ls))

        #Calculating the  sum
        sum_columns=np.sum(ls,axis=0)
        sum_rows=np.sum(ls,axis=1)
        flatted_sum=(np.sum(ls))
   




        return {
                'mean': [mean_columns.tolist(), mean_rows.tolist(), flatted_mean],
                'variance': [var_columns.tolist(), var_rows.tolist(), flatted_var],
                'standard deviation': [std_columns.tolist(), std_rows.tolist(), flatted_std],
                'max': [max_columns.tolist(), max_rows.tolist(), flatted_max],
                'min': [min_columns.tolist(), min_rows.tolist(), flatted_min],
                'sum': [sum_columns.tolist(), sum_rows.tolist(), flatted_sum]
}