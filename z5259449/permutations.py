import pytest
def permutations(string):
    '''
    For the given string, compute the set of all permutations of the characters of that string. For example:
    >>> permutations('ABC')
    {'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}

    Params:
      string (str): The string to permute

    Returns:
      (set of str): Each string in this set should be a permutation of the input string.
    '''
    if(type(string) != str):
        raise ValueError
    if len(string) == 0:
        return ['']
    #recursively call the function with one less letter
    #to find all the possible combination 
    prevList = permutations(string[1:len(string)])
    nextList = []
    #loop through the list to append non-dupe into nextList
    for i in range(0,len(prevList)):
        #appends the string to all combination of other strings
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList
