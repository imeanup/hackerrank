# Python code for 
### Approach 1: Top-Down Dynamic Programming 


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        ageScorePair = []
        for i in range(n):
            ageScorePair.append((ages[i], scores[i]))
        ageScorePair.sort(key=lambda x:(x[0], x[1]))
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.findMaxScore(dp, ageScorePair, -1, 0)

    def findMaxScore(self, dp, ageScorePair, prev, index):
        if index == len(ageScorePair):
            return 0

        if dp[prev + 1][index] != -1:
            return dp[prev + 1][index]

        if prev == -1 or ageScorePair[index][1] >= ageScorePair[prev][1]:
            dp[prev + 1][index] = max(self.findMaxScore(dp, ageScorePair, prev, index + 1), ageScorePair[index][1] + self.findMaxScore(dp, ageScorePair, index, index + 1))
            return dp[prev + 1][index]


        dp[prev + 1][index] = self.findMaxScore(dp, ageScorePair, prev, index + 1)
        return dp[prev + 1][index]



### Approach 2: Bottom-Up Dynamic Programming


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScorePair = [(ages[i], scores[i]) for i in range(len(scores))]
        ageScorePair.sort(key=lambda x: (x[0], x[1]))
        return self.findMaxScore(ageScorePair)

    def findMaxScore(self, ageScorePair: List[Tuple[int, int]]) -> int:
        n = len(ageScorePair)
        answer = 0
        
        dp = [0] * n
        for i in range(n):
            dp[i] = ageScorePair[i][1]
            answer = max(answer, dp[i])
            
        for i in range(n):
            for j in range(i-1, -1, -1):
                if ageScorePair[i][1] >= ageScorePair[j][1]:
                    dp[i] = max(dp[i], ageScorePair[i][1] + dp[j])
            answer = max(answer, dp[i])
            
        return answer



### Approach 3: Binary Indexed Tree (BIT) / Fenwick Tree


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score_pair = list(zip(ages, scores))
        age_score_pair.sort(key=lambda x: (x[1], x[0]))

        highest_age = max(ages)
        BIT = [0] * (highest_age + 1)
        
        answer = float('-inf')
        for age, score in age_score_pair:
            current_best = score + self.queryBIT(BIT, age)
            self.updateBIT(BIT, age, current_best)
            
            answer = max(answer, current_best)
        
        return answer

    def queryBIT(self, BIT, age):
        max_score = float('-inf')
        i = age
        while i > 0:
            max_score = max(max_score, BIT[i])
            i -= i & (-i)
        return max_score

    def updateBIT(self, BIT, age, current_best):
        i = age
        while i < len(BIT):
            BIT[i] = max(BIT[i], current_best)
            i += i & (-i)

