import numpy as np

def one_hot(labels, depth, on_value=1.0, off_value=0.0):
    """ Takes an numpy array and replaces the last axis with a one_hot encoding

    Args:
            labels (np.ndarray): Input array
            depth (int): amount of classes in one_hot encoding

    Returns:
            (np.ndarray) one_hot encoding with shape labels.shape + (depth,)

    The inverse of one_hot is np.argmax(one_hot_array, axis=-1)
    """
    y = np.array(labels)
    one_hot = np.ones(y.shape + (depth,)) * off_value
    one_hot[..., np.arange(y.shape[-1]), y.astype(int)] = on_value
    return one_hot

def softmax(y, axis=-1):
    """ softmax function in numpy
    applies to the last axis.
    """
    # we don't want to get rid of the sum axis, so we store the desired shape
    sumshape = list(y.shape)
    sumshape[axis] = 1
    sumshape = tuple(sumshape)
    return np.exp(y) * 1.0 / np.sum(np.exp(y), axis=axis).reshape(sumshape)
