class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import deque, Counter
        
        map = Counter(s)
        
        n = len(s)
        
        bucket = [[] for _ in range(n+1)]
        
        for char, freq in map.items():
            bucket[freq].append(char)
            
        ans = []
        for freq in range(n, -1, -1):
            for char in bucket[freq]:
                ans.append(char*freq)
                
        return "".join(ans)
    
        '''
        Runtime: 191 ms, faster than 9.23% of Python3 online submissions for 
        Sort Characters By Frequency. Memory Usage: 23.7 MB, less than 9.93% 
        of Python3 online submissions for Sort Characters By Frequency.
        '''
        
        '''
        dic = Counter(s)
        
        arr = [[values, keys] for keys, values in dic.items()]
        
        arr.sort(key=lambda x:-x[0])
        
        ans = []
        
        for values, keys in arr:
            ans.append(keys * values)
            
        return "".join(ans)
        '''
        
        '''
        Runtime: 47 ms, faster than 91.75% of Python3 online submissions for Sort Characters 
        By Frequency. Memory Usage: 15.3 MB, less than 81.15% of Python3 online submissions 
        for Sort Characters By Frequency.
        '''
