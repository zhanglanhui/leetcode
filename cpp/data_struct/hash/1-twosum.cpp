//
// Created by DELL on 2021/7/26.
//

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end()) {
                return {it->second, i};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution tmp;
    vector<int> gg=vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    vector<int> xx = tmp.twoSum(gg, 7);
    for (auto array: xx) {
        std::cout << array << " ";
    }
    std::cout << std::endl;

    return 0;
}
