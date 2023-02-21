"""
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：

每一对相邻的单词只差一个字母。
 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
sk == endWord
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
链接：https://leetcode.cn/problems/word-ladder

广度优先搜索
优化建图？

"""


import queue

def ladderLength(beginWord, endWord, wordList):
    if len(wordList) == 0:
        return 0
    if endWord not in wordList:
        return 0

    q = []
    q.append(beginWord)
    wordList.append(beginWord)
    wordst = set(wordList)
    wordList = list(wordst)
    ret = 0
    while len(q) != 0:
        ret += 1
        size = len(q)
        for i in range(size):
            top = q[0]
            if top == endWord: return ret
            q.pop(0)
            for w in range(len(wordst)):
                word = wordList[w]
                if word == "" or len(word) != len(beginWord): continue
                diff = 0
                for j in range(len(word)):
                    if(word[j] != top[j]):
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    q.append(word)
                    wordList[w]= ""
    return ret

begin = "hit"
end = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
ret =  ladderLength(begin, end, wordList)
print("ret is ", ret)
