"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
链接：https://leetcode.cn/problems/valid-parentheses
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # 遇到左括号时入栈，遇到右括号时讲对应栈顶的
        if len(s) == 0 or len(s) %2 == 1:
            return False
        left = ["(", "{", "["]
     
        match = { ")": "(", "}":"{", "]":"["}
        stack = []
        for i in s:  
            if stack and i in match:
                if match[i] == stack[-1]: #当右括号能和栈顶的左括号配上对，左括号出栈
                    stack.pop()
                else: 
                    return False # 如果匹配不上，直接return false
            else: stack.append(i) # 如果是右括号就入栈，
        return not stack

