class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        set<int> seen;
        for (int num : nums){
            if (seen.find(num) != seen.end()){
                return num;
            }
            else{
                seen.insert(num);
            }
        }
        return -1;
    }
};
