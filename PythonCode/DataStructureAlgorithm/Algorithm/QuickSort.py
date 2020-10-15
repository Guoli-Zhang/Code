# encoding:utf-8

"""快速排序"""


def quick__sort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]
    left = start
    right = end
    while left < right:
        while left < right and alist[right] >= mid:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
    # 退出循环，left与right相遇， 即left==right,获得此轮mid，准备进入下一轮
    alist[left] = mid
    # 开启新一轮
    quick__sort(alist, start, left-1)
    quick__sort(alist, left+1, end)


if __name__ == "__main__":
    blist = [3, 0, 9, 1, 8, 6, 6, 8, 6, 3, 8, 3, 0, 4, 6, 6]
    print(blist)
    quick__sort(blist, 0, len(blist)-1)
    print(blist)


# >---<
def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]
        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1
            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]
            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base
        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


myList = [49, 38, 65, 97, 76, 13, 27, 49]
print("Quick Sort: ")

QuickSort(myList, 0, len(myList)-1)
print(myList)

