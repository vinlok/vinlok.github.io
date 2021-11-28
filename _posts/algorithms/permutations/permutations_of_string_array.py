def calculate_perms(a):

    '''algo:
    1. For a array with n elements the permutations are n!. Example: 3 elements = 3! = 6
    '''

    sol = [[]]
    for e in a:
        _sol = []

        for p in sol:
            for i in range(0, len(p) + 1):
                # print(p[:i] + [e] + p[i:])
                _sol.append(p[:i] + [e] + p[i:])
        print(sol)

        sol = _sol
    print(sol)



calculate_perms([1,2,3])