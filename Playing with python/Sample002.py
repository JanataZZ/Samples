def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    res = []
    for i in range(len(L)):
        res.append(L[i] > thresh)     
    return res
    
print(elementwise_greater_than([1,2,3,4,5,6], 4))

