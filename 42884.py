def solution(routes):
    ans, tmp = 0, -30_000
    routes.sort(key= lambda x : x[1])
    for start, end in routes:
        if tmp >= start: continue
        
        if tmp < end:
            tmp = end
            ans += 1
    return ans