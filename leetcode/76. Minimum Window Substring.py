# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        n = len(s)
        mp = {}
        for c in t:
            mp[c] = mp.get(c, 0) + 1
        print(mp)
        count = len(mp)
        l = 0; r = float('inf')
        while j < n:
            if s[j] in mp:
                mp[s[j]] -= 1
                if mp[s[j]] == 0:
                    count -= 1
            if count == 0:
                while count == 0:
                    if r > j-i+1:
                        r = j-i+1
                        l = i
                    if s[i] in mp:
                        mp[s[i]] += 1
                        if mp[s[i]] > 0:
                            count += 1
                    i += 1
            j += 1
        return "" if r == float('inf') else s[l:r+l]
    
    
    def minWindow(self, s: str, t: str) -> str:

        # Initialize a dictionary to store the count of each character in t
        mp = {c: t.count(c) for c in t}

        # Initialize variables to keep track of the window
        i = 0 # start
        j = 0 # end
        r = float('inf') # min_length
        l = 0 # min_start

        # Initialize a counter to keep track of the number of unique characters in that have been matched so far
        matched = 0

        # Slide the window over the string s
        while j < len(s):
            # If the character at the end of the window is in t, decrement the count in the char_count dictionary
            if s[j] in mp:
                mp[s[j]] -= 1
                # If the count for this character becomes zero, it means that all instances of this character in t have been matched, so increment the matched counter
                if mp[s[j]] == 0:
                    matched += 1

            # If the matched counter is equal to the number of unique characters in t, it means that the window contains all of the characters in t, so we can try to shrink the window by moving the start pointer
            while matched == len(mp):
                # Update the minimum length if necessary
                if j - i + 1 < r:
                    r = j - i + 1
                    i = i

                # If the character at the start of the window is in t, increment the count in the char_count dictionary
                if s[i] in mp:
                    mp[s[i]] += 1
                    # If the count for this character becomes non-zero, it means that the window no longer contains all of the characters in t, so decrement the matched counter
                    if mp[s[i]] > 0:
                        matched -= 1

                # Move the start pointer to the right
                i += 1

            # Move the end pointer to the right
            j += 1

        # Return the minimum window substring, or an empty string if no such substring was found
        return s[i:i + j] if r != float('inf') else ''

'''
s = "ADOBECODEBANC"; t = "ABC"
# s = "a"; t = "a"
# s = "a"; t = "aa"
# s = "ab"; t = "a"

c = Solution()
print(c.minWindow(s, t))
'''
