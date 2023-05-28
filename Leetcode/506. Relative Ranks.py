class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        mp = {}
        s_score = sorted(score, reverse = True)
        
        for i, s in enumerate(s_score):
            mp[s] = i + 1

        res = []
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        # print(mp)
        for s in score:
            pos = mp[s]
            if pos < 4:
                res.append(medals[pos-1])
            else:
                res.append(str(pos))

        return res
