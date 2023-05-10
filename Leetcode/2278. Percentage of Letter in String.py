class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        mp = Counter(s)
        if letter in mp.keys():
            percentage = mp[letter] / len(s) * 100
            return int(percentage)
        else:
            return 0
