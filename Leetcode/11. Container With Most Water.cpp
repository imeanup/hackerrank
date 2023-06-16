class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int i = 0, j = n - 1;
        int area = 0;
        while (i < j){
            int width = j - i;
            area = max(area, min(height[i], height[j])*width);
            if (height[i] <= height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return area;
    }
};
