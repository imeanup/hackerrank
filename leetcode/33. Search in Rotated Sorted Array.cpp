int search(vector<int>& nums, int target) 
{
        auto skip_left  = [&]( int x) { return x >= nums[0] ? numeric_limits<int>::min() : x; };
        auto skip_right = [&] (int x) { return x < nums[0] ? numeric_limits<int>::max() : x; };
        auto adjust = [&] (int x) { return target < nums[0] ? skip_left(x) : skip_right(x); };
  
        auto it = lower_bound( nums.begin(), nums.end(), target, [&] (int x, int y) { return adjust(x) < adjust(y); } );
            
        return it != nums.end() && *it == target ? it-nums.begin() : -1;
}

/*
Explanation

Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. 
And the adjustment is done by comparing both the target and the actual element against nums[0]. 

*/
  
  
/*
Try to think in this way, It's essentially just deciding whether you are on the right side or not.
(nums[mid] < nums[0]) == (target < nums[0]) This line is checking if the target and current number is on the same side
If they are, we can assign num the actual number in the array
target < nums[0] ? -INFINITY : INFINITY This line is saying: Oh since the two numbers are on the different side, 
let's move the pointers to make them on the same side. So refer to the explanation above, if target < nums[0], 
that means the target is on the right side, so we assign negative infinity to move the low pointer to the right; 
otherwise, we assign the positive infinite to move high pointer to the left.
What I mean by left side and right side refers to left side or right side of the actual start of the soring array.
Hope this will help.
*/

/*
If nums[mid] and target are "on the same side" of nums[0], we just take nums[mid]. Otherwise we use -infinity or +infinity as needed.
*/

int search(vector<int>& nums, int target) {
    int lo = 0, hi = nums.size();
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        
        double num = (nums[mid] < nums[0]) == (target < nums[0])
                   ? nums[mid]
                   : target < nums[0] ? -INFINITY : INFINITY;
                   
        if (num < target)
            lo = mid + 1;
        else if (num > target)
            hi = mid;
        else
            return mid;
    }
    return -1;
}
