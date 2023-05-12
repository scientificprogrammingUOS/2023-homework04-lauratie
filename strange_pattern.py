import numpy as np

# implement the function strange pattern

def strange_pattern(pattern):
    array = np.full(shape=pattern, fill_value=False)
    for index, i in enumerate(array):
        i[(0-index)%3::3] = True

    return array



if __name__ == "__main__":
    # use this for your own testing!
    strange_pattern((4,5))
    pass
