def partion(nums, low, high):
    left = low
    right = high
    pivot = nums[left]
    print("left ",left, "right ", right)
    while left < right:
        while left < right and nums[right] > pivot:
            right -= 1
        # 直到、、、交换 右边的大值到左边， 锚点作为换位的中间点
        nums[left] = nums[right]
        # print(arr)
        while left < right and nums[left] <= pivot:
            left += 1
        # 把左边的值换到 右边
        nums[right] = nums[left]
        # print(arr)
    # 把锚点的值重新赋上
    nums[right] = pivot
    return right

def partion(nums, low, high):
    i = low
    location = low - 1  # loc指向最小的位置的末端
    pivot = nums[high]
    while i < high:
        if nums[i] <= pivot:
            location += 1
            nums[location], nums[i] = nums[i], nums[location]
        i += 1
    nums[location + 1], nums[high] = nums[high], nums[location+1]
    p = location + 1
    return p


def quick_sort(nums, low, high):
    if low < high:
        p = partion(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)

arr = [6, 1, 2, 3, 2, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)
