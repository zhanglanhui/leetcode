#!/usr/bin/python3
from typing import List
from collections import OrderedDict

# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
#
# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from random import choice


class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_12 = obj.insert(2)
param_121 = obj.insert(3)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_3)
