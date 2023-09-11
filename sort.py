# # x=[12,67,4,52,76,435]
# # x.sort()
# # print(x)
# def bubblesort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             print(arr)
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 print(arr)
#
# ele=[12,1,32,3,33,211,333,443]
# bubblesort(ele)
# print(f"{ele}")















def bubble_sort(x):
    n=len(x)
    for i in range (n):
        for j in range(0,n-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1]=x[j+1],x[j]
                print(x)

ele=[12,4,32,1,4,89]
bubble_sort(ele)
print(ele)

