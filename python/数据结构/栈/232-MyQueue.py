# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
#
# 实现 MyQueue 类：
#
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
#  
#
# 说明：
#
# 你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front_num = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1 and not self.s2: self.front_num = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        ans = self.s2.pop()
        # 这块需要注意
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        self.front_num = self.s2[-1] if self.s2 else None
        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front_num

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
