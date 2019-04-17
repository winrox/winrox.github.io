# def binary_search(list, target):
#     start_time = datetime.datetime.now()
#     end_time = None
#     first = 0
#     last = len(list) - 1
#
#     while first <= last:
#         midpoint = (first + last) // 2
#
#         if list[midpoint] == target:
#             end_time = datetime.datetime.now()
#             return (midpoint, end_time - start_time)
#         elif list[midpoint] < target:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1
#
#     end_time = datetime.datetime.now()
#     return (None, end_time - start_time)
#
# def recursive_binary_search(list, target, start=0, end=None):
# if end is None:
#     end = len(list) - 1
# if start > end:
#     return -1
#
# mid = (start + end) // 2
#
# if target == list[mid]:
#     return mid
# else:
#     if target < list[mid]:
#         return recursive_binary_search(list, target, start, mid-1)
#     else:
#         return recursive_binary_search(list, target, mid+1, end)


# def reverse_str(str):
#     return str[::-1]
#
# def convert_to_list_reverse_str(str):
#     list = list(str)
#     list.reverse()
#     return "".join(list)
#
# def loop_reverse_str(str):
#     reversed_str = ""
#     for char in str:
#         reverse_str = char + reversed_str
#     return reversed_str
#
# def find_missing(list1, list2):
#     return list(set(list1) ^ set(list2))[0]
