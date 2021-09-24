# https://leetcode.com/problems/design-a-stack-with-increment-operation/

# Brute force - O(n)
# class CustomStack:
#
#     def __init__(self, maxSize: int):
#         self.__data = []
#         self.__max = maxSize
#
#     def push(self, x: int) -> None:
#         if len(self.__data) == self.__max:
#             return
#         self.__data.append(x)
#
#     def pop(self) -> int:
#         if len(self.__data) == 0:
#             return -1
#         return self.__data.pop()
#
#     def increment(self, k: int, val: int) -> None:
#         for i in range(k):
#             if i < len(self.__data):
#                 self.__data[i] = self.__data[i] + val


# 0(1) time and O(N) Space
#can also use list/stack instead of dict
class CustomStack:
    def __init__(self, maxSize: int):
        self.increament_at = collections.defaultdict(lambda: 0)
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        tmp = self.increament_at[len(self.stack) - 1]
        self.increament_at[len(self.stack) - 2] += tmp
        self.increament_at[len(self.stack) - 1] = 0
        return self.stack.pop() + tmp

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            self.increament_at[len(self.stack) - 1] += val
        else:
            self.increament_at[k - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)