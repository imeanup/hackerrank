class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)

        if n != m:
            return False
        s, goal = list(s), list(goal)
        left, right = -1, -1
        diff_count = 0
        for i in range(n):
            if s[i] != goal[i]:
                diff_count += 1
                if left == -1:
                    left = i
                else:
                    right = i
        
        if diff_count == 0:
            return len(set(s)) < n
        elif diff_count == 2:
            s[left], s[right] = s[right], s[left]
            return s == goal
        else:
            return False

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
                if freq[ord(ch) - ord('a')] == 2:
                    return True
            return False

        left = -1
        right = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if left == -1:
                    left = i
                elif right == -1:
                    right = i
                else:
                    return False
        if right == -1:
            return False
        return s[left] == goal[right] and s[right] == goal[left]
