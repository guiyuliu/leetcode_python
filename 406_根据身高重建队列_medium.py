from typing import List
"""
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
请你重新构造并返回输入数组people 所表示的队列。返回的队列应该格式化为数组 queue ，
其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/queue-reconstruction-by-height


（套路）：一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，
或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。
"""
def reconstructQueue( people: List[List[int]]) -> List[List[int]]:
    # 对第一个元素身高从大到小排序。第二个元素从小到大排序(为了后面插入排序的正确性)
    people = sorted(people, key=lambda x: (-x[0], x[1]))

    i = 0
    while i < len(people):
        if i > people[i][1]:  # 如果元素的index 大于当前的i，把它插到前面去
            people.insert(people[i][1], people[i])
            # 此时这个people[i]的index 变成了i+1。因为已经在前面插入了，所以要把它移到后走
            people.pop(i + 1)
        i += 1
    # 这个方法是在原数列上变，也可以新建一个res=[] 插入
    return people


people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
res =reconstructQueue(people)
print(res)
