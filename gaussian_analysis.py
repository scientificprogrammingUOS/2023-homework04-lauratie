import numpy as np

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if type(loc)and type(scale)and type(lower_bound) and type(upper_bound) in [int,float]:
        if lower_bound < upper_bound:
            gaussian = np.random.normal(loc = loc, scale = scale, size = 100)
            mask = (gaussian <= upper_bound) & (gaussian >= lower_bound)
            gaussian = gaussian[mask]
            statistics = (np.mean(gaussian), np.std(gaussian))
            return statistics        
        else:
            raise TypeError ("make sure your lower bound is smaller than your upper bound") 
    else:
        raise ValueError ("make sure all attributes are of type int or float") 
    # delete the NotImplementedError when you write your function.

if __name__ == "__main__":
    gaussian_analysis(2,3,1,5)


    pass
