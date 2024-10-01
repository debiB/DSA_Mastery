from collections import defaultdict 
from bisect import bisect_right
def longest_subsequence(s,d):

    max_len = 0 
    word_map = defaultdict(list)
    for i,j in enumerate(s):
        word_map[j].append(i)
    
    def check_sub(word):
        prev_pos = -1
        for w in word:
            idx = bisect_right(word_map[w],prev_pos)
            if idx < prev_pos:
                return  False
            if idx >= len(word_map[w]):
                return False 
        return True 



    for i in d: 
        res = False
        if len(i) > max_len:
            res = check_sub(i)
        if res: 
            max_len = max(max_len, len(i))
    return max_len
        



    