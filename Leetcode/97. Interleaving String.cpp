class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size(), m = s2.size();
        if (s3.size() != n + m) return false;
        // vector<vector<bool>> dp (n+1, vector<bool>(m+1));
        bool dp[n+1][m+1];
        for (int i = 0; i <= n; i++){
            for (int j = 0; j <= m; j++){
                if (i == 0 && j == 0) {
                    dp[i][j] = true;
                }
                else if (i == 0) {
                    dp[i][j] = dp[i][j-1] && s2[j-1] == s3[i+j-1];
                }
                else if (j == 0) {
                    dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i+j-1];
                }
                else {
                    dp[i][j] = (dp[i][j-1] && s2[j-1] == s3[i+j-1]) || 
                                (dp[i-1][j] && s1[i-1] == s3[i+j-1]);
                }
            }
        }
        return dp[n][m];
    }
};

class Solution {
public:
    bool helper(string s1, int i, string s2, int j,string s3, int k, vector<vector<int>>& memo){
        int n = s1.size(), m = s2.size();
        if (i == n) return s2.substr(j) == s3.substr(k);
        if (j == m) return s1.substr(i) == s3.substr(k);

        if (memo[i][j] > -1){
            return memo[i][j] == 1 ? true : false;
        }

        bool ans = false;
        if (
            (s3[k] == s1[i] && helper(s1, i+1, s2, j, s3, k+1, memo))
            || 
            (s3[k] == s2[j] && helper(s1, i, s2, j+1, s3, k+1, memo))
            ){
            ans = true;
        } 
        memo[i][j] = ans ? 1 : 0;

        return ans;
    }

    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size(), m = s2.size();
        vector<vector<int>> memo (n, vector<int>(m, -1));
        return helper(s1, 0, s2, 0, s3, 0, memo);
    }
};

/* # Python

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def helper(s1, i, s2, j, s3, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if len(s1) == i:
                return s2[j:] == s3[k:]
            if len(s2) == j:
                return s1[i:] == s3[k:]
            ans = False
            if (s3[k] == s1[i] and helper(s1, i+1, s2, j, s3, k+1)) or (s3[k] == s2[j] and helper(s1, i, s2, j+1, s3, k+1)):
                ans = True
            return ans

        return helper(s1, 0, s2, 0, s3, 0)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def helper(s1, i, s2, j, s3, k, memo):
            if len(s3) == k:
                return len(s1) == i and len(s2) == j
            if len(s1) == i:
                return s2[j:] == s3[k:]
            if len(s2) == j:
                return s1[i:] == s3[k:]
            if (i, j) in memo:
                return True if memo[(i, j)] == 1 else False
            ans = False
            if (s3[k] == s1[i] and helper(s1, i+1, s2, j, s3, k+1, memo)) or (s3[k] == s2[j] and helper(s1, i, s2, j+1, s3, k+1, memo)):
                ans = True
            memo[(i, j)] = 1 if ans else 0
            return ans
        memo = {}
        return helper(s1, 0, s2, 0, s3, 0, memo)

        
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        if len(s3) != len(s1) + len(s2):
            return False
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                                (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                    
        print(dp)

        return dp[len(s1)][len(s2)]
    

c = Solution()


print(c.isInterleave(s1="aabcc",s2="dbbca",s3="aadbbbaccc"))
print(c.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
*/
