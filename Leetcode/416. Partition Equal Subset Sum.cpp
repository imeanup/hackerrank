class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if ((sum & 1) == 1){
            return false;
        }

        sum /= 2;

        int n = nums.size();
        vector<vector<bool>> dp(n+1, vector<bool>(sum+1, false));

        dp[0][0] = true;

        for (int i = 1; i < n + 1; i++)
            dp[i][0] = true;
        for (int j = 1; j < sum + 1; ++j)
            dp[0][j] = false;
        for (const auto &row : dp) {
            for (bool element : row) {
                cout << element << ' ';
            }
            cout << endl;
        }
        cout << "Result: "<< "\n";
        for (int i = 1; i < n+1; ++i){
            for (int j = 1; j < sum + 1; ++j){
                dp[i][j] = dp[i-1][j];
                if (j >= nums[i-1]){
                    dp[i][j] = (dp[i][j] || dp[i-1][j-nums[i-1]]);
                }
            }
        }

        for (const auto &row : dp) {
            for (bool element : row) {
                cout << element << ' ';
            }
            cout << endl;
        }

        return dp[n][sum];
    }
};

/*
The comment is explaining that the problem of partitioning an array into two subsets with equal sums can be thought of as a variation of the 0/1 knapsack problem. In the 0/1 knapsack problem, you have a set of items with weights and values, and a knapsack with a maximum weight capacity. The goal is to choose a subset of items such that the total weight is less than or equal to the knapsack's capacity and the total value is maximized.

In this case, the "items" are the numbers in the array `nums`, and the "knapsack" has a capacity of `sum/2`, where `sum` is the total sum of all numbers in `nums`. The goal is to choose a subset of numbers such that their total sum is equal to `sum/2`. If such a subset exists, then it means that the remaining numbers in `nums` also have a total sum of `sum/2`, so it's possible to partition `nums` into two subsets with equal sums.

The dynamic programming (DP) approach used in this code is similar to the one used to solve the 0/1 knapsack problem. The 2D DP array `dp[i][j]` represents whether it's possible to achieve a sum of `j` using the first `i` numbers in `nums`. The base case is when `i = 0` and `j = 0`, which means that it's possible to achieve a sum of 0 using 0 numbers (by choosing no numbers), so `dp[0][0]` is set to `true`.

The transition function describes how to compute the value of `dp[i][j]` based on the values of previous states. For each number `nums[i-1]`, we have two choices: either pick it or don't pick it. If we don't pick it, then `dp[i][j]` is equal to `dp[i-1][j]`, because we're ignoring `nums[i-1]` and only considering the first `i-1` numbers. If we do pick it, then we need to check if it's possible to achieve a sum of `j - nums[i-1]` using the first `i-1` numbers. If it is possible (i.e., if `dp[i-1][j-nums[i-1]]` is true), then it means that by adding `nums[i-1]` to that subset of numbers, we can achieve a sum of `j`. So in this case, `dp[i][j]` is also true.

The last loop in the code computes the values of the DP array using this transition function. It iterates over all possible values of `i` (from 1 to `n`) and all possible values of `j` (from 1 to `sum/2`). For each pair `(i, j)`, it first sets `dp[i][j]` to be equal to `dp[i-1][j]`, which corresponds to not picking `nums[i-1]`. Then it checks if `j >= nums[i-1]`. If this condition is true, then it means that we can potentially pick

*/
