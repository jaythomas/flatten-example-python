def flatten(array):
    """ Return flattened copy of a list """
    if not isinstance(array, list):
        return [array]

    flat_array = []

    for val in array:
        for sub_val in flatten(val):
            flat_array.append(sub_val)

    return flat_array
