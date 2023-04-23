class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        map<int, int> cnt;
        for(int i = 0; i < k; i++){
            cnt[nums[i]]++;
        }
        auto get_kth = [&](int kt){
            for(auto [k, v] : cnt){
                if(v < kt) kt -= v;
                else return min(k, 0);
            }
            return 0;
        };
        int n = nums.size();
        vector<int> res;
        for(int i = 0; i < n - k + 1; i++){
            res.push_back(get_kth(x));
            cnt[nums[i]]--;
            if(i + k < n){
                cnt[nums[i + k]]++;
            }
        }
        return res;
    }
};
