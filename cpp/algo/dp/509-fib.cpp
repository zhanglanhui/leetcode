//
// Created by DELL on 2021/5/24.
//


/*
一圆型游泳池如图所示，现在需在其周围建一圆型过道，并在其四周围上栅栏。栅栏价格为35元/米，过道造价为20元/平方米。
过道宽度为3米，游泳池半径由键盘输入。要求编程计算并输出过道和栅栏的造价。
图形描述：大圆嵌套小圆：
小圆在大圆中间，小圆为游泳池，大圆与小圆间隔为道。
*/
#include<iostream>

using namespace std;
const float PI = 3.14159;
const float FencePrice = 35;
const float ConcretePrice = 20;

class Solution {
public:
    int fib(int n) {
        int prev1 = 1;
        int prev2 = 0;
        int ans = 0;
        if (n <= 1)
            return n;
        for (int i = 2; i < n + 1; i++) {
            ans = prev1 + prev2;
            prev2 = prev1;
            prev1 = ans;
        }
        return ans;
    }
};

int main(int argc, char const *argv[]) {
    cout<<Solution().fib(4)<<endl;
    return 0;
}