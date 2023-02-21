from typing import List

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    length = len(temperatures)
    # 构建一个单调栈， 栈里面存的是单调递减的 元素的index
    stack = []
    ans = [0] * length
    for i in range(length):
        t = temperatures[i]
        # stack 永远维持单调递减，如果不满足，就一直出栈到满足未知
        while stack and t > temperatures[stack[-1]]:
            prev_index = stack.pop()
             # ans, 下一个更大值在几天后， 所以是index相减
            ans[prev_index] = i - prev_index
        stack.append(i)
    return ans

arr = [1,3 ,5, 4,2]
res = dailyTemperatures(arr)
print(res)
