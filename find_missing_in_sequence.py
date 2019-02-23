def find_missing(seq):
    diffs = {}
    prev = None
    for num in seq:  
        if prev == None:
            prev = num
        else: 
            if (num-prev) not in diffs:
                diffs[num-prev] = [0,[]]    
            diffs[num-prev][0]+=1
            diffs[num-prev][1].append(num)
            prev = num
    ans = -1
    afterMissing = -1
    interval = -1
    for diff in diffs:
        if diffs[diff][0] == 1:
            afterMissing = diffs[diff][1][0]
        else: 
            interval = diff
    ans = afterMissing - interval
    return(ans)
