"""
Unpickle.py Comp1531
Jackie Cai z5259449
"""

import pickle


def most_common():
    """function that opens a pickle file and finds the most common
    shape colour pair"""
    infile = open('shapecolour.p', 'rb')
    new_dict = pickle.load(infile)
    result = []
    for words in new_dict:
        new = words['shape'] + ' ' + words['colour']
        result.append(new)
    most = max(set(result), key=result.count)
    splitted = most.split()
    shape = splitted[0]
    colour = splitted[1]
    common = {
        'Colour': colour,
        'Shape': shape
    }
    return common
