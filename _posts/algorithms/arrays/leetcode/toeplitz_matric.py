def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool

    Algo:

    1. For ToeplitzMatrix, the vals at r-c should be same.
    2. Now iterate over the val using enumerate and see if the r-c is same. Use dictionary to track r-c
    """

    location_map={}

    for r, row in enumerate(matrix):
        for c,col in enumerate(row):
            print(r,c,col)
            if r-c in location_map:
                if location_map[r-c] != col:
                    return False
            else:
                location_map[r-c] = col

    return True
matrix = [[1,2,3,4],[5,1,2,3],[9,5,2,2]]


print(isToeplitzMatrix(matrix))