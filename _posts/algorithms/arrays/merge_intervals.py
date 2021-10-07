def merge_intervals(intervals):

    [s,e] = intervals[0]
    r=[]
    for i in range(1,len(intervals)):

        [n_s,n_e]=intervals[i]

        if n_s <= e:
            if n_e > e:
                e = n_e

            # r.append([s,e])
        elif n_s > e:
            r.append([s,e])
            s=n_s
            e=n_e
    r.append([s,e])
    print(r)





intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals=[[1,4],[4,5]]
merge_intervals(intervals)
#Output should be: [[1,6],[8,10],[15,18]]