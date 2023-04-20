def merge_sort(left,right,arr):
    if left == right:
        return [arr[left]]
    mid = (left+right)//2
    l = merge_sort(left, mid, arr)
    r = merge_sort(mid+1, right,arr)
    return merge(arr, l, r)
def merge(arr, left, right):
    li = []
    i,j = 0,0
    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            li.append(left[i])
            i+=1
        else:
            li.append(right[j])
            j+=1
    if i < len(left):
        li.extend(left[i:])
    if j < len(right):
        li.extend(right[j:])
    return li
def test():
    assert merge_sort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert merge_sort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert merge_sort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    print("Great Job !!!")
test()
