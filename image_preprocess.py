import numpy as np

def rgb2gray(rgb):
    '''
    Parameters
    ----------
    rgb : shape (height, width, 3)

    Returns
    -------
    gray : shape (height, width)
    '''
    return rgb[:, :, 0] * 0.299 + rgb[:, :, 1] * 0.578 + rgb[:, :, 2] * 0.114