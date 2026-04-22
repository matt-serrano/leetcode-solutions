class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> newNums;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    newNums.push_back(i);
                    newNums.push_back(j);
                }
            }
        }

        return newNums;
    }
};