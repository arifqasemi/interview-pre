def OffLineMinimum(strArr):
    pool = []
    result = []

    for s in strArr:
        if s == "E":
            if pool:
                smallest = min(pool)
                result.append(smallest)
                pool.remove(smallest)
        else:
            pool.append(int(s))
    
    return result
